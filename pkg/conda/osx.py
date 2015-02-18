import os, glob
from os.path import basename, join
from conda_build import macho


"""

fixes some `rpath` by python, since I can't figure out how to resolve the following in CMake


this paths:
	@rpath/./libstdc++.6.dylib (compatibility version 7.0.0, current version 7.18.0)

need to be transformed into:
	@loader_path/./libstdc++.6.dylib (compatibility version 7.0.0, current version 7.18.0)


"""
PREFIX = os.getenv('PREFIX')
PYOCC = join(PREFIX, 'lib/python2.7/site-packages/OCC')


def ch_link_libstdcplusplus(path, link):
    if "libstdc++" in link and link.startswith("@rpath"):
        return link.replace("@rpath/./libstdc++.6.dylib", "@loader_path/../../../libstdc++.6.dylib")


def main():
    for path in glob.glob(join(PYOCC, "*.so")):
        if macho.is_dylib(path) or macho.is_macho(path):
            macho.install_name_change(path, ch_link_libstdcplusplus)


if __name__ == '__main__':
    main()

#!/bin/bash

echo "conda build directory is:" `pwd`
export PYTHONOCC_VERSION=`python -c "import OCC;print OCC.VERSION"`
echo "building pythonocc-core version:" $PYTHONOCC_VERSION

# see https://github.com/conda/conda-build/pull/312
export DYLD_LIBRARY_PATH="" #"$PREFIX/lib:$DYLD_LIBRARY_PATH"

backup_prefix=$PREFIX

ncpus=1
if test -x /usr/bin/getconf; then
    ncpus=$(/usr/bin/getconf _NPROCESSORS_ONLN)
fi

#swig_incl_dir=`$PREFIX/bin/swig -swiglib`
# see: https://github.com/ContinuumIO/anaconda-issues/issues/164
# setting the $SWIG_LIB variable as a temporary bypass
export SWIG_LIB=$PREFIX/share/swig/2.0.10
echo "swig <<<"$SWIG_LIB">>>"

echo "Timestamp" && date
cmake -DCMAKE_INSTALL_PREFIX=$PREFIX \
      -DCMAKE_OSX_DEPLOYMENT_TARGET=10.9 \
      -DCMAKE_CXX_FLAGS=-stdlib=libstdc++ \
      -DSWIG_DIR=$SWIG_LIB \
      -DOCE_INCLUDE_PATH=$PREFIX/include/oce \
      -DPYTHON_LIBRARY=$PREFIX/lib/libpython2.7.dylib \
      -DSWIG_EXECUTABLE=$PREFIX/bin/swig \
      -DOCE_LIB_PATH=$PREFIX/lib\
      -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
      -DCMAKE_C_COMPILER=/usr/bin/clang \
      $SRC_DIR

echo ""
echo "Timestamp" && date
echo "Starting build with -j$ncpus ..."
make -j$ncpus
make install
echo "Done building and installing pythonocc-core" && date

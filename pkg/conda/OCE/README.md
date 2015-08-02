OCE_INSTALL_PREFIX -> this needs to be set to Conda's prefix

for linux, use this channel for freeimage:
conda install -c https://conda.binstar.org/mutirri freeimage

perhaps run_test.py should run "make test", but that's a bit of a hassle. would be better if you can specify a shell script for testing
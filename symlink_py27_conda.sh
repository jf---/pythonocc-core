#!/bin/bash

pyocc_root="/Users/jelleferinga/GIT/pythonocc-core/src/addons"

CONDA=~/miniconda/envs/pyrapid-test
PYOCC=$CONDA/lib/python2.7/site-packages/OCC/

cd $PYOCC

rm -rf DataExchange
rm -rf Utils
rm -rf Display
rm -rf KBE

ln -s $pyocc_root/DataExchange $PYOCC/DataExchange
ln -s $pyocc_root/Utils $PYOCC/Utils
ln -s $pyocc_root/Display $PYOCC/Display
ln -s $pyocc_root/KBE $PYOCC/KBE





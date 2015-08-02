#!/bin/sh

export NP_INC=`python -c "import numpy; print numpy.get_include()"`
echo "numpy include directory: " $NP_INC

mkdir build
cd build

#cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
#-DCMAKE_C_COMPILER=/usr/bin/clang \
#-DVTK_SMP_IMPLEMENTATION_TYPE=TBB \
#-DVTK_RENDERING_BACKEND=OpenGL2 \
#-DVTK_PYTHON_VERSION=2.7 \
#-DVTK_LEGACY_REMOVE=ON \
#-DCMAKE_INSTALL_PREFIX:PATH="$PREFIX" \
#-DCMAKE_INSTALL_RPATH:STRING="$PREFIX/lib" \
#-DBUILD_TESTING:BOOL=OFF \
#-DBUILD_EXAMPLES:BOOL=OFF \
#-DBUILD_SHARED_LIBS:BOOL=ON \
#-DPYTHON_EXECUTABLE:FILEPATH=$PYTHON \
#-DPYTHON_INCLUDE_DIR=$PREFIX/include/python2.7 \
#-DVTK_Group_Qt=ON \
#-DVTK_Group_Views=ON \
#-DVTK_Group_Imaging=ON \
#-DPYTHON_INCLUDE_PATH:PATH=$PREFIX/include/python2.7 \
#-DPYTHON_LIBRARY:FILEPATH=$PREFIX/lib/$PY_LIB \
#-DVTK_WRAP_PYTHON:BOOL=ON \
#-DModule_vtkParallelMPI=ON \
#-DModule_vtkPython=ON \
#-DModule_vtkPythonInterpreter=ON \
#-DModule_vtkRenderingContextOpen=ON \
#-DModule_vtkRenderingExternal=OFF \
#-DModule_vtkRenderingMatplotlib=ON \
#-DModule_vtkRenderingOpenGL2=ON \
#-DModule_vtkRenderingQt=ON \
#-DModule_vtkViewsQt=ON \
#-DModule_vtkWrappingPythonCore=ON \
#-DModule_vtkWrappingTools=ON \
#-DModule_vtkRenderingParallel=OFF \
#-DModule_vtkmpi4py=ON \
#-DModule_vtkGUISupportQtOpenGL=ON \
#-DModule_vtkGUISupportQt=ON \
#-DModule_vtkFiltersReebGraph=ON \
#-DCMAKE_RANLIB=/usr/bin/ranlib \
#-DCMAKE_INSTALL_NAME_TOOL==/usr/bin/install_name_tool \
#-DCMAKE_LINKER=/usr/bin/ld \
#-DCMAKE_NM=/usr/bin/nm \
#-DCMAKE_STRIP=/usr/bin/strip \
#-DCMAKE_AR=/usr/bin/ar \
#-DQT_MOC_EXECUTABLE=$PREFIX/bin/moc \
#-DQT_RCC_EXECUTABLE=$PREFIX/bin/rcc \
#-DQT_UIC_EXECUTABLE=$PREFIX/bin/uic
#..


cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
    -DCMAKE_C_COMPILER=/usr/bin/clang \
    -DVTK_RENDERING_BACKEND=OpenGL2 \
    -DVTK_PYTHON_VERSION=2.7 \
    -DVTK_LEGACY_REMOVE=ON \
    -DCMAKE_INSTALL_PREFIX:PATH="$PREFIX" \
    -DCMAKE_INSTALL_RPATH:STRING="$PREFIX/lib" \
    -DBUILD_TESTING:BOOL=OFF \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DPYTHON_EXECUTABLE:FILEPATH=$PYTHON \
    -DPYTHON_INCLUDE_DIR=$PREFIX/include/python2.7 \
    -DPYTHON_INCLUDE_PATH:PATH=$PREFIX/include/python2.7 \
    -DPYTHON_LIBRARY:FILEPATH=$PREFIX/lib/libpython2.7.dylib \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DCMAKE_RANLIB=/usr/bin/ranlib \
    -DCMAKE_INSTALL_NAME_TOOL==/usr/bin/install_name_tool \
    -DCMAKE_LINKER=/usr/bin/ld \
    -DCMAKE_NM=/usr/bin/nm \
    -DCMAKE_STRIP=/usr/bin/strip \
    -DCMAKE_AR=/usr/bin/ar \
    -DQT_MOC_EXECUTABLE=$PREFIX/bin/moc \
    -DQT_RCC_EXECUTABLE=$PREFIX/bin/rcc \
    -DQT_UIC_EXECUTABLE=$PREFIX/bin/uic \
    ..

#VTK_Group_Qt
#-DVTK_SMP_IMPLEMENTATION_TYPE=TBB \


#-DVTK_ENABLE_KITS=ON \
#-DVTK_HAS_FEENABLEEXCEPT:BOOL=OFF \
# Module_vtkFiltersMatlab probably useful
# Module_vtkAcceleratorsDax dunno
# Module_vtkAcceleratorsPiston cool GPU stuff
#Module_vtkRenderingFreeTypeFon
#Module_vtkRenderingFreeTypeOpe

make -j8
make install
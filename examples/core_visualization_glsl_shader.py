##Copyright 2010-2014 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

#-------------------------------------------------------------------------------
# Example for attaching GLSL shaders to shapes
# GLSL stands for OpenGL Shader Language
# Find out more about GLSL here: http://www.lighthouse3d.com/opengl/glsl/
#-------------------------------------------------------------------------------

import os, glob

import sys

import time
from OCC.Display.OCCViewer import to_string
from OCC.Display.SimpleGui import init_display
from OCC.BRepPrimAPI import BRepPrimAPI_MakeSphere
from OCC.Graphic3d import (Graphic3d_ShaderProgram, Graphic3d_TOS_VERTEX, Graphic3d_TOS_FRAGMENT,
                           Graphic3d_ShaderObject)
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.STEPControl import STEPControl_Reader
from OCC.TCollection import TCollection_AsciiString

display, start_display, add_menu, add_function_to_menu = init_display()
from OCC.BRepTools import breptools_Read
from OCC.TopoDS import TopoDS_Shape
from OCC.BRep import BRep_Builder


def step():
    tA = time.time()
    step_reader = STEPControl_Reader()
    # status = step_reader.ReadFile("""/Users/jelleferinga/Dropbox (Odico)/Odico 05 RD/01 Hardware/01 Documentation/Drawings From Per's computer/Portal Robot irb6620/Tool/Full/baumer_wiresaw_full.stp""")
    status = step_reader.ReadFile("""/Users/jelleferinga/Dropbox (Odico)/Odico 02 xPro-Archive/C 064 Playscape/003 Picnicsten/01 Recieved drawings/25669_2014-06-10_Playscapes_07.stp""")

    if status == IFSelect_RetDone:  # check status
        failsonly = False
        step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
        step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)

        ok = step_reader.TransferRoot(1)
        _nbs = step_reader.NbShapes()
        aResShape = step_reader.Shape(1)
    else:
        sys.exit()
    print "loading step file took: ", time.time() - tA
    return aResShape

# render the sphere with default shading attributes ( no GLSL shader attached! )
shape = step()
anIO = display.DisplayShape(shape, update=True)

# returns the directory where OCE stores the GLSL shaders
# _shader_dir = #Graphic3d_ShaderProgram.ShadersFolder()
# convert the returned TCollection_AsciiString to a python string
# shader_dir = "".join([_shader_dir.Value(x+1) for x in range(_shader_dir.Length())])
shader_dir = "/Users/jelleferinga/miniconda/envs/_test/share/oce-0.18-dev/src/Shaders"

# look for the shaders stored in the shader folder...
# only a single vertex (vs) and fragment (fs) shader for the moment
_phong_vs = glob.glob(os.path.join(shader_dir, "*.vs"))[0] # PhongShading.vs
_phong_fs = glob.glob(os.path.join(shader_dir, "*.fs"))[0] # PhongShading.fs

# construct TCollection_AsciiString from string
fs = TCollection_AsciiString(_phong_fs)
vs = TCollection_AsciiString(_phong_vs)
# fs = TCollection_AsciiString("/Users/jelleferinga/GIT/pythonocc-core/examples/shaders/pink.fs")
# vs = TCollection_AsciiString("/Users/jelleferinga/GIT/pythonocc-core/examples/shaders/pink.vs")
# fs = TCollection_AsciiString("/Users/jelleferinga/miniconda/envs/_test/share/oce-0.18-dev/src/Shaders/RaytraceSmooth.fs")
# vs=TCollection_AsciiString("/Users/jelleferinga/miniconda/envs/_test/share/oce-0.18-dev/src/Shaders/RaytraceRender.vs")

# construct the shader, load, compile and attach the GLSL programs
aProgram = Graphic3d_ShaderProgram()
aProgram.AttachShader(Graphic3d_ShaderObject.CreateFromFile(Graphic3d_TOS_FRAGMENT, fs ) )
aProgram.AttachShader(Graphic3d_ShaderObject.CreateFromFile(Graphic3d_TOS_VERTEX, vs ) )

# attach the shader to the AIS_Shape representation that renders the sphere
aspect = anIO.GetObject().Attributes().GetObject().ShadingAspect().GetObject().aspect().GetObject()
# h_aProgram = aspect.ShaderProgram() # returns a Graphic3d_ShaderProgram_Handle
#-------------------------------------------------------------------------------
# h_aProgram -> Graphic3d_ShaderProgram_Handle cannot be cast to a Graphic3d_ShaderProgram
# aProgram has not method .GetHandle...
# aspect.SetShader requires a `Graphic3d_ShaderProgram_Handle` instance
#-------------------------------------------------------------------------------
sm = display.Context.MainPrsMgr().GetObject().StructureManager()
global_shader = sm.GetObject().FillArea3dAspect().GetObject().ShaderProgram()

aProgram.This()

# attach to a single shape
# aspect.SetShaderProgram(aProgram.GetHandle())
#
# aspect.SetShaderProgram(global_shader)
#
# from OCC.Graphic3d import Graphic3d_ShaderObject_CreateFromFile
from OCC.Graphic3d import Graphic3d_ShaderObject_CreateFromSource

# vs = TCollection_AsciiString("/Users/jelleferinga/miniconda/envs/_test/share/oce-0.18-dev/src/Shaders/PhongShading.vs")
# eee = Graphic3d_ShaderObject_CreateFromSource(Graphic3d_TOS_VERTEX, vs)

# from PyQt5.QtCore import pyqtRemoveInputHook
# pyqtRemoveInputHook()
# import ipdb; ipdb.set_trace()


aspect.SetShaderProgram(aProgram.GetHandle())

# aProgram.AttachShader(eee)

# update the rendering attributes such that the sphere is rendered with the GLSL shader
display.Context.Redisplay(anIO)

display.FitAll()

# type(aspect.ShaderProgram())
# Out[76]: SwigPyObject



# start the GUI event loop
start_display()

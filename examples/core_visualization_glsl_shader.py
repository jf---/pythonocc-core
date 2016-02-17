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

from OCC.Display.OCCViewer import to_string
from OCC.Display.SimpleGui import init_display
from OCC.BRepPrimAPI import BRepPrimAPI_MakeSphere
from OCC.Graphic3d import (Graphic3d_ShaderProgram, Graphic3d_TOS_VERTEX, Graphic3d_TOS_FRAGMENT,
                           Graphic3d_ShaderObject)
from OCC.TCollection import TCollection_AsciiString

display, start_display, add_menu, add_function_to_menu = init_display()
my_box = BRepPrimAPI_MakeSphere(20.).Shape()

# render the sphere with default shading attributes ( no GLSL shader attached! )
anIO = display.DisplayShape(my_box, update=True)

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
phong_fs = TCollection_AsciiString(_phong_fs)
phong_vs = TCollection_AsciiString(_phong_vs)

# construct the shader, load, compile and attach the GLSL programs
aProgram = Graphic3d_ShaderProgram()
aProgram.AttachShader(Graphic3d_ShaderObject.CreateFromFile(Graphic3d_TOS_FRAGMENT, phong_fs ) )
aProgram.AttachShader(Graphic3d_ShaderObject.CreateFromFile(Graphic3d_TOS_VERTEX, phong_vs ) )

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

vs = TCollection_AsciiString("/Users/jelleferinga/miniconda/envs/_test/share/oce-0.18-dev/src/Shaders/PhongShading.vs")
# eee = Graphic3d_ShaderObject_CreateFromSource(Graphic3d_TOS_VERTEX, vs)

from PyQt5.QtCore import pyqtRemoveInputHook
pyqtRemoveInputHook()
import ipdb; ipdb.set_trace()


aspect.SetShaderProgram(aProgram)

# aProgram.AttachShader(eee)

# update the rendering attributes such that the sphere is rendered with the GLSL shader
display.Context.Redisplay(anIO)
# type(aspect.ShaderProgram())
# Out[76]: SwigPyObject



# start the GUI event loop
start_display()

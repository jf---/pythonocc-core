#!/usr/bin/env python

##Copyright 2009-2015 Jelle Feringa (jelleferinga@gmail.com)
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

from __future__ import print_function

from OCC.BRepPrimAPI import BRepPrimAPI_MakeSphere
from OCC.Display.SimpleGui import init_display

display, start_display, add_menu, add_function_to_menu = init_display()

ais_boxshp = None


def build_shape():
    boxshp = BRepPrimAPI_MakeSphere(50.0).Shape()
    ais_boxshp = display.DisplayShape(boxshp, update=True)
    return ais_boxshp


build_shape()

from OCC.Graphic3d import *

params = display.View.RenderingParams()

render_params = Graphic3d_RenderingParams()

display.View.ChangeRenderingParams(render_params)

start_display()

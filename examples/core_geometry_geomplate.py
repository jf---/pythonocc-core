#!/usr/bin/env python

# TODO:
# * need examples where the tangency to constraining faces is respected

##Copyright 2009-2013 Jelle Ferina (jelleferinga@gmail.com)
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

import os
import sys
import time
import types

from OCC.BRep import BRep_Tool
from OCC.BRepAdaptor import BRepAdaptor_HCurve
from OCC.BRepFill import BRepFill_CurveConstraint
from OCC.Display.SimpleGui import init_display
from OCC.GeomAbs import GeomAbs_C0
from OCC.GeomLProp import GeomLProp_SLProps
from OCC.GeomLProp import GeomLProp_SurfaceTool
from OCC.GeomPlate import GeomPlate_BuildPlateSurface, GeomPlate_PointConstraint, \
    GeomPlate_MakeApprox
from OCC.ShapeAnalysis import ShapeAnalysis_Surface
from OCC.gp import gp_Pnt
from OCCUtils.Construct import make_closed_polygon, make_n_sided, \
    make_vertex, make_face, make_wire
from OCCUtils.Topology import WireExplorer, Topo

display, start_display, add_menu, add_function_to_menu = init_display()

try:
    from scipy import arange
    from scipy.optimize import fsolve
except ImportError:
    print 'scipy not installed, will not be able to run the geomplate example'


def iges_importer(path_):
    from OCC.IGESControl import IGESControl_Reader
    from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
    iges_reader = IGESControl_Reader()
    status = iges_reader.ReadFile(path_)

    if status == IFSelect_RetDone:  # check status
        failsonly = False
        iges_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
        iges_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)
        ok = iges_reader.TransferRoots()
        aResShape = iges_reader.Shape(1)
        return  aResShape
    else:
        raise AssertionError("could not import IGES file: {0}".format(path_))


def geom_plate(event=None):
    display.EraseAll()
    p1 = gp_Pnt(0, 0, 0)
    p2 = gp_Pnt(0, 10, 0)
    p3 = gp_Pnt(0, 10, 10)
    p4 = gp_Pnt(0, 0, 10)
    p5 = gp_Pnt(5, 5, 5)
    poly = make_closed_polygon([p1, p2, p3, p4])
    edges = [i for i in Topo(poly).edges()]
    face = make_n_sided(edges, [p5])
    display.DisplayShape(edges)
    display.DisplayShape(make_vertex(p5))
    display.DisplayShape(face, update=True)


# ============================================================================
# Find a surface such that the radius at the vertex is n
# ============================================================================


def build_plate(polygon, points):
    '''
    build a surface from a constraining polygon(s) and point(s)
    @param polygon:     list of polygons ( TopoDS_Shape)
    @param points:      list of points ( gp_Pnt )
    '''
    # plate surface
    bpSrf = GeomPlate_BuildPlateSurface(3, 15, 2)

    # add curve constraints
    for poly in polygon:
        for edg in WireExplorer(poly).ordered_edges():
            c = BRepAdaptor_HCurve()
            c.ChangeCurve().Initialize(edg)
            constraint = BRepFill_CurveConstraint(c.GetHandle(), 0)
            bpSrf.Add(constraint.GetHandle())

    # add point constraint
    for pt in points:
        bpSrf.Add(GeomPlate_PointConstraint(pt, 0).GetHandle())
        bpSrf.Perform()

    maxSeg, maxDeg, critOrder = 9, 8, 0
    tol = 1e-4
    dmax = max([tol, 10 * bpSrf.G0Error()])

    srf = bpSrf.Surface()
    plate = GeomPlate_MakeApprox(srf, tol, maxSeg, maxDeg, dmax, critOrder)
    uMin, uMax, vMin, vMax = srf.GetObject().Bounds()

    return make_face(plate.Surface(), uMin, uMax, vMin, vMax, 1e-4)


def radius_at_uv(face, u, v):
    '''
    returns the mean radius at a u,v coordinate
    @param face:    surface input
    @param u,v:     u,v coordinate
    '''
    h_srf = BRep_Tool().Surface(face)
    uv_domain = GeomLProp_SurfaceTool().Bounds(h_srf)
    curvature = GeomLProp_SLProps(h_srf, u, v, 1, 1e-6)
    try:
        _crv_min = 1. / curvature.MinCurvature()
    except ZeroDivisionError:
        _crv_min = 0.

    try:
        _crv_max = 1. / curvature.MaxCurvature()
    except ZeroDivisionError:
        _crv_max = 0.
    return abs((_crv_min + _crv_max) / 2.)


def uv_from_projected_point_on_face(face, pt):
    '''
    returns the uv coordinate from a projected point on a face
    '''
    srf = BRep_Tool().Surface(face)
    sas = ShapeAnalysis_Surface(srf)
    uv = sas.ValueOfUV(pt, 1e-2)
    print 'distance', sas.Value(uv).Distance(pt)
    return uv.Coord()


class RadiusConstrainedSurface():
    '''
    returns a surface that has `radius` at `pt`
    '''

    def __init__(self, display, poly, pnt, targetRadius):
        self.display = display
        self.targetRadius = targetRadius
        self.poly = poly
        self.pnt = pnt
        self.plate = self.build_surface()

    def build_surface(self):
        '''
        builds and renders the plate
        '''
        self.plate = build_plate([self.poly], [self.pnt])
        self.display.EraseAll()
        self.display.DisplayShape(self.plate)
        vert = make_vertex(self.pnt)
        self.display.DisplayShape(vert, update=True)

    def radius(self, z):
        '''
        sets the height of the point constraining the plate, returns
        the radius at this point
        '''
        if isinstance(z, types.FloatType):
            self.pnt.SetX(z)
        else:
            self.pnt.SetX(float(z[0]))
        self.build_surface()
        uv = uv_from_projected_point_on_face(self.plate, self.pnt)
        radius = radius_at_uv(self.plate, uv[0], uv[1])
        print 'z:', z, 'radius:', radius
        self.curr_radius = radius
        return self.targetRadius - abs(radius)

    def solve(self):
        fsolve(self.radius, 1, maxfev=1000)
        return self.plate


def solve_radius(event=None):
    display.EraseAll()
    p1 = gp_Pnt(0, 0, 0)
    p2 = gp_Pnt(0, 10, 0)
    p3 = gp_Pnt(0, 10, 10)
    p4 = gp_Pnt(0, 0, 10)
    p5 = gp_Pnt(5, 5, 5)
    poly = make_closed_polygon([p1, p2, p3, p4])
    for i in arange(0.1, 3., 0.2).tolist():
        rcs = RadiusConstrainedSurface(display, poly, p5, i)
        face = rcs.solve()
        print 'Goal: %s radius: %s' % (i, rcs.curr_radius)
        time.sleep(0.5)


def build_geom_plate(edges):
    bpSrf = GeomPlate_BuildPlateSurface(3, 9, 12)

    # add curve constraints
    for edg in edges:
        c = BRepAdaptor_HCurve()
        print 'edge:', edg
        c.ChangeCurve().Initialize(edg)
        constraint = BRepFill_CurveConstraint(c.GetHandle(), 0)
        bpSrf.Add(constraint.GetHandle())

    # add point constraint
    try:
        bpSrf.Perform()
    except RuntimeError:
        print 'failed to build the geom plate surface '

    maxSeg, maxDeg, critOrder = 9, 8, 0
    tol = 1e-4
    dmax = max([tol, 10 * bpSrf.G0Error()])

    srf = bpSrf.Surface()
    # segfaults here...
    # plate = GeomPlate_MakeApprox(srf, 1e-04, 100, 9, 1e-03, 0)
    plate = GeomPlate_MakeApprox(srf, 0.01, 10, 5, 0.01, 0, GeomAbs_C0)
    # plate = GeomPlate_MakeApprox(srf)

    uMin, uMax, vMin, vMax = srf.GetObject().Bounds()
    face = make_face(plate.Surface(), uMin, uMax, vMin, vMax, 1e-6)
    return face


def build_curve_network(event=None):
    '''
    mimic the curve network surfacing command from rhino
    '''
    print 'Importing IGES file...',
    pth = os.path.dirname(os.path.abspath(__file__))
    pth = os.path.abspath(
            os.path.join(pth, 'models', 'curve_geom_plate.igs'))
    iges = iges_importer(pth)
    print 'done.'

    print 'Building geomplate...',
    topo = Topo(iges)
    edges_list = list(topo.edges())
    face = build_geom_plate(edges_list)
    print 'done.'
    display.EraseAll()
    display.DisplayShape(edges_list)
    display.DisplayShape(face)
    display.FitAll()
    print 'Cutting out of edges...',
    # Make a wire from outer edges
    _edges = [edges_list[2], edges_list[3], edges_list[4], edges_list[5]]
    outer_wire = make_wire(_edges)


def exit(event=None):
    sys.exit()


if __name__ == "__main__":
    add_menu('geom plate')
    add_function_to_menu('geom plate', geom_plate)
    add_function_to_menu('geom plate', solve_radius)
    add_function_to_menu('geom plate', build_curve_network)
    add_function_to_menu('geom plate', exit)

    build_curve_network()
    start_display()

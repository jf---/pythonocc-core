import math
from OCC.Display.SimpleGui import init_display
from OCC.gp import gp_QuaternionSLerp, gp_Lin, gp, gp_Lin2d, gp_Quaternion, gp_Vec, gp_Pnt, gp_Pln
from OCCUtils.Construct import make_edge, make_box

display, start_display, add_menu, add_function_to_menu = init_display()


def rotate(event=None):
    display.EraseAll()
    origin = gp_Vec(0,0,0)
    origin_pt = origin.as_pnt()

    vX = gp_Vec(12,0,0)
    vY = gp_Vec(0,12,0)
    vZ = gp_Vec(0,0,12)
    v45 = (gp_Vec(1,1,1).Normalized()*12)
    q1  = gp_Quaternion(vX,vY)

    p1 = (origin + vX).as_pnt()
    p2 = (origin + vY).as_pnt()
    p3 = (origin + (q1 * vY)).as_pnt()
    p4 = (origin + (q1 * v45)).as_pnt()

    # RED
    e1  = make_edge(origin_pt, p1)
    e2  = make_edge(origin_pt, p2)
    e3  = make_edge(origin_pt, v45.as_pnt())
    # GREEN -> transformed
    e4  = make_edge(origin_pt, p3)
    e5  = make_edge(origin_pt, p4)


    display.DisplayShape([e1,e2,e3])
    display.DisplayColoredShape([e4,e5], 'GREEN')
    display.DisplayMessage(p1, 'e1')
    display.DisplayMessage(p2, 'e2')
    display.DisplayMessage(v45.as_pnt(), 'e3')
    display.DisplayMessage(p3, 'q1*vY')
    display.DisplayMessage(p4, 'q1*v45')
    display.DisplayVector((q1 * vY).Normalized(), (origin + q1*vY/2.).as_pnt())
    display.DisplayVector((q1 * v45).Normalized(), (origin + q1*v45/2.).as_pnt())


def interpolate(event=None):
    display.EraseAll()

    origin = gp_Vec()
    vX = gp_Vec(12,0,0)
    vY = gp_Vec(0,12,0)
    v45 = (gp_Vec(1,1,1).Normalized()*12)

    interp = gp_QuaternionSLerp(gp_Quaternion(vX,vX), gp_Quaternion(vX,vY))
    for i in range(10):
        q = gp_Quaternion()
        interp.Interpolate(i/10., q)
        # displace the white edges a little from the origin so not to obstruct the other edges
        v = gp_Vec(0,-24,0)
        p = (q * v45 + v).as_pnt()
        e = make_edge((origin + v).as_pnt(), p)
        display.DisplayColoredShape(e, 'WHITE')
        display.DisplayMessage(p, 'v45->q1*v45 @{0}'.format(i/10.))


a=gp_Quaternion(gp_Vec(1,0,0), math.radians(45))
b=gp_Quaternion(gp_Vec(0,1,0), math.radians(45))
c=gp_Quaternion(gp_Vec(0,0,1), math.radians(45))

a=gp_Quaternion(gp_Vec(1,0,0), gp_Vec(1,1,0))
a1 = gp_Quaternion(gp_Vec(0,0,1), math.radians(45))
a.IsEqual(a1)
b1 = gp_Quaternion(gp_Vec(1,0,0), math.radians(-45))

print a1 * a1.Dot(b1)

edge1 = make_edge(gp_Pnt(), (a1 * gp_Vec(1, 0, 0)).as_pnt())
edge2 = make_edge(gp_Pnt(), (b1 * gp_Vec(1, 0, 0)).as_pnt())
edge4 = make_edge(gp_Pnt(), ((a1 + b1) * gp_Vec(1, 0, 0)).as_pnt())
edge3 = make_edge(gp_Pnt(), gp_Pnt(0,0,1))
#d.display.DisplayShape(edge1)
#d.display.DisplayColoredShape(edge2, 'GREEN')
#d.display.DisplayColoredShape(edge3, 'WHITE')
#d.display.DisplayColoredShape(edge4, 'BLUE')
display.DisplayShape(make_box(gp_Pnt(), gp_Pnt(1,1,1)))


(a1+b1).Normalized()
(a1*b1).Normalized()

neutral_vec = gp_Vec(0, 0, 1)
tool_vec    = gp_Vec(1/3., 1/3., 1/3.)
orientation = gp_Quaternion(neutral_vec, tool_vec)

vec_ = (orientation * gp_Vec(0, 0, 1)).as_pnt()
li_quat = gp_Lin( gp_Pnt(), vec_.as_vec().as_dir() )

display.DisplayColoredShape(make_edge(li_quat, 0, 2), 'CYAN')

from OCC.ProjLib import ProjLib_Plane

xy = gp_Pln(gp_Pnt(), gp.DZ())
xz = gp_Pln(gp_Pnt(), gp.DY())
yz = gp_Pln(gp_Pnt(), gp.DX())
proj_pln = ProjLib_Plane(xy)
proj_xy1 = ProjLib_Plane(xy, li_quat).Line()
proj_xy1.Angle(gp_Lin2d())
proj_xy2 = ProjLib_Plane()

#proj_xy2.Init(xy)
#ProjLib_Plane(xy).Project(gp_Hypr())
#proj_xy1 = ProjLib_Plane(xy, li_quat)


#p = ProjLib.Project(xy, li_quat)
#p = ProjLib().Project(gp_Torus(), gp_Pnt())
#ProjLib.Project(xy, li_quat)
#
#proj = ProjLib_Projector()

from OCC.GeomProjLib import geomprojlib_ProjectOnPlane, geomprojlib
from OCC.Geom import Geom_Line, Geom_Plane


pln = Geom_Plane(gp_Pnt(), gp.DZ())
li = Geom_Line(gp_Pnt(), vec_.as_vec().as_dir())

proj = geomprojlib()
li_proj = proj.ProjectOnPlane(li.GetHandle(), pln.GetHandle(), gp.DZ(), True).GetObject()

# KABOOM
li_proj.Value(0)
li_proj.Value(10)

from OCC.GeomAPI import geomapi_To2d, geomapi_To3d

def project_geom_curve_to_plane(curve, pln):
    crv2d = geomapi_To2d(curve.GetHandle(),pln)
    return geomapi_To3d(crv2d, pln)

edg1 = (make_edge(project_geom_curve_to_plane(li, xy), 0,2))
edg2 = (make_edge(project_geom_curve_to_plane(li, xz), 0,2))
edg3 = (make_edge(project_geom_curve_to_plane(li, yz), 0,2))
display.DisplayColoredShape(edg1, 'BLACK')
display.DisplayColoredShape(edg2, 'YELLOW')
display.DisplayColoredShape(edg3, 'ORANGE')

# http://www.opencascade.org/org/forum/thread_10862/
# project vector on plane
# gp_Vec vec; // your vector
# gp_Pln pln; // your plane
# gp_Vec normal = plane.Direction().XYZ();
# #gp_Vec normal = pln.Axis().Direction().XYZ();
# gp_Vec prj = normal ^ vec ^ normal;



#orientA = gp_Quaternion(gp_Vec(1,0,0), math.radians(-90.))
#orientB = gp_Quaternion(gp_Vec(0,1,0), math.radians(90.))
#orientC = (orientA+orientB).Normalized()
#
#orientD = gp_Quaternion(gp_Vec(1,0,0), gp_Vec(1/3.,1/3.,1/3.))
#print orientD * gp_Vec(0,0,1)

# d.add_menu('quaternion')
# d.add_function_to_menu('quaternion', rotate)
# d.add_function_to_menu('quaternion', interpolate)

interpolate(None)

start_display()
from OCC import gp
from OCC.AIS import AIS_Line, AIS_Trihedron, AIS_Shaded
from OCC.Display.SimpleGui import init_display
from OCC.Display.backend import get_qt_modules
from OCC.Geom import Geom_CartesianPoint, Geom_Axis2Placement
from OCCUtils.Construct import make_box
from PyQt5.QtCore import QObject

display, start_display, add_menu, add_function_to_menu = init_display()
QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()
# from OCC.Display.qtDisplay import qtViewer3d

pO = Geom_CartesianPoint(0, 0, 0)
pX = Geom_CartesianPoint(1000, 0, 0)
pY = Geom_CartesianPoint(0, 1000, 0)
pZ = Geom_CartesianPoint(0, 0, 1000)

li_x = AIS_Line(pO.GetHandle(), pX.GetHandle())
li_y = AIS_Line(pO.GetHandle(), pY.GetHandle())
li_z = AIS_Line(pO.GetHandle(), pZ.GetHandle())


class TriWithSelectionEvents(AIS_Trihedron):
    def __init__(self, axe, display):
        pass


axe = Geom_Axis2Placement(gp.gp_Pnt(2000, 0, 0), gp.gp.DY(), gp.gp.DZ())

tri = AIS_Trihedron(axe.GetHandle())
tri.SetDisplayMode(AIS_Shaded)
# tri.SetSize(100)
tri.SetSelectionMode(2)

tri.SetWidth(5)

box = make_box(50, 50, 100)
display.DisplayShape(box)

aDrawer = tri.Attributes().GetObject()
aDrawer.DatumAspect()

display.Context.Display(li_x.GetHandle())
display.Context.Display(li_y.GetHandle())
display.Context.Display(li_z.GetHandle())
display.Context.Display(tri.GetHandle())


def omg():
    print("OMG!!!")


app = QtWidgets.QApplication.instance()
v = app.findChild(QObject, "qtViewer3d")

# display.sig_interactive_selected.connect(omg)

start_display()


# -------------------------------------------------------------------------------
# TODO:
# register slot onMouseClicked event / select
# register shape to be moved
# AIS_Context.IsSelected ( loop through components of tri )
# move in direction of the axis
#
# Better graphics
# create something inherited from AIS_InteractiveObject
# override Pr3d_Presentation for graphics
# see this:
# http://www.opencascade.com/doc/occt-6.7.0/overview/html/user_guides__visualization.html
# -------------------------------------------------------------------------------

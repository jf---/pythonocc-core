import sys

from OCC.BRepGProp import brepgprop_LinearProperties
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
from OCC.Display.backend import get_qt_modules
from OCC.GProp import GProp_GProps
from OCC.TopAbs import TopAbs_SOLID, TopAbs_EDGE, TopAbs_FACE

display, start_display, add_menu, add_function_to_menu = init_display("qt-pyqt4")
QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()

from OCC.Display.qtDisplay import qtViewer3d

print "Usage: press G to find the linear properties for volume, face, edge, vertex..."


def get_occ_viewer():
    """

    Returns
    -------

    qtViewer3d

    """
    app = QtWidgets.QApplication.instance()  # checks if QApplication already exists
    if not app:
        app = QtWidgets.QApplication(sys.argv)
    widgets = app.topLevelWidgets()
    for wi in widgets:
        if hasattr(wi, "_menus"):  # OCC.Display.SimpleGui.MainWindow
            viewer = wi.findChild(qtViewer3d, "qt_viewer_3d")
            return viewer


def on_select(shape):
    """

    Parameters
    ----------
    shape : TopoDS_Shape

    """
    g1 = GProp_GProps()
    brepgprop_LinearProperties(shape, g1)
    mass = g1.Mass()
    centre_of_mass = g1.CentreOfMass()
    com_x = centre_of_mass.X()
    com_y = centre_of_mass.Y()
    com_z = centre_of_mass.Z()
    static_moments = g1.StaticMoments()
    print "shape {shape}: \n mass: {mass}" \
          "\n center of mass: {com_x}, {com_y}, {com_z}" \
          "\n static moments: {static_moments}".format(**vars())

def also_on_select(shape):
    if shape.ShapeType() == TopAbs_SOLID:
        print "solid selected"
    if shape.ShapeType() == TopAbs_EDGE:
        print "edge selected"
    if shape.ShapeType() == TopAbs_FACE:
        print "fae selected"

cube = BRepPrimAPI_MakeBox(100, 100, 100).Shape()
display.DisplayShape(cube)

viewer = get_occ_viewer()
viewer.sig_topods_selected.connect(on_select)
viewer.sig_topods_selected.connect(also_on_select)

display.FitAll()
start_display()

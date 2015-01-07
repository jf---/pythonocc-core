import os
from OCC.Display.SimpleGui import init_display
from OCC.DataExchange.utils import file_to_shape
from OCC.Utils.Topology import Topo
from OCC.Utils.Construct import geodesic_path
display, start_display, add_menu, add_function_to_menu = init_display()

directory = os.path.abspath(os.path.split(__name__)[0])
pth = os.path.join(directory, "models", "curve_geom_plate.igs")
shape = file_to_shape(pth)
tp = Topo(shape, True)

display.DisplayShape(shape)

e = tp.edges().next()
uva, pnta = e.project_vertex(e.first_vertex())
edges = [i for i in tp.edges()]
for edg in edges[1:-1]:
    n = 0
    for uvb, pntb in edg.divide_by_number_of_points(36)[1:-1]:
        print 'n', n
        if pnta == pntb or edg == e:
            continue
        fc = tp.faces().next()
        geodesic_edg = geodesic_path(pnta, pntb, e, edg, fc, 12, 0.1, 120)
        geodesic_edg.show()
        n += 1




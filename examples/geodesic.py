
from core_geometry_utils import make_edge, points_to_bspline


def smooth_pnts(pnts):
    smooth = [pnts[0]]
    for i in range(1, len(pnts)-1):
        prev = pnts[i-1]
        this = pnts[i]
        next = pnts[i+1]
        pt = (prev+this+next) / 3.0
        smooth.append(pt)
    smooth.append(pnts[-1])
    return smooth


def geodesic_path(pntA, pntB, edgA, edgB, kbe_face, n_segments=20, _tolerance=0.1, n_iter=20):
    """
    :param pntA:        point to start from
    :param pntB:        point to move towards
    :param edgA:        edge to start from
    :param edgB:        edge to move towards
    :param kbe_face:    kbe.face.Face on which `edgA` and `edgB` lie
    :param n_segments:  the number of segments the geodesic is built from
    :param _tolerance:  tolerance when the geodesic is converged
    :param n_iter:      maximum number of iterations
    :return:            TopoDS_Edge
    """
    uvA, srf_pnt_A = kbe_face.project_vertex(pntA)
    uvB, srf_pnt_B = kbe_face.project_vertex(pntB)

    path = []
    for i in range(n_segments):
        t = i / float(n_segments)
        u = uvA[0] + t*(uvB[0] - uvA[0])
        v = uvA[1] + t*(uvB[1] - uvA[1])
        path.append(kbe_face.parameter_to_point(u,v))

    project_pnts = lambda x: [kbe_face.project_vertex(i)[1] for i in x]
    poly_length = lambda x: sum([x[i].Distance(x[i+1]) for i in range(len(x)-1)]) / len(x)

    length = poly_length(path)

    n = 0
    while True:
        path = smooth_pnts(path)
        path = project_pnts(path)
        newlength = poly_length(path)
        if abs(newlength-length) < _tolerance or n == n_iter:
            crv = points_to_bspline(path)
            return make_edge(crv)
        n+=1




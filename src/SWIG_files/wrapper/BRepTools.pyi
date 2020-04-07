from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.Bnd import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.TopTools import *
from OCC.Core.BRep import *
from OCC.Core.Message import *
from OCC.Core.GeomAbs import *
from OCC.Core.TopLoc import *
from OCC.Core.gp import *
from OCC.Core.Poly import *
from OCC.Core.TopAbs import *


class BRepTools:
	@staticmethod
	def AddUVBounds(self, F: TopoDS_Face, B: Bnd_Box2d) -> None: ...
	@staticmethod
	def AddUVBounds(self, F: TopoDS_Face, W: TopoDS_Wire, B: Bnd_Box2d) -> None: ...
	@staticmethod
	def AddUVBounds(self, F: TopoDS_Face, E: TopoDS_Edge, B: Bnd_Box2d) -> None: ...
	@staticmethod
	def Clean(self, S: TopoDS_Shape) -> None: ...
	@staticmethod
	def CleanGeometry(self, theShape: TopoDS_Shape) -> None: ...
	@staticmethod
	def Compare(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> bool: ...
	@staticmethod
	def Compare(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> bool: ...
	@staticmethod
	def DetectClosedness(self, theFace: TopoDS_Face) -> Tuple[bool, bool]: ...
	@staticmethod
	def EvalAndUpdateTol(self, theE: TopoDS_Edge, theC3d: Geom_Curve, theC2d: Geom2d_Curve, theS: Geom_Surface, theF: float, theL: float) -> float: ...
	@staticmethod
	def IsReallyClosed(self, E: TopoDS_Edge, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def Map3DEdges(self, S: TopoDS_Shape, M: TopTools_IndexedMapOfShape) -> None: ...
	@staticmethod
	def OuterWire(self, F: TopoDS_Face) -> TopoDS_Wire: ...
	@staticmethod
	def Read(self, Sh: TopoDS_Shape, File: str, B: BRep_Builder, PR: Optional[Message_ProgressIndicator]) -> bool: ...
	@staticmethod
	def RemoveUnusedPCurves(self, S: TopoDS_Shape) -> None: ...
	@staticmethod
	def Triangulation(self, S: TopoDS_Shape, deflec: float) -> bool: ...
	@staticmethod
	def UVBounds(self, F: TopoDS_Face) -> Tuple[float, float, float, float]: ...
	@staticmethod
	def UVBounds(self, F: TopoDS_Face, W: TopoDS_Wire) -> Tuple[float, float, float, float]: ...
	@staticmethod
	def UVBounds(self, F: TopoDS_Face, E: TopoDS_Edge) -> Tuple[float, float, float, float]: ...
	@staticmethod
	def Update(self, V: TopoDS_Vertex) -> None: ...
	@staticmethod
	def Update(self, E: TopoDS_Edge) -> None: ...
	@staticmethod
	def Update(self, W: TopoDS_Wire) -> None: ...
	@staticmethod
	def Update(self, F: TopoDS_Face) -> None: ...
	@staticmethod
	def Update(self, S: TopoDS_Shell) -> None: ...
	@staticmethod
	def Update(self, S: TopoDS_Solid) -> None: ...
	@staticmethod
	def Update(self, C: TopoDS_CompSolid) -> None: ...
	@staticmethod
	def Update(self, C: TopoDS_Compound) -> None: ...
	@staticmethod
	def Update(self, S: TopoDS_Shape) -> None: ...
	@staticmethod
	def UpdateFaceUVPoints(self, theF: TopoDS_Face) -> None: ...
	@staticmethod
	def Write(self, Sh: TopoDS_Shape, File: str, PR: Optional[Message_ProgressIndicator]) -> bool: ...

class BRepTools_History(Standard_Transient):
	def AddGenerated(self, theInitial: TopoDS_Shape, theGenerated: TopoDS_Shape) -> None: ...
	def AddModified(self, theInitial: TopoDS_Shape, theModified: TopoDS_Shape) -> None: ...
	def Clear(self) -> None: ...
	def Generated(self, theInitial: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def HasGenerated(self) -> bool: ...
	def HasModified(self) -> bool: ...
	def HasRemoved(self) -> bool: ...
	def IsRemoved(self, theInitial: TopoDS_Shape) -> bool: ...
	@staticmethod
	def IsSupportedType(self, theShape: TopoDS_Shape) -> bool: ...
	def Modified(self, theInitial: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Remove(self, theRemoved: TopoDS_Shape) -> None: ...
	def ReplaceGenerated(self, theInitial: TopoDS_Shape, theGenerated: TopoDS_Shape) -> None: ...
	def ReplaceModified(self, theInitial: TopoDS_Shape, theModified: TopoDS_Shape) -> None: ...

class BRepTools_Modification(Standard_Transient):
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewPolygon(self, E: TopoDS_Edge, P: Poly_Polygon3D) -> bool: ...
	def NewPolygonOnTriangulation(self, E: TopoDS_Edge, F: TopoDS_Face, P: Poly_PolygonOnTriangulation) -> bool: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...
	def NewTriangulation(self, F: TopoDS_Face, T: Poly_Triangulation) -> bool: ...

class BRepTools_Modifier:
	@overload
	def __init__(self, theMutableInput: Optional[bool]) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, M: BRepTools_Modification) -> None: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def IsMutableInput(self) -> bool: ...
	def ModifiedShape(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	def Perform(self, M: BRepTools_Modification, aProgress: Optional[Message_ProgressIndicator]) -> None: ...
	def SetMutableInput(self, theMutableInput: bool) -> None: ...

class BRepTools_Quilt:
	def __init__(self) -> None: ...
	def Add(self, S: TopoDS_Shape) -> None: ...
	def Bind(self, Eold: TopoDS_Edge, Enew: TopoDS_Edge) -> None: ...
	def Bind(self, Vold: TopoDS_Vertex, Vnew: TopoDS_Vertex) -> None: ...
	def Copy(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	def IsCopied(self, S: TopoDS_Shape) -> bool: ...
	def Shells(self) -> TopoDS_Shape: ...

class BRepTools_ReShape(Standard_Transient):
	def __init__(self) -> None: ...
	def Apply(self, shape: TopoDS_Shape, until: Optional[TopAbs_ShapeEnum]) -> TopoDS_Shape: ...
	def Clear(self) -> None: ...
	def CopyVertex(self, theV: TopoDS_Vertex, theTol: Optional[float]) -> TopoDS_Vertex: ...
	def CopyVertex(self, theV: TopoDS_Vertex, theNewPos: gp_Pnt, aTol: float) -> TopoDS_Vertex: ...
	def History(self) -> BRepTools_History: ...
	def IsNewShape(self, theShape: TopoDS_Shape) -> bool: ...
	def IsRecorded(self, shape: TopoDS_Shape) -> bool: ...
	def ModeConsiderLocation(self) -> bool: ...
	def Remove(self, shape: TopoDS_Shape) -> None: ...
	def Replace(self, shape: TopoDS_Shape, newshape: TopoDS_Shape) -> None: ...
	def Status(self, shape: TopoDS_Shape, newsh: TopoDS_Shape, last: Optional[bool]) -> int: ...
	def Value(self, shape: TopoDS_Shape) -> TopoDS_Shape: ...

class BRepTools_ShapeSet(TopTools_ShapeSet):
	@overload
	def __init__(self, isWithTriangles: Optional[bool]) -> None: ...
	@overload
	def __init__(self, B: BRep_Builder, isWithTriangles: Optional[bool]) -> None: ...
	def AddGeometry(self, S: TopoDS_Shape) -> None: ...
	def AddShapes(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...
	def Check(self, T: TopAbs_ShapeEnum, S: TopoDS_Shape) -> None: ...
	def Clear(self) -> None: ...

class BRepTools_Substitution:
	def __init__(self) -> None: ...
	def Build(self, S: TopoDS_Shape) -> None: ...
	def Clear(self) -> None: ...
	def Copy(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def IsCopied(self, S: TopoDS_Shape) -> bool: ...
	def Substitute(self, OldShape: TopoDS_Shape, NewShapes: TopTools_ListOfShape) -> None: ...

class BRepTools_WireExplorer:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, W: TopoDS_Wire) -> None: ...
	@overload
	def __init__(self, W: TopoDS_Wire, F: TopoDS_Face) -> None: ...
	def Clear(self) -> None: ...
	def Current(self) -> TopoDS_Edge: ...
	def CurrentVertex(self) -> TopoDS_Vertex: ...
	def Init(self, W: TopoDS_Wire) -> None: ...
	def Init(self, W: TopoDS_Wire, F: TopoDS_Face) -> None: ...
	def Init(self, W: TopoDS_Wire, F: TopoDS_Face, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Orientation(self) -> TopAbs_Orientation: ...

class BRepTools_GTrsfModification(BRepTools_Modification):
	def __init__(self, T: gp_GTrsf) -> None: ...
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def GTrsf(self) -> gp_GTrsf: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...

class BRepTools_NurbsConvertModification(BRepTools_Modification):
	def __init__(self) -> None: ...
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def GetUpdatedEdges(self) -> TopTools_ListOfShape: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...

class BRepTools_TrsfModification(BRepTools_Modification):
	def __init__(self, T: gp_Trsf) -> None: ...
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, NewE: TopoDS_Edge, NewF1: TopoDS_Face, NewF2: TopoDS_Face) -> GeomAbs_Shape: ...
	def NewCurve(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location) -> Tuple[bool, float]: ...
	def NewCurve2d(self, E: TopoDS_Edge, F: TopoDS_Face, NewE: TopoDS_Edge, NewF: TopoDS_Face, C: Geom2d_Curve) -> Tuple[bool, float]: ...
	def NewParameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
	def NewSurface(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location) -> Tuple[bool, float, bool, bool]: ...
	def Trsf(self) -> gp_Trsf: ...

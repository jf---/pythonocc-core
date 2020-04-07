from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *
from OCC.Core.TShort import *


class Poly:
	@staticmethod
	def Catenate(self, lstTri: Poly_ListOfTriangulation) -> Poly_Triangulation: ...
	@staticmethod
	def ComputeNormals(self, Tri: Poly_Triangulation) -> None: ...
	@staticmethod
	def PointOnTriangle(self, P1: gp_XY, P2: gp_XY, P3: gp_XY, P: gp_XY, UV: gp_XY) -> float: ...

class Poly_CoherentLink:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, iNode0: int, iNode1: int) -> None: ...
	@overload
	def __init__(self, theTri: Poly_CoherentTriangle, iSide: int) -> None: ...
	def GetAttribute(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	def Node(self, ind: int) -> int: ...
	def Nullify(self) -> None: ...
	def OppositeNode(self, ind: int) -> int: ...
	def SetAttribute(self, theAtt: None) -> None: ...

class Poly_CoherentNode(gp_XYZ):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, thePnt: gp_XYZ) -> None: ...
	def AddTriangle(self, theTri: Poly_CoherentTriangle, theA: NCollection_BaseAllocator) -> None: ...
	def GetIndex(self) -> int: ...
	def GetNormal(self) -> gp_XYZ: ...
	def GetU(self) -> float: ...
	def GetV(self) -> float: ...
	def HasNormal(self) -> bool: ...
	def IsFreeNode(self) -> bool: ...
	def RemoveTriangle(self, theTri: Poly_CoherentTriangle, theA: NCollection_BaseAllocator) -> bool: ...
	def SetIndex(self, theIndex: int) -> None: ...
	def SetNormal(self, theVector: gp_XYZ) -> None: ...
	def SetUV(self, theU: float, theV: float) -> None: ...
	def TriangleIterator(self) -> False: ...

class Poly_CoherentTriangle:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, iNode0: int, iNode1: int, iNode2: int) -> None: ...
	def GetConnectedNode(self, iConn: int) -> int: ...
	def GetConnectedTri(self, iConn: int) -> Poly_CoherentTriangle: ...
	def GetLink(self, iLink: int) -> Poly_CoherentLink: ...
	def IsEmpty(self) -> bool: ...
	def NConnections(self) -> int: ...
	def Node(self, ind: int) -> int: ...
	def RemoveConnection(self, iConn: int) -> None: ...
	def RemoveConnection(self, theTri: Poly_CoherentTriangle) -> bool: ...
	def SetConnection(self, iConn: int, theTr: Poly_CoherentTriangle) -> bool: ...
	def SetConnection(self, theTri: Poly_CoherentTriangle) -> bool: ...

class Poly_Connect:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theTriangulation: Poly_Triangulation) -> None: ...
	def Initialize(self, N: int) -> None: ...
	def Load(self, theTriangulation: Poly_Triangulation) -> None: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Nodes(self, T: int) -> Tuple[int, int, int]: ...
	def Triangle(self, N: int) -> int: ...
	def Triangles(self, T: int) -> Tuple[int, int, int]: ...
	def Triangulation(self) -> Poly_Triangulation: ...
	def Value(self) -> int: ...

class Poly_Polygon2D(Standard_Transient):
	def __init__(self, Nodes: TColgp_Array1OfPnt2d) -> None: ...
	def Deflection(self) -> float: ...
	def Deflection(self, D: float) -> None: ...
	def NbNodes(self) -> int: ...
	def Nodes(self) -> TColgp_Array1OfPnt2d: ...

class Poly_Polygon3D(Standard_Transient):
	@overload
	def __init__(self, Nodes: TColgp_Array1OfPnt) -> None: ...
	@overload
	def __init__(self, Nodes: TColgp_Array1OfPnt, Parameters: TColStd_Array1OfReal) -> None: ...
	def ChangeParameters(self) -> TColStd_Array1OfReal: ...
	def Copy(self) -> Poly_Polygon3D: ...
	def Deflection(self) -> float: ...
	def Deflection(self, D: float) -> None: ...
	def HasParameters(self) -> bool: ...
	def NbNodes(self) -> int: ...
	def Nodes(self) -> TColgp_Array1OfPnt: ...
	def Parameters(self) -> TColStd_Array1OfReal: ...

class Poly_PolygonOnTriangulation(Standard_Transient):
	@overload
	def __init__(self, Nodes: TColStd_Array1OfInteger) -> None: ...
	@overload
	def __init__(self, Nodes: TColStd_Array1OfInteger, Parameters: TColStd_Array1OfReal) -> None: ...
	def Copy(self) -> Poly_PolygonOnTriangulation: ...
	def Deflection(self) -> float: ...
	def Deflection(self, D: float) -> None: ...
	def HasParameters(self) -> bool: ...
	def NbNodes(self) -> int: ...
	def Nodes(self) -> TColStd_Array1OfInteger: ...
	def Parameters(self) -> TColStd_HArray1OfReal: ...

class Poly_Triangle:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, N1: int, N2: int, N3: int) -> None: ...
	def GetChangeValue(self, Index: int) -> int: ...
	def SetChangeValue(self, Index: int, value: int) -> None: ...
	def Get(self) -> Tuple[int, int, int]: ...
	def Set(self, N1: int, N2: int, N3: int) -> None: ...
	def Set(self, Index: int, Node: int) -> None: ...
	def Value(self, Index: int) -> int: ...

class Poly_Triangulation(Standard_Transient):
	@overload
	def __init__(self, nbNodes: int, nbTriangles: int, UVNodes: bool) -> None: ...
	@overload
	def __init__(self, Nodes: TColgp_Array1OfPnt, Triangles: Poly_Array1OfTriangle) -> None: ...
	@overload
	def __init__(self, Nodes: TColgp_Array1OfPnt, UVNodes: TColgp_Array1OfPnt2d, Triangles: Poly_Array1OfTriangle) -> None: ...
	@overload
	def __init__(self, theTriangulation: Poly_Triangulation) -> None: ...
	def ChangeNode(self, theIndex: int) -> gp_Pnt: ...
	def ChangeNodes(self) -> TColgp_Array1OfPnt: ...
	def ChangeNormals(self) -> TShort_Array1OfShortReal: ...
	def ChangeTriangle(self, theIndex: int) -> Poly_Triangle: ...
	def ChangeTriangles(self) -> Poly_Array1OfTriangle: ...
	def ChangeUVNode(self, theIndex: int) -> gp_Pnt2d: ...
	def ChangeUVNodes(self) -> TColgp_Array1OfPnt2d: ...
	def Copy(self) -> Poly_Triangulation: ...
	def Deflection(self) -> float: ...
	def Deflection(self, theDeflection: float) -> None: ...
	def HasNormals(self) -> bool: ...
	def HasUVNodes(self) -> bool: ...
	def NbNodes(self) -> int: ...
	def NbTriangles(self) -> int: ...
	def Node(self, theIndex: int) -> gp_Pnt: ...
	def Nodes(self) -> TColgp_Array1OfPnt: ...
	def Normal(self, theIndex: int) -> gp_Dir: ...
	def Normals(self) -> TShort_Array1OfShortReal: ...
	def RemoveUVNodes(self) -> None: ...
	def SetNormal(self, theIndex: int, theNormal: gp_Dir) -> None: ...
	def SetNormals(self, theNormals: TShort_HArray1OfShortReal) -> None: ...
	def Triangle(self, theIndex: int) -> Poly_Triangle: ...
	def Triangles(self) -> Poly_Array1OfTriangle: ...
	def UVNode(self, theIndex: int) -> gp_Pnt2d: ...
	def UVNodes(self) -> TColgp_Array1OfPnt2d: ...

#classnotwrapped
class Poly_CoherentTriPtr:
	pass

#classnotwrapped
class Poly_CoherentTriangulation:
	pass

#classnotwrapped
class Poly_MakeLoops:
	pass

#classnotwrapped
class Poly_MakeLoops3D:
	pass

#classnotwrapped
class Poly_MakeLoops2D:
	pass

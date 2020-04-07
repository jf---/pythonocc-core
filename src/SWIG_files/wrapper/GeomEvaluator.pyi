from typing import overload, NewType, Optional, Tuple

from OCC.Core.GeomEvaluator import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.Geom import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.Adaptor3d import *


class GeomEvaluator_Curve(Standard_Transient):
	def D0(self, theU: float, theValue: gp_Pnt) -> None: ...
	def D1(self, theU: float, theValue: gp_Pnt, theD1: gp_Vec) -> None: ...
	def D2(self, theU: float, theValue: gp_Pnt, theD1: gp_Vec, theD2: gp_Vec) -> None: ...
	def D3(self, theU: float, theValue: gp_Pnt, theD1: gp_Vec, theD2: gp_Vec, theD3: gp_Vec) -> None: ...
	def DN(self, theU: float, theDerU: int) -> gp_Vec: ...

class GeomEvaluator_Surface(Standard_Transient):
	def D0(self, theU: float, theV: float, theValue: gp_Pnt) -> None: ...
	def D1(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec) -> None: ...
	def D2(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec) -> None: ...
	def D3(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec, theD3U: gp_Vec, theD3V: gp_Vec, theD3UUV: gp_Vec, theD3UVV: gp_Vec) -> None: ...
	def DN(self, theU: float, theV: float, theDerU: int, theDerV: int) -> gp_Vec: ...

class GeomEvaluator_OffsetCurve(GeomEvaluator_Curve):
	@overload
	def __init__(self, theBase: Geom_Curve, theOffset: float, theDirection: gp_Dir) -> None: ...
	@overload
	def __init__(self, theBase: GeomAdaptor_HCurve, theOffset: float, theDirection: gp_Dir) -> None: ...
	def D0(self, theU: float, theValue: gp_Pnt) -> None: ...
	def D1(self, theU: float, theValue: gp_Pnt, theD1: gp_Vec) -> None: ...
	def D2(self, theU: float, theValue: gp_Pnt, theD1: gp_Vec, theD2: gp_Vec) -> None: ...
	def D3(self, theU: float, theValue: gp_Pnt, theD1: gp_Vec, theD2: gp_Vec, theD3: gp_Vec) -> None: ...
	def DN(self, theU: float, theDeriv: int) -> gp_Vec: ...
	def SetOffsetDirection(self, theDirection: gp_Dir) -> None: ...
	def SetOffsetValue(self, theOffset: float) -> None: ...

class GeomEvaluator_OffsetSurface(GeomEvaluator_Surface):
	@overload
	def __init__(self, theBase: Geom_Surface, theOffset: float, theOscSurf: Optional[Geom_OsculatingSurface]) -> None: ...
	@overload
	def __init__(self, theBase: GeomAdaptor_HSurface, theOffset: float, theOscSurf: Optional[Geom_OsculatingSurface]) -> None: ...
	def D0(self, theU: float, theV: float, theValue: gp_Pnt) -> None: ...
	def D1(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec) -> None: ...
	def D2(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec) -> None: ...
	def D3(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec, theD3U: gp_Vec, theD3V: gp_Vec, theD3UUV: gp_Vec, theD3UVV: gp_Vec) -> None: ...
	def DN(self, theU: float, theV: float, theDerU: int, theDerV: int) -> gp_Vec: ...
	def SetOffsetValue(self, theOffset: float) -> None: ...

class GeomEvaluator_SurfaceOfExtrusion(GeomEvaluator_Surface):
	@overload
	def __init__(self, theBase: Geom_Curve, theExtrusionDir: gp_Dir) -> None: ...
	@overload
	def __init__(self, theBase: Adaptor3d_HCurve, theExtrusionDir: gp_Dir) -> None: ...
	def D0(self, theU: float, theV: float, theValue: gp_Pnt) -> None: ...
	def D1(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec) -> None: ...
	def D2(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec) -> None: ...
	def D3(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec, theD3U: gp_Vec, theD3V: gp_Vec, theD3UUV: gp_Vec, theD3UVV: gp_Vec) -> None: ...
	def DN(self, theU: float, theV: float, theDerU: int, theDerV: int) -> gp_Vec: ...
	def SetDirection(self, theDirection: gp_Dir) -> None: ...

class GeomEvaluator_SurfaceOfRevolution(GeomEvaluator_Surface):
	@overload
	def __init__(self, theBase: Geom_Curve, theRevolDir: gp_Dir, theRevolLoc: gp_Pnt) -> None: ...
	@overload
	def __init__(self, theBase: Adaptor3d_HCurve, theRevolDir: gp_Dir, theRevolLoc: gp_Pnt) -> None: ...
	def D0(self, theU: float, theV: float, theValue: gp_Pnt) -> None: ...
	def D1(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec) -> None: ...
	def D2(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec) -> None: ...
	def D3(self, theU: float, theV: float, theValue: gp_Pnt, theD1U: gp_Vec, theD1V: gp_Vec, theD2U: gp_Vec, theD2V: gp_Vec, theD2UV: gp_Vec, theD3U: gp_Vec, theD3V: gp_Vec, theD3UUV: gp_Vec, theD3UVV: gp_Vec) -> None: ...
	def DN(self, theU: float, theV: float, theDerU: int, theDerV: int) -> gp_Vec: ...
	def SetAxis(self, theAxis: gp_Ax1) -> None: ...
	def SetDirection(self, theDirection: gp_Dir) -> None: ...
	def SetLocation(self, theLocation: gp_Pnt) -> None: ...
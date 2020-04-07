from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.LDOM import *
from OCC.Core.TCollection import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.Storage import *

XmlObjMgt_DOMString = NewType('XmlObjMgt_DOMString', LDOMString)
XmlObjMgt_Document = NewType('XmlObjMgt_Document', LDOM_Document)
XmlObjMgt_Element = NewType('XmlObjMgt_Element', LDOM_Element)

class XmlObjMgt:
	@staticmethod
	def FindChildByName(self, theSource: XmlObjMgt_Element, theName: XmlObjMgt_DOMString) -> XmlObjMgt_Element: ...
	@staticmethod
	def FindChildByRef(self, theSource: XmlObjMgt_Element, theRefName: XmlObjMgt_DOMString) -> XmlObjMgt_Element: ...
	@staticmethod
	def FindChildElement(self, theSource: XmlObjMgt_Element, theObjId: int) -> XmlObjMgt_Element: ...
	@staticmethod
	def GetExtendedString(self, theElement: XmlObjMgt_Element, theString: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def GetInteger(self, theString: str) -> Tuple[bool, int]: ...
	@staticmethod
	def GetReal(self, theString: str) -> Tuple[bool, float]: ...
	@staticmethod
	def GetReal(self, theString: XmlObjMgt_DOMString) -> Tuple[bool, float]: ...
	@staticmethod
	def GetStringValue(self, theElement: XmlObjMgt_Element) -> XmlObjMgt_DOMString: ...
	@staticmethod
	def GetTagEntryString(self, theTarget: XmlObjMgt_DOMString, theTagEntry: TCollection_AsciiString) -> bool: ...
	@staticmethod
	def IdString(self) -> XmlObjMgt_DOMString: ...
	@staticmethod
	def SetExtendedString(self, theElement: XmlObjMgt_Element, theString: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def SetStringValue(self, theElement: XmlObjMgt_Element, theData: XmlObjMgt_DOMString, isClearText: Optional[bool]) -> None: ...
	@staticmethod
	def SetTagEntryString(self, theSource: XmlObjMgt_DOMString, theTagEntry: TCollection_AsciiString) -> None: ...

class XmlObjMgt_Array1:
	@overload
	def __init__(self, Low: int, Up: int) -> None: ...
	@overload
	def __init__(self, theParent: XmlObjMgt_Element, theName: XmlObjMgt_DOMString) -> None: ...
	def CreateArrayElement(self, theParent: XmlObjMgt_Element, theName: XmlObjMgt_DOMString) -> None: ...
	def Element(self) -> XmlObjMgt_Element: ...
	def Length(self) -> int: ...
	def Lower(self) -> int: ...
	def SetValue(self, Index: int, Value: XmlObjMgt_Element) -> None: ...
	def Upper(self) -> int: ...
	def Value(self, Index: int) -> XmlObjMgt_Element: ...

class XmlObjMgt_GP:
	@staticmethod
	def Translate(self, aTrsf: gp_Trsf) -> XmlObjMgt_DOMString: ...
	@staticmethod
	def Translate(self, aMat: gp_Mat) -> XmlObjMgt_DOMString: ...
	@staticmethod
	def Translate(self, anXYZ: gp_XYZ) -> XmlObjMgt_DOMString: ...
	@staticmethod
	def Translate(self, aStr: XmlObjMgt_DOMString, T: gp_Trsf) -> bool: ...
	@staticmethod
	def Translate(self, aStr: XmlObjMgt_DOMString, T: gp_Mat) -> bool: ...
	@staticmethod
	def Translate(self, aStr: XmlObjMgt_DOMString, T: gp_XYZ) -> bool: ...

class XmlObjMgt_Persistent:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theElement: XmlObjMgt_Element) -> None: ...
	@overload
	def __init__(self, theElement: XmlObjMgt_Element, theRef: XmlObjMgt_DOMString) -> None: ...
	def CreateElement(self, theParent: XmlObjMgt_Element, theType: XmlObjMgt_DOMString, theID: int) -> None: ...
	def Element(self) -> XmlObjMgt_Element: ...
	def Element(self) -> XmlObjMgt_Element: ...
	def Id(self) -> int: ...
	def SetId(self, theId: int) -> None: ...

class XmlObjMgt_RRelocationTable(TColStd_DataMapOfIntegerTransient):
	def Clear(self, doReleaseMemory: Optional[bool]) -> None: ...
	def GetHeaderData(self) -> Storage_HeaderData: ...
	def SetHeaderData(self, theHeaderData: Storage_HeaderData) -> None: ...

class XmlObjMgt_SRelocationTable(TColStd_IndexedMapOfTransient):
	def Clear(self, doReleaseMemory: Optional[bool]) -> None: ...
	def GetHeaderData(self) -> Storage_HeaderData: ...
	def SetHeaderData(self, theHeaderData: Storage_HeaderData) -> None: ...

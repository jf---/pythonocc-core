from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BinMDF import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.BinObjMgt import *


class BinMDataStd:
	@staticmethod
	def AddDrivers(self, theDriverTable: BinMDF_ADriverTable, aMsgDrv: Message_Messenger) -> None: ...

class BinMDataStd_AsciiStringDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_BooleanArrayDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_BooleanListDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_ByteArrayDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_CommentDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_DirectoryDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_ExpressionDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_ExtStringArrayDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_ExtStringListDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_IntPackedMapDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_IntegerArrayDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_IntegerDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_IntegerListDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_NameDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_NamedDataDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_NoteBookDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_RealArrayDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_RealDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_RealListDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_ReferenceArrayDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_ReferenceListDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_RelationDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_TickDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_TreeNodeDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_UAttributeDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

class BinMDataStd_VariableDriver(BinMDF_ADriver):
	def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Source: BinObjMgt_Persistent, Target: TDF_Attribute, RelocTable: BinObjMgt_RRelocationTable) -> bool: ...
	def Paste(self, Source: TDF_Attribute, Target: BinObjMgt_Persistent, RelocTable: BinObjMgt_SRelocationTable) -> None: ...

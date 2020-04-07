from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *

NCollection_String = NewType('NCollection_String', NCollection_Utf8String)
Standard_Size = NewType('Standard_Size', int)

class NCollection_StdAllocator:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAlloc: NCollection_BaseAllocator) -> None: ...
	@overload
	def __init__(self, X: NCollection_StdAllocator) -> None: ...
	def Allocator(self) -> NCollection_BaseAllocator: ...

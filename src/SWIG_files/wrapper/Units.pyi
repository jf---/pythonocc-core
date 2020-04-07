from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *


class Units:
	@staticmethod
	def Convert(self, avalue: float, afirstunit: str, asecondunit: str) -> float: ...
	@staticmethod
	def DictionaryOfUnits(self, amode: Optional[bool]) -> Units_UnitsDictionary: ...
	@staticmethod
	def Dimensions(self, aType: str) -> Units_Dimensions: ...
	@staticmethod
	def FirstQuantity(self, aunit: str) -> str: ...
	@staticmethod
	def FromSI(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def FromSI(self, aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def LexiconFile(self, afile: str) -> None: ...
	@staticmethod
	def LexiconFormula(self) -> Units_Lexicon: ...
	@staticmethod
	def LexiconUnits(self, amode: Optional[bool]) -> Units_Lexicon: ...
	@staticmethod
	def NullDimensions(self) -> Units_Dimensions: ...
	@staticmethod
	def Quantity(self, aquantity: str) -> Units_Quantity: ...
	@staticmethod
	def ToSI(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def ToSI(self, aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def UnitsFile(self, afile: str) -> None: ...

class Units_Explorer:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aunitssystem: Units_UnitsSystem) -> None: ...
	@overload
	def __init__(self, aunitsdictionary: Units_UnitsDictionary) -> None: ...
	@overload
	def __init__(self, aunitssystem: Units_UnitsSystem, aquantity: str) -> None: ...
	@overload
	def __init__(self, aunitsdictionary: Units_UnitsDictionary, aquantity: str) -> None: ...
	def Init(self, aunitssystem: Units_UnitsSystem) -> None: ...
	def Init(self, aunitsdictionary: Units_UnitsDictionary) -> None: ...
	def Init(self, aunitssystem: Units_UnitsSystem, aquantity: str) -> None: ...
	def Init(self, aunitsdictionary: Units_UnitsDictionary, aquantity: str) -> None: ...
	def IsActive(self) -> bool: ...
	def MoreQuantity(self) -> bool: ...
	def MoreUnit(self) -> bool: ...
	def NextQuantity(self) -> None: ...
	def NextUnit(self) -> None: ...
	def Quantity(self) -> TCollection_AsciiString: ...
	def Unit(self) -> TCollection_AsciiString: ...

class Units_Lexicon(Standard_Transient):
	def __init__(self) -> None: ...
	def AddToken(self, aword: str, amean: str, avalue: float) -> None: ...
	def Creates(self) -> None: ...
	def Dump(self) -> None: ...
	def Sequence(self) -> Units_TokensSequence: ...

class Units_Measurement:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, avalue: float, atoken: Units_Token) -> None: ...
	@overload
	def __init__(self, avalue: float, aunit: str) -> None: ...
	def Add(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	def Convert(self, aunit: str) -> None: ...
	def Divide(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	def Divide(self, avalue: float) -> Units_Measurement: ...
	def Dump(self) -> None: ...
	def Fractional(self) -> Units_Measurement: ...
	def HasToken(self) -> bool: ...
	def Integer(self) -> Units_Measurement: ...
	def Measurement(self) -> float: ...
	def Multiply(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	def Multiply(self, avalue: float) -> Units_Measurement: ...
	def Power(self, anexponent: float) -> Units_Measurement: ...
	def Subtract(self, ameasurement: Units_Measurement) -> Units_Measurement: ...
	def Token(self) -> Units_Token: ...

class Units_Sentence:
	def __init__(self, alexicon: Units_Lexicon, astring: str) -> None: ...
	def Dump(self) -> None: ...
	def Evaluate(self) -> Units_Token: ...
	def IsDone(self) -> bool: ...
	def Sequence(self) -> Units_TokensSequence: ...
	def Sequence(self, asequenceoftokens: Units_TokensSequence) -> None: ...
	def SetConstants(self) -> None: ...

class Units_Token(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aword: str) -> None: ...
	@overload
	def __init__(self, atoken: Units_Token) -> None: ...
	@overload
	def __init__(self, aword: str, amean: str) -> None: ...
	@overload
	def __init__(self, aword: str, amean: str, avalue: float) -> None: ...
	@overload
	def __init__(self, aword: str, amean: str, avalue: float, adimension: Units_Dimensions) -> None: ...
	def Add(self, aninteger: int) -> Units_Token: ...
	def Add(self, atoken: Units_Token) -> Units_Token: ...
	def Creates(self) -> Units_Token: ...
	def Dimensions(self) -> Units_Dimensions: ...
	def Dimensions(self, adimensions: Units_Dimensions) -> None: ...
	def Divide(self, atoken: Units_Token) -> Units_Token: ...
	def Divided(self, avalue: float) -> float: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def IsEqual(self, astring: str) -> bool: ...
	def IsEqual(self, atoken: Units_Token) -> bool: ...
	def IsGreater(self, astring: str) -> bool: ...
	def IsGreater(self, atoken: Units_Token) -> bool: ...
	def IsGreaterOrEqual(self, atoken: Units_Token) -> bool: ...
	def IsLessOrEqual(self, astring: str) -> bool: ...
	def IsNotEqual(self, astring: str) -> bool: ...
	def IsNotEqual(self, atoken: Units_Token) -> bool: ...
	def Length(self) -> int: ...
	def Mean(self) -> TCollection_AsciiString: ...
	def Mean(self, amean: str) -> None: ...
	def Multiplied(self, avalue: float) -> float: ...
	def Multiply(self, atoken: Units_Token) -> Units_Token: ...
	def Power(self, atoken: Units_Token) -> Units_Token: ...
	def Power(self, anexponent: float) -> Units_Token: ...
	def Subtract(self, atoken: Units_Token) -> Units_Token: ...
	def Update(self, amean: str) -> None: ...
	def Value(self) -> float: ...
	def Value(self, avalue: float) -> None: ...
	def Word(self) -> TCollection_AsciiString: ...
	def Word(self, aword: str) -> None: ...

class Units_Unit(Standard_Transient):
	@overload
	def __init__(self, aname: str, asymbol: str, avalue: float, aquantity: Units_Quantity) -> None: ...
	@overload
	def __init__(self, aname: str, asymbol: str) -> None: ...
	@overload
	def __init__(self, aname: str) -> None: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def IsEqual(self, astring: str) -> bool: ...
	def Name(self) -> TCollection_AsciiString: ...
	def Quantity(self) -> Units_Quantity: ...
	def Quantity(self, aquantity: Units_Quantity) -> None: ...
	def Symbol(self, asymbol: str) -> None: ...
	def SymbolsSequence(self) -> TColStd_HSequenceOfHAsciiString: ...
	def Token(self) -> Units_Token: ...
	def Value(self) -> float: ...
	def Value(self, avalue: float) -> None: ...

class Units_UnitsDictionary(Standard_Transient):
	def __init__(self) -> None: ...
	def ActiveUnit(self, aquantity: str) -> TCollection_AsciiString: ...
	def Creates(self) -> None: ...
	def Dump(self, alevel: int) -> None: ...
	def Dump(self, adimensions: Units_Dimensions) -> None: ...
	def Sequence(self) -> Units_QuantitiesSequence: ...

class Units_UnitsSystem(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, aName: str, Verbose: Optional[bool]) -> None: ...
	def Activate(self, aquantity: str, aunit: str) -> None: ...
	def Activates(self) -> None: ...
	def ActiveUnit(self, aquantity: str) -> TCollection_AsciiString: ...
	def ActiveUnitsSequence(self) -> TColStd_HSequenceOfInteger: ...
	def ConvertSIValueToUserSystem(self, aquantity: str, avalue: float) -> float: ...
	def ConvertUserSystemValueToSI(self, aquantity: str, avalue: float) -> float: ...
	def ConvertValueToUserSystem(self, aquantity: str, avalue: float, aunit: str) -> float: ...
	def Dump(self) -> None: ...
	def IsEmpty(self) -> bool: ...
	def QuantitiesSequence(self) -> Units_QuantitiesSequence: ...
	def Remove(self, aquantity: str, aunit: str) -> None: ...
	def Specify(self, aquantity: str, aunit: str) -> None: ...

class Units_MathSentence(Units_Sentence):
	def __init__(self, astring: str) -> None: ...

class Units_ShiftedToken(Units_Token):
	def __init__(self, aword: str, amean: str, avalue: float, amove: float, adimensions: Units_Dimensions) -> None: ...
	def Creates(self) -> Units_Token: ...
	def Divided(self, avalue: float) -> float: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def Move(self) -> float: ...
	def Multiplied(self, avalue: float) -> float: ...

class Units_ShiftedUnit(Units_Unit):
	@overload
	def __init__(self, aname: str, asymbol: str, avalue: float, amove: float, aquantity: Units_Quantity) -> None: ...
	@overload
	def __init__(self, aname: str, asymbol: str) -> None: ...
	@overload
	def __init__(self, aname: str) -> None: ...
	def Dump(self, ashift: int, alevel: int) -> None: ...
	def Move(self, amove: float) -> None: ...
	def Move(self) -> float: ...
	def Token(self) -> Units_Token: ...

class Units_UnitSentence(Units_Sentence):
	@overload
	def __init__(self, astring: str) -> None: ...
	@overload
	def __init__(self, astring: str, aquantitiessequence: Units_QuantitiesSequence) -> None: ...
	def Analyse(self) -> None: ...
	def SetUnits(self, aquantitiessequence: Units_QuantitiesSequence) -> None: ...

class Units_UnitsLexicon(Units_Lexicon):
	def __init__(self) -> None: ...
	def Creates(self, amode: Optional[bool]) -> None: ...
	def Dump(self) -> None: ...

#classnotwrapped
class Units_Quantity:
	pass

#classnotwrapped
class Units_Dimensions:
	pass

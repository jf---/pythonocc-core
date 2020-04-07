from typing import overload, NewType, Optional, Tuple

from OCC.Core.Message import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *


class Message_Status:
	Message_None: int = ...
	Message_Done1: int = ...
	Message_Done2: int = ...
	Message_Done3: int = ...
	Message_Done4: int = ...
	Message_Done5: int = ...
	Message_Done6: int = ...
	Message_Done7: int = ...
	Message_Done8: int = ...
	Message_Done9: int = ...
	Message_Done10: int = ...
	Message_Done11: int = ...
	Message_Done12: int = ...
	Message_Done13: int = ...
	Message_Done14: int = ...
	Message_Done15: int = ...
	Message_Done16: int = ...
	Message_Done17: int = ...
	Message_Done18: int = ...
	Message_Done19: int = ...
	Message_Done20: int = ...
	Message_Done21: int = ...
	Message_Done22: int = ...
	Message_Done23: int = ...
	Message_Done24: int = ...
	Message_Done25: int = ...
	Message_Done26: int = ...
	Message_Done27: int = ...
	Message_Done28: int = ...
	Message_Done29: int = ...
	Message_Done30: int = ...
	Message_Done31: int = ...
	Message_Done32: int = ...
	Message_Warn1: int = ...
	Message_Warn2: int = ...
	Message_Warn3: int = ...
	Message_Warn4: int = ...
	Message_Warn5: int = ...
	Message_Warn6: int = ...
	Message_Warn7: int = ...
	Message_Warn8: int = ...
	Message_Warn9: int = ...
	Message_Warn10: int = ...
	Message_Warn11: int = ...
	Message_Warn12: int = ...
	Message_Warn13: int = ...
	Message_Warn14: int = ...
	Message_Warn15: int = ...
	Message_Warn16: int = ...
	Message_Warn17: int = ...
	Message_Warn18: int = ...
	Message_Warn19: int = ...
	Message_Warn20: int = ...
	Message_Warn21: int = ...
	Message_Warn22: int = ...
	Message_Warn23: int = ...
	Message_Warn24: int = ...
	Message_Warn25: int = ...
	Message_Warn26: int = ...
	Message_Warn27: int = ...
	Message_Warn28: int = ...
	Message_Warn29: int = ...
	Message_Warn30: int = ...
	Message_Warn31: int = ...
	Message_Warn32: int = ...
	Message_Alarm1: int = ...
	Message_Alarm2: int = ...
	Message_Alarm3: int = ...
	Message_Alarm4: int = ...
	Message_Alarm5: int = ...
	Message_Alarm6: int = ...
	Message_Alarm7: int = ...
	Message_Alarm8: int = ...
	Message_Alarm9: int = ...
	Message_Alarm10: int = ...
	Message_Alarm11: int = ...
	Message_Alarm12: int = ...
	Message_Alarm13: int = ...
	Message_Alarm14: int = ...
	Message_Alarm15: int = ...
	Message_Alarm16: int = ...
	Message_Alarm17: int = ...
	Message_Alarm18: int = ...
	Message_Alarm19: int = ...
	Message_Alarm20: int = ...
	Message_Alarm21: int = ...
	Message_Alarm22: int = ...
	Message_Alarm23: int = ...
	Message_Alarm24: int = ...
	Message_Alarm25: int = ...
	Message_Alarm26: int = ...
	Message_Alarm27: int = ...
	Message_Alarm28: int = ...
	Message_Alarm29: int = ...
	Message_Alarm30: int = ...
	Message_Alarm31: int = ...
	Message_Alarm32: int = ...
	Message_Fail1: int = ...
	Message_Fail2: int = ...
	Message_Fail3: int = ...
	Message_Fail4: int = ...
	Message_Fail5: int = ...
	Message_Fail6: int = ...
	Message_Fail7: int = ...
	Message_Fail8: int = ...
	Message_Fail9: int = ...
	Message_Fail10: int = ...
	Message_Fail11: int = ...
	Message_Fail12: int = ...
	Message_Fail13: int = ...
	Message_Fail14: int = ...
	Message_Fail15: int = ...
	Message_Fail16: int = ...
	Message_Fail17: int = ...
	Message_Fail18: int = ...
	Message_Fail19: int = ...
	Message_Fail20: int = ...
	Message_Fail21: int = ...
	Message_Fail22: int = ...
	Message_Fail23: int = ...
	Message_Fail24: int = ...
	Message_Fail25: int = ...
	Message_Fail26: int = ...
	Message_Fail27: int = ...
	Message_Fail28: int = ...
	Message_Fail29: int = ...
	Message_Fail30: int = ...
	Message_Fail31: int = ...
	Message_Fail32: int = ...

class Message_Gravity:
	Message_Trace: int = ...
	Message_Info: int = ...
	Message_Warning: int = ...
	Message_Alarm: int = ...
	Message_Fail: int = ...

class Message_StatusType:
	Message_DONE: int = ...
	Message_WARN: int = ...
	Message_ALARM: int = ...
	Message_FAIL: int = ...

class Message:
	@staticmethod
	def DefaultMessenger(self) -> Message_Messenger: ...
	@staticmethod
	def FillTime(self, Hour: int, Minute: int, Second: float) -> TCollection_AsciiString: ...

class Message_Alert(Standard_Transient):
	def GetMessageKey(self) -> str: ...
	def Merge(self, theTarget: Message_Alert) -> bool: ...
	def SupportsMerge(self) -> bool: ...

class Message_Algorithm(Standard_Transient):
	def __init__(self) -> None: ...
	def AddStatus(self, theOther: Message_Algorithm) -> None: ...
	def AddStatus(self, theStatus: Message_ExecStatus, theOther: Message_Algorithm) -> None: ...
	def ChangeStatus(self) -> Message_ExecStatus: ...
	def ClearStatus(self) -> None: ...
	def GetMessageNumbers(self, theStatus: Message_Status) -> TColStd_HPackedMapOfInteger: ...
	def GetMessageStrings(self, theStatus: Message_Status) -> TColStd_HSequenceOfHExtendedString: ...
	def GetMessenger(self) -> Message_Messenger: ...
	def GetStatus(self) -> Message_ExecStatus: ...
	@staticmethod
	def PrepareReport(self, theError: TColStd_HPackedMapOfInteger, theMaxCount: int) -> TCollection_ExtendedString: ...
	@staticmethod
	def PrepareReport(self, theReportSeq: TColStd_SequenceOfHExtendedString, theMaxCount: int) -> TCollection_ExtendedString: ...
	def SendMessages(self, theTraceLevel: Optional[Message_Gravity], theMaxCount: Optional[int]) -> None: ...
	def SendStatusMessages(self, theFilter: Message_ExecStatus, theTraceLevel: Optional[Message_Gravity], theMaxCount: Optional[int]) -> None: ...
	def SetMessenger(self, theMsgr: Message_Messenger) -> None: ...
	def SetStatus(self, theStat: Message_Status) -> None: ...
	def SetStatus(self, theStat: Message_Status, theInt: int) -> None: ...
	def SetStatus(self, theStat: Message_Status, theStr: str, noRepetitions: Optional[bool]) -> None: ...
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_AsciiString, noRepetitions: Optional[bool]) -> None: ...
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_HAsciiString, noRepetitions: Optional[bool]) -> None: ...
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_ExtendedString, noRepetitions: Optional[bool]) -> None: ...
	def SetStatus(self, theStat: Message_Status, theStr: TCollection_HExtendedString, noRepetitions: Optional[bool]) -> None: ...
	def SetStatus(self, theStat: Message_Status, theMsg: Message_Msg) -> None: ...

class Message_ExecStatus:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, status: Message_Status) -> None: ...
	def Add(self, theOther: Message_ExecStatus) -> None: ...
	def And(self, theOther: Message_ExecStatus) -> None: ...
	def Clear(self, status: Message_Status) -> None: ...
	def Clear(self) -> None: ...
	def ClearAllAlarm(self) -> None: ...
	def ClearAllDone(self) -> None: ...
	def ClearAllFail(self) -> None: ...
	def ClearAllWarn(self) -> None: ...
	def IsAlarm(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def IsFail(self) -> bool: ...
	def IsSet(self, status: Message_Status) -> bool: ...
	def IsWarn(self) -> bool: ...
	@staticmethod
	def LocalStatusIndex(self, status: Message_Status) -> int: ...
	def Set(self, status: Message_Status) -> None: ...
	def SetAllAlarm(self) -> None: ...
	def SetAllDone(self) -> None: ...
	def SetAllFail(self) -> None: ...
	def SetAllWarn(self) -> None: ...
	@staticmethod
	def StatusByIndex(self, theIndex: int) -> Message_Status: ...
	@staticmethod
	def StatusIndex(self, status: Message_Status) -> int: ...
	@staticmethod
	def TypeOfStatus(self, status: Message_Status) -> Message_StatusType: ...

class Message_Messenger(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, thePrinter: Message_Printer) -> None: ...
	def AddPrinter(self, thePrinter: Message_Printer) -> bool: ...
	def ChangePrinters(self) -> Message_SequenceOfPrinters: ...
	def Printers(self) -> Message_SequenceOfPrinters: ...
	def RemovePrinter(self, thePrinter: Message_Printer) -> bool: ...
	def RemovePrinters(self, theType: Standard_Type) -> int: ...
	def Send(self, theString: str, theGravity: Optional[Message_Gravity], putEndl: Optional[bool]) -> None: ...
	def Send(self, theString: TCollection_AsciiString, theGravity: Optional[Message_Gravity], putEndl: Optional[bool]) -> None: ...
	def Send(self, theString: TCollection_ExtendedString, theGravity: Optional[Message_Gravity], putEndl: Optional[bool]) -> None: ...

class Message_Msg:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theMsg: Message_Msg) -> None: ...
	@overload
	def __init__(self, theKey: str) -> None: ...
	@overload
	def __init__(self, theKey: TCollection_ExtendedString) -> None: ...
	def Arg(self, theString: str) -> Message_Msg: ...
	def Arg(self, theString: TCollection_AsciiString) -> Message_Msg: ...
	def Arg(self, theString: TCollection_HAsciiString) -> Message_Msg: ...
	def Arg(self, theString: TCollection_ExtendedString) -> Message_Msg: ...
	def Arg(self, theString: TCollection_HExtendedString) -> Message_Msg: ...
	def Arg(self, theInt: int) -> Message_Msg: ...
	def Arg(self, theReal: float) -> Message_Msg: ...
	def Get(self) -> TCollection_ExtendedString: ...
	def IsEdited(self) -> bool: ...
	def Original(self) -> TCollection_ExtendedString: ...
	def Set(self, theMsg: str) -> None: ...
	def Set(self, theMsg: TCollection_ExtendedString) -> None: ...
	def Value(self) -> TCollection_ExtendedString: ...

class Message_MsgFile:
	@staticmethod
	def AddMsg(self, key: TCollection_AsciiString, text: TCollection_ExtendedString) -> bool: ...
	@staticmethod
	def HasMsg(self, key: TCollection_AsciiString) -> bool: ...
	@staticmethod
	def Load(self, theDirName: str, theFileName: str) -> bool: ...
	@staticmethod
	def LoadFile(self, theFName: str) -> bool: ...
	@staticmethod
	def LoadFromEnv(self, theEnvName: str, theFileName: str, theLangExt: Optional[str]) -> bool: ...
	@staticmethod
	def LoadFromString(self, theContent: str, theLength: Optional[int]) -> bool: ...
	@staticmethod
	def Msg(self, key: str) -> TCollection_ExtendedString: ...
	@staticmethod
	def Msg(self, key: TCollection_AsciiString) -> TCollection_ExtendedString: ...

class Message_Printer(Standard_Transient):
	def GetTraceLevel(self) -> Message_Gravity: ...
	def Send(self, theString: TCollection_ExtendedString, theGravity: Message_Gravity, theToPutEol: bool) -> None: ...
	def Send(self, theString: str, theGravity: Message_Gravity, theToPutEol: bool) -> None: ...
	def Send(self, theString: TCollection_AsciiString, theGravity: Message_Gravity, theToPutEol: bool) -> None: ...
	def SetTraceLevel(self, theTraceLevel: Message_Gravity) -> None: ...

class Message_ProgressIndicator(Standard_Transient):
	def EndScope(self) -> bool: ...
	def GetNbScopes(self) -> int: ...
	def GetPosition(self) -> float: ...
	def GetScale(self) -> Tuple[float, float, float, bool]: ...
	def GetScope(self, index: int) -> Message_ProgressScale: ...
	def GetValue(self) -> float: ...
	def Increment(self) -> None: ...
	def Increment(self, step: float) -> None: ...
	def NewScope(self, name: Optional[str]) -> bool: ...
	def NewScope(self, name: TCollection_HAsciiString) -> bool: ...
	def NewScope(self, span: float, name: Optional[str]) -> bool: ...
	def NewScope(self, span: float, name: TCollection_HAsciiString) -> bool: ...
	def NextScope(self, name: Optional[str]) -> bool: ...
	def NextScope(self, span: float, name: Optional[str]) -> bool: ...
	def Reset(self) -> None: ...
	def SetInfinite(self, isInf: Optional[bool]) -> None: ...
	def SetName(self, name: str) -> None: ...
	def SetName(self, name: TCollection_HAsciiString) -> None: ...
	def SetRange(self, min: float, max: float) -> None: ...
	def SetScale(self, name: str, min: float, max: float, step: float, isInf: Optional[bool]) -> None: ...
	def SetScale(self, min: float, max: float, step: float, isInf: Optional[bool]) -> None: ...
	def SetStep(self, step: float) -> None: ...
	def SetValue(self, val: float) -> None: ...
	def Show(self, force: Optional[bool]) -> bool: ...
	def UserBreak(self) -> bool: ...

class Message_ProgressScale:
	def __init__(self) -> None: ...
	def BaseToLocal(self, val: float) -> float: ...
	def GetFirst(self) -> float: ...
	def GetInfinite(self) -> bool: ...
	def GetLast(self) -> float: ...
	def GetMax(self) -> float: ...
	def GetMin(self) -> float: ...
	def GetName(self) -> TCollection_HAsciiString: ...
	def GetStep(self) -> float: ...
	def LocalToBase(self, val: float) -> float: ...
	def SetInfinite(self, theInfinite: Optional[bool]) -> None: ...
	def SetMax(self, theMax: float) -> None: ...
	def SetMin(self, theMin: float) -> None: ...
	def SetName(self, theName: str) -> None: ...
	def SetName(self, theName: TCollection_HAsciiString) -> None: ...
	def SetRange(self, min: float, max: float) -> None: ...
	def SetScale(self, min: float, max: float, step: float, theInfinite: Optional[bool]) -> None: ...
	def SetSpan(self, first: float, last: float) -> None: ...
	def SetStep(self, theStep: float) -> None: ...

class Message_ProgressSentry:
	@overload
	def __init__(self, PI: Message_ProgressIndicator, name: str, min: float, max: float, step: float, isInf: Optional[bool], newScopeSpan: Optional[float]) -> None: ...
	@overload
	def __init__(self, PI: Message_ProgressIndicator, name: TCollection_HAsciiString, min: float, max: float, step: float, isInf: Optional[bool], newScopeSpan: Optional[float]) -> None: ...
	def More(self) -> bool: ...
	def Next(self, name: Optional[str]) -> None: ...
	def Next(self, span: float, name: Optional[str]) -> None: ...
	def Next(self, span: float, name: TCollection_HAsciiString) -> None: ...
	def Relieve(self) -> None: ...
	def Show(self) -> None: ...

class Message_Report(Standard_Transient):
	def __init__(self) -> None: ...
	def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> None: ...
	def Clear(self) -> None: ...
	def Clear(self, theGravity: Message_Gravity) -> None: ...
	def Clear(self, theType: Standard_Type) -> None: ...
	def GetAlerts(self, theGravity: Message_Gravity) -> Message_ListOfAlert: ...
	def HasAlert(self, theType: Standard_Type) -> bool: ...
	def HasAlert(self, theType: Standard_Type, theGravity: Message_Gravity) -> bool: ...
	def Merge(self, theOther: Message_Report) -> None: ...
	def Merge(self, theOther: Message_Report, theGravity: Message_Gravity) -> None: ...
	def SendMessages(self, theMessenger: Message_Messenger) -> None: ...
	def SendMessages(self, theMessenger: Message_Messenger, theGravity: Message_Gravity) -> None: ...

class Message_PrinterOStream(Message_Printer):
	@overload
	def __init__(self, theTraceLevel: Optional[Message_Gravity]) -> None: ...
	@overload
	def __init__(self, theFileName: str, theDoAppend: bool, theTraceLevel: Optional[Message_Gravity]) -> None: ...
	def Close(self) -> None: ...
	def GetStream(self) -> Standard_OStream: ...
	def GetUseUtf8(self) -> bool: ...
	def Send(self, theString: str, theGravity: Message_Gravity, putEndl: Optional[bool]) -> None: ...
	def Send(self, theString: TCollection_AsciiString, theGravity: Message_Gravity, putEndl: Optional[bool]) -> None: ...
	def Send(self, theString: TCollection_ExtendedString, theGravity: Message_Gravity, putEndl: Optional[bool]) -> None: ...
	def SetUseUtf8(self, useUtf8: bool) -> None: ...
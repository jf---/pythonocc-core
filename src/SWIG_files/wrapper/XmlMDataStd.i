/*
Copyright 2008-2020 Thomas Paviot (tpaviot@gmail.com)

This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/
%define XMLMDATASTDDOCSTRING
"XmlMDataStd module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_xmlmdatastd.html"
%enddef
%module (package="OCC.Core", docstring=XMLMDATASTDDOCSTRING) XmlMDataStd


%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/Operators.i
%include ../common/OccHandle.i


%{
#include<XmlMDataStd_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<XmlMDF_module.hxx>
#include<Message_module.hxx>
#include<TDF_module.hxx>
#include<XmlObjMgt_module.hxx>
#include<Resource_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import XmlMDF.i
%import Message.i
%import TDF.i
%import XmlObjMgt.i

%pythoncode {
from enum import IntEnum
from OCC.Core.Exception import *
};

/* public enums */
/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {
};
/* end python proxy for enums */

/* handles */
%wrap_handle(XmlMDataStd_AsciiStringDriver)
%wrap_handle(XmlMDataStd_BooleanArrayDriver)
%wrap_handle(XmlMDataStd_BooleanListDriver)
%wrap_handle(XmlMDataStd_ByteArrayDriver)
%wrap_handle(XmlMDataStd_CommentDriver)
%wrap_handle(XmlMDataStd_DirectoryDriver)
%wrap_handle(XmlMDataStd_ExpressionDriver)
%wrap_handle(XmlMDataStd_ExtStringArrayDriver)
%wrap_handle(XmlMDataStd_ExtStringListDriver)
%wrap_handle(XmlMDataStd_IntPackedMapDriver)
%wrap_handle(XmlMDataStd_IntegerArrayDriver)
%wrap_handle(XmlMDataStd_IntegerDriver)
%wrap_handle(XmlMDataStd_IntegerListDriver)
%wrap_handle(XmlMDataStd_NameDriver)
%wrap_handle(XmlMDataStd_NamedDataDriver)
%wrap_handle(XmlMDataStd_NoteBookDriver)
%wrap_handle(XmlMDataStd_RealArrayDriver)
%wrap_handle(XmlMDataStd_RealDriver)
%wrap_handle(XmlMDataStd_RealListDriver)
%wrap_handle(XmlMDataStd_ReferenceArrayDriver)
%wrap_handle(XmlMDataStd_ReferenceListDriver)
%wrap_handle(XmlMDataStd_RelationDriver)
%wrap_handle(XmlMDataStd_TickDriver)
%wrap_handle(XmlMDataStd_TreeNodeDriver)
%wrap_handle(XmlMDataStd_UAttributeDriver)
%wrap_handle(XmlMDataStd_VariableDriver)
/* end handles declaration */

/* templates */
/* end templates declaration */

/* typedefs */
/* end typedefs declaration */

/********************
* class XmlMDataStd *
********************/
%rename(xmlmdatastd) XmlMDataStd;
class XmlMDataStd {
	public:
		/****************** AddDrivers ******************/
		%feature("compactdefaultargs") AddDrivers;
		%feature("autodoc", "Adds the attribute drivers to <adrivertable>.

Parameters
----------
aDriverTable: XmlMDF_ADriverTable
anMsgDrv: Message_Messenger

Returns
-------
None
") AddDrivers;
		static void AddDrivers(const opencascade::handle<XmlMDF_ADriverTable> & aDriverTable, const opencascade::handle<Message_Messenger> & anMsgDrv);

};


%extend XmlMDataStd {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class XmlMDataStd_AsciiStringDriver *
**************************************/
class XmlMDataStd_AsciiStringDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_AsciiStringDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_AsciiStringDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_AsciiStringDriver;
		 XmlMDataStd_AsciiStringDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Persistent -> transient (retrieve).

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Transient -> persistent (store).

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_AsciiStringDriver)

%extend XmlMDataStd_AsciiStringDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class XmlMDataStd_BooleanArrayDriver *
***************************************/
class XmlMDataStd_BooleanArrayDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_BooleanArrayDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_BooleanArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_BooleanArrayDriver;
		 XmlMDataStd_BooleanArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_BooleanArrayDriver)

%extend XmlMDataStd_BooleanArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class XmlMDataStd_BooleanListDriver *
**************************************/
class XmlMDataStd_BooleanListDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_BooleanListDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_BooleanListDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_BooleanListDriver;
		 XmlMDataStd_BooleanListDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_BooleanListDriver)

%extend XmlMDataStd_BooleanListDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class XmlMDataStd_ByteArrayDriver *
************************************/
class XmlMDataStd_ByteArrayDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_ByteArrayDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_ByteArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_ByteArrayDriver;
		 XmlMDataStd_ByteArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_ByteArrayDriver)

%extend XmlMDataStd_ByteArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**********************************
* class XmlMDataStd_CommentDriver *
**********************************/
class XmlMDataStd_CommentDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_CommentDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_CommentDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_CommentDriver;
		 XmlMDataStd_CommentDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_CommentDriver)

%extend XmlMDataStd_CommentDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class XmlMDataStd_DirectoryDriver *
************************************/
class XmlMDataStd_DirectoryDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_DirectoryDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_DirectoryDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_DirectoryDriver;
		 XmlMDataStd_DirectoryDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_DirectoryDriver)

%extend XmlMDataStd_DirectoryDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************************
* class XmlMDataStd_ExpressionDriver *
*************************************/
class XmlMDataStd_ExpressionDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_ExpressionDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_ExpressionDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_ExpressionDriver;
		 XmlMDataStd_ExpressionDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_ExpressionDriver)

%extend XmlMDataStd_ExpressionDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************************
* class XmlMDataStd_ExtStringArrayDriver *
*****************************************/
class XmlMDataStd_ExtStringArrayDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_ExtStringArrayDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_ExtStringArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_ExtStringArrayDriver;
		 XmlMDataStd_ExtStringArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_ExtStringArrayDriver)

%extend XmlMDataStd_ExtStringArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************************
* class XmlMDataStd_ExtStringListDriver *
****************************************/
class XmlMDataStd_ExtStringListDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_ExtStringListDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_ExtStringListDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_ExtStringListDriver;
		 XmlMDataStd_ExtStringListDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_ExtStringListDriver)

%extend XmlMDataStd_ExtStringListDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class XmlMDataStd_IntPackedMapDriver *
***************************************/
class XmlMDataStd_IntPackedMapDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_IntPackedMapDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_IntPackedMapDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_IntPackedMapDriver;
		 XmlMDataStd_IntPackedMapDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Persistent -> transient (retrieve).

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "Transient -> persistent (store).

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_IntPackedMapDriver)

%extend XmlMDataStd_IntPackedMapDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class XmlMDataStd_IntegerArrayDriver *
***************************************/
class XmlMDataStd_IntegerArrayDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_IntegerArrayDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_IntegerArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_IntegerArrayDriver;
		 XmlMDataStd_IntegerArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_IntegerArrayDriver)

%extend XmlMDataStd_IntegerArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**********************************
* class XmlMDataStd_IntegerDriver *
**********************************/
class XmlMDataStd_IntegerDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_IntegerDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_IntegerDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_IntegerDriver;
		 XmlMDataStd_IntegerDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_IntegerDriver)

%extend XmlMDataStd_IntegerDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/**************************************
* class XmlMDataStd_IntegerListDriver *
**************************************/
class XmlMDataStd_IntegerListDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_IntegerListDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_IntegerListDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_IntegerListDriver;
		 XmlMDataStd_IntegerListDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_IntegerListDriver)

%extend XmlMDataStd_IntegerListDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*******************************
* class XmlMDataStd_NameDriver *
*******************************/
class XmlMDataStd_NameDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_NameDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_NameDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_NameDriver;
		 XmlMDataStd_NameDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_NameDriver)

%extend XmlMDataStd_NameDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class XmlMDataStd_NamedDataDriver *
************************************/
class XmlMDataStd_NamedDataDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_NamedDataDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_NamedDataDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_NamedDataDriver;
		 XmlMDataStd_NamedDataDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_NamedDataDriver)

%extend XmlMDataStd_NamedDataDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class XmlMDataStd_NoteBookDriver *
***********************************/
class XmlMDataStd_NoteBookDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_NoteBookDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_NoteBookDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_NoteBookDriver;
		 XmlMDataStd_NoteBookDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_NoteBookDriver)

%extend XmlMDataStd_NoteBookDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class XmlMDataStd_RealArrayDriver *
************************************/
class XmlMDataStd_RealArrayDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_RealArrayDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_RealArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_RealArrayDriver;
		 XmlMDataStd_RealArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_RealArrayDriver)

%extend XmlMDataStd_RealArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*******************************
* class XmlMDataStd_RealDriver *
*******************************/
class XmlMDataStd_RealDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_RealDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_RealDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_RealDriver;
		 XmlMDataStd_RealDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_RealDriver)

%extend XmlMDataStd_RealDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class XmlMDataStd_RealListDriver *
***********************************/
class XmlMDataStd_RealListDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_RealListDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_RealListDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_RealListDriver;
		 XmlMDataStd_RealListDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_RealListDriver)

%extend XmlMDataStd_RealListDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************************
* class XmlMDataStd_ReferenceArrayDriver *
*****************************************/
class XmlMDataStd_ReferenceArrayDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_ReferenceArrayDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_ReferenceArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_ReferenceArrayDriver;
		 XmlMDataStd_ReferenceArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_ReferenceArrayDriver)

%extend XmlMDataStd_ReferenceArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/****************************************
* class XmlMDataStd_ReferenceListDriver *
****************************************/
class XmlMDataStd_ReferenceListDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_ReferenceListDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_ReferenceListDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_ReferenceListDriver;
		 XmlMDataStd_ReferenceListDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_ReferenceListDriver)

%extend XmlMDataStd_ReferenceListDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class XmlMDataStd_RelationDriver *
***********************************/
class XmlMDataStd_RelationDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_RelationDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_RelationDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_RelationDriver;
		 XmlMDataStd_RelationDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_RelationDriver)

%extend XmlMDataStd_RelationDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*******************************
* class XmlMDataStd_TickDriver *
*******************************/
class XmlMDataStd_TickDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_TickDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_TickDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_TickDriver;
		 XmlMDataStd_TickDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_TickDriver)

%extend XmlMDataStd_TickDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class XmlMDataStd_TreeNodeDriver *
***********************************/
class XmlMDataStd_TreeNodeDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_TreeNodeDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_TreeNodeDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_TreeNodeDriver;
		 XmlMDataStd_TreeNodeDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_TreeNodeDriver)

%extend XmlMDataStd_TreeNodeDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*************************************
* class XmlMDataStd_UAttributeDriver *
*************************************/
class XmlMDataStd_UAttributeDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_UAttributeDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_UAttributeDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_UAttributeDriver;
		 XmlMDataStd_UAttributeDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_UAttributeDriver)

%extend XmlMDataStd_UAttributeDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class XmlMDataStd_VariableDriver *
***********************************/
class XmlMDataStd_VariableDriver : public XmlMDF_ADriver {
	public:
		/****************** XmlMDataStd_VariableDriver ******************/
		%feature("compactdefaultargs") XmlMDataStd_VariableDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") XmlMDataStd_VariableDriver;
		 XmlMDataStd_VariableDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: XmlObjMgt_Persistent
Target: TDF_Attribute
RelocTable: XmlObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const XmlObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, XmlObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: XmlObjMgt_Persistent
RelocTable: XmlObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, XmlObjMgt_Persistent & Target, XmlObjMgt_SRelocationTable & RelocTable);

};


%make_alias(XmlMDataStd_VariableDriver)

%extend XmlMDataStd_VariableDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */
/* harray2 classes */
/* hsequence classes */

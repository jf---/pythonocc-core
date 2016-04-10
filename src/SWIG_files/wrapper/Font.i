/*
Copyright 2008-2015 Thomas Paviot (tpaviot@gmail.com)


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
%module (package="OCC") Font

#pragma SWIG nowarn=504,325,503

%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/Operators.i


%include Font_headers.i


%pythoncode {
def register_handle(handle, base_object):
    """
    Inserts the handle into the base object to
    prevent memory corruption in certain cases
    """
    try:
        if base_object.IsKind("Standard_Transient"):
            base_object.thisHandle = handle
            base_object.thisown = False
    except:
        pass
};

/* typedefs */
typedef NCollection_List <Handle_Font_SystemFont> Font_NListOfSystemFont;
/* end typedefs declaration */

/* public enums */
enum Font_FontAspect {
	Font_FA_Undefined = 0,
	Font_FA_Regular = 1,
	Font_FA_Bold = 2,
	Font_FA_Italic = 3,
	Font_FA_BoldItalic = 4,
};

/* end public enums declaration */

%nodefaultctor Font_FontMgr;
class Font_FontMgr : public MMgt_TShared {
	public:
		%feature("compactdefaultargs") GetInstance;
		%feature("autodoc", "	:rtype: Handle_Font_FontMgr
") GetInstance;
		static Handle_Font_FontMgr GetInstance ();
		%feature("compactdefaultargs") GetAvailableFonts;
		%feature("autodoc", "	:rtype: Font_NListOfSystemFont
") GetAvailableFonts;
		const Font_NListOfSystemFont & GetAvailableFonts ();
		%feature("compactdefaultargs") GetAvailableFontsNames;
		%feature("autodoc", "	* Returns sequence of available fonts names

	:param theFontsNames:
	:type theFontsNames: TColStd_SequenceOfHAsciiString &
	:rtype: None
") GetAvailableFontsNames;
		void GetAvailableFontsNames (TColStd_SequenceOfHAsciiString & theFontsNames);
		%feature("compactdefaultargs") GetFont;
		%feature("autodoc", "	* Returns font that match given parameters. If theFontName is empty string returned font can have any FontName. If theFontAspect is Font_FA_Undefined returned font can have any FontAspect. If theFontSize is '-1' returned font can have any FontSize.

	:param theFontName:
	:type theFontName: Handle_TCollection_HAsciiString &
	:param theFontAspect:
	:type theFontAspect: Font_FontAspect
	:param theFontSize:
	:type theFontSize: int
	:rtype: Handle_Font_SystemFont
") GetFont;
		Handle_Font_SystemFont GetFont (const Handle_TCollection_HAsciiString & theFontName,const Font_FontAspect theFontAspect,const Standard_Integer theFontSize);
		%feature("compactdefaultargs") FindFont;
		%feature("autodoc", "	* Tries to find font by given parameters. If the specified font is not found tries to use font names mapping. If the requested family name not found -> search for any font family with given aspect and height. If the font is still not found, returns any font available in the system. Returns NULL in case when the fonts are not found in the system.

	:param theFontName:
	:type theFontName: Handle_TCollection_HAsciiString &
	:param theFontAspect:
	:type theFontAspect: Font_FontAspect
	:param theFontSize:
	:type theFontSize: int
	:rtype: Handle_Font_SystemFont
") FindFont;
		Handle_Font_SystemFont FindFont (const Handle_TCollection_HAsciiString & theFontName,const Font_FontAspect theFontAspect,const Standard_Integer theFontSize);
		%feature("compactdefaultargs") CheckFont;
		%feature("autodoc", "	* Read font file and retrieve information from it.

	:param theFontPath:
	:type theFontPath: char *
	:rtype: Handle_Font_SystemFont
") CheckFont;
		Handle_Font_SystemFont CheckFont (const char * theFontPath);
		%feature("compactdefaultargs") RegisterFont;
		%feature("autodoc", "	* Register new font. If there is existing entity with the same name and properties but different path then font will will be overridden or ignored depending on theToOverride flag.

	:param theFont:
	:type theFont: Handle_Font_SystemFont &
	:param theToOverride:
	:type theToOverride: bool
	:rtype: bool
") RegisterFont;
		Standard_Boolean RegisterFont (const Handle_Font_SystemFont & theFont,const Standard_Boolean theToOverride);
};


%extend Font_FontMgr {
	%pythoncode {
		def GetHandle(self):
		    try:
		        return self.thisHandle
		    except:
		        self.thisHandle = Handle_Font_FontMgr(self)
		        self.thisown = False
		        return self.thisHandle
	}
};

%pythonappend Handle_Font_FontMgr::Handle_Font_FontMgr %{
    # register the handle in the base object
    if len(args) > 0:
        register_handle(self, args[0])
%}

%nodefaultctor Handle_Font_FontMgr;
class Handle_Font_FontMgr : public Handle_MMgt_TShared {

    public:
        // constructors
        Handle_Font_FontMgr();
        Handle_Font_FontMgr(const Handle_Font_FontMgr &aHandle);
        Handle_Font_FontMgr(const Font_FontMgr *anItem);
        void Nullify();
        Standard_Boolean IsNull() const;
        static const Handle_Font_FontMgr DownCast(const Handle_Standard_Transient &AnObject);

};
%extend Handle_Font_FontMgr {
    Font_FontMgr* GetObject() {
    return (Font_FontMgr*)$self->Access();
    }
};

%nodefaultctor Font_SystemFont;
class Font_SystemFont : public MMgt_TShared {
	public:
		%feature("compactdefaultargs") Font_SystemFont;
		%feature("autodoc", "	* Creates empty font object

	:rtype: None
") Font_SystemFont;
		 Font_SystemFont ();
		%feature("compactdefaultargs") Font_SystemFont;
		%feature("autodoc", "	* Creates Font object initialized with <FontName> as name <FontAspect>.... TODO

	:param theFontName:
	:type theFontName: Handle_TCollection_HAsciiString &
	:param theFontAspect:
	:type theFontAspect: Font_FontAspect
	:param theFilePath:
	:type theFilePath: Handle_TCollection_HAsciiString &
	:rtype: None
") Font_SystemFont;
		 Font_SystemFont (const Handle_TCollection_HAsciiString & theFontName,const Font_FontAspect theFontAspect,const Handle_TCollection_HAsciiString & theFilePath);
		%feature("compactdefaultargs") Font_SystemFont;
		%feature("autodoc", "	* Creates Font object and initialize class fields with values taken from XLFD (X Logical Font Description)

	:param theXLFD:
	:type theXLFD: Handle_TCollection_HAsciiString &
	:param theFilePath:
	:type theFilePath: Handle_TCollection_HAsciiString &
	:rtype: None
") Font_SystemFont;
		 Font_SystemFont (const Handle_TCollection_HAsciiString & theXLFD,const Handle_TCollection_HAsciiString & theFilePath);
		%feature("compactdefaultargs") FontName;
		%feature("autodoc", "	* Returns font family name

	:rtype: Handle_TCollection_HAsciiString
") FontName;
		Handle_TCollection_HAsciiString FontName ();
		%feature("compactdefaultargs") FontPath;
		%feature("autodoc", "	* Returns font file path Level: Public

	:rtype: Handle_TCollection_HAsciiString
") FontPath;
		Handle_TCollection_HAsciiString FontPath ();
		%feature("compactdefaultargs") FontAspect;
		%feature("autodoc", "	* Returns font aspect Level: Public

	:rtype: Font_FontAspect
") FontAspect;
		Font_FontAspect FontAspect ();
		%feature("compactdefaultargs") FontHeight;
		%feature("autodoc", "	* Returns font height If returned value is equal -1 it means that font is resizable Level: Public

	:rtype: int
") FontHeight;
		Standard_Integer FontHeight ();
		%feature("compactdefaultargs") IsValid;
		%feature("autodoc", "	:rtype: bool
") IsValid;
		Standard_Boolean IsValid ();
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "	* Return true if the FontName, FontAspect and FontSize are the same. Level: Public

	:param theOtherFont:
	:type theOtherFont: Handle_Font_SystemFont &
	:rtype: bool
") IsEqual;
		Standard_Boolean IsEqual (const Handle_Font_SystemFont & theOtherFont);
};


%extend Font_SystemFont {
	%pythoncode {
		def GetHandle(self):
		    try:
		        return self.thisHandle
		    except:
		        self.thisHandle = Handle_Font_SystemFont(self)
		        self.thisown = False
		        return self.thisHandle
	}
};

%pythonappend Handle_Font_SystemFont::Handle_Font_SystemFont %{
    # register the handle in the base object
    if len(args) > 0:
        register_handle(self, args[0])
%}

%nodefaultctor Handle_Font_SystemFont;
class Handle_Font_SystemFont : public Handle_MMgt_TShared {

    public:
        // constructors
        Handle_Font_SystemFont();
        Handle_Font_SystemFont(const Handle_Font_SystemFont &aHandle);
        Handle_Font_SystemFont(const Font_SystemFont *anItem);
        void Nullify();
        Standard_Boolean IsNull() const;
        static const Handle_Font_SystemFont DownCast(const Handle_Standard_Transient &AnObject);

};
%extend Handle_Font_SystemFont {
    Font_SystemFont* GetObject() {
    return (Font_SystemFont*)$self->Access();
    }
};

%nodefaultctor Font_BRepFont;
class Font_BRepFont : protected Font_FTFont {
	public:
		%feature("compactdefaultargs") Font_BRepFont;
		%feature("autodoc", "	* Empty constructor

	:rtype: None
") Font_BRepFont;
		 Font_BRepFont ();
		%feature("compactdefaultargs") Font_BRepFont;
		%feature("autodoc", "	* Constructor with initialization. @param theFontPath FULL path to the font @param theSize the face size in model units

	:param theFontPath:
	:type theFontPath: NCollection_String &
	:param theSize:
	:type theSize: float
	:rtype: None
") Font_BRepFont;
		 Font_BRepFont (const NCollection_String & theFontPath,const Standard_Real theSize);
		%feature("compactdefaultargs") Font_BRepFont;
		%feature("autodoc", "	* Constructor with initialization. @param theFontName the font name @param theFontAspect the font style @param theSize the face size in model units

	:param theFontName:
	:type theFontName: NCollection_String &
	:param theFontAspect:
	:type theFontAspect: Font_FontAspect
	:param theSize:
	:type theSize: float
	:rtype: None
") Font_BRepFont;
		 Font_BRepFont (const NCollection_String & theFontName,const Font_FontAspect theFontAspect,const Standard_Real theSize);
		%feature("compactdefaultargs") Release;
		%feature("autodoc", "	* Release currently loaded font.

	:rtype: void
") Release;
		virtual void Release ();
		%feature("compactdefaultargs") Init;
		%feature("autodoc", "	* Initialize the font. @param theFontPath FULL path to the font @param theSize the face size in model units returns true on success

	:param theFontPath:
	:type theFontPath: NCollection_String &
	:param theSize:
	:type theSize: float
	:rtype: bool
") Init;
		bool Init (const NCollection_String & theFontPath,const Standard_Real theSize);
		%feature("compactdefaultargs") Init;
		%feature("autodoc", "	* Initialize the font. Please take into account that size is specified NOT in typography points (pt.). If you need to specify size in points, value should be converted. Formula for pt. -> m conversion: aSizeMeters = 0.0254 * theSizePt / 72.0 @param theFontName the font name @param theFontAspect the font style @param theSize the face size in model units returns true on success

	:param theFontName:
	:type theFontName: NCollection_String &
	:param theFontAspect:
	:type theFontAspect: Font_FontAspect
	:param theSize:
	:type theSize: float
	:rtype: bool
") Init;
		bool Init (const NCollection_String & theFontName,const Font_FontAspect theFontAspect,const Standard_Real theSize);
		%feature("compactdefaultargs") RenderGlyph;
		%feature("autodoc", "	* Render single glyph as TopoDS_Shape. @param theChar glyph identifier returns rendered glyph within cache, might be NULL shape

	:param theChar:
	:type theChar: Standard_Utf32Char &
	:rtype: TopoDS_Shape
") RenderGlyph;
		TopoDS_Shape RenderGlyph (const Standard_Utf32Char & theChar);
		%feature("compactdefaultargs") SetCompositeCurveMode;
		%feature("autodoc", "	* Setup glyph geometry construction mode. By default algorithm creates independent TopoDS_Edge for each original curve in the glyph (line segment or Bezie curve). Algorithm might optionally create composite BSpline curve for each contour which reduces memory footprint but limits curve class to C0. Notice that altering this flag clears currently accumulated cache!

	:param theToConcatenate:
	:type theToConcatenate: bool
	:rtype: None
") SetCompositeCurveMode;
		void SetCompositeCurveMode (const Standard_Boolean theToConcatenate);
		%feature("compactdefaultargs") RenderText;
		%feature("autodoc", "	* Render text as BRep shape. @param theString text in UTF-8 encoding returns result shape within XOY plane and start position (0,0,0) on the baseline

	:param theString:
	:type theString: NCollection_String &
	:rtype: TopoDS_Shape
") RenderText;
		TopoDS_Shape RenderText (const NCollection_String & theString);
		%feature("compactdefaultargs") RenderText;
		%feature("autodoc", "	* Render text as BRep shape. @param theString text in UTF-8 encoding @param thePenLoc start position and orientation on the baseline returns result shape with pen transformation applied as shape location

	:param theString:
	:type theString: NCollection_String &
	:param thePenLoc:
	:type thePenLoc: gp_Ax3
	:rtype: TopoDS_Shape
") RenderText;
		TopoDS_Shape RenderText (const NCollection_String & theString,const gp_Ax3 & thePenLoc);
		%feature("compactdefaultargs") Ascender;
		%feature("autodoc", "	* returns vertical distance from the horizontal baseline to the highest character coordinate.

	:rtype: float
") Ascender;
		Standard_Real Ascender ();
		%feature("compactdefaultargs") Descender;
		%feature("autodoc", "	* returns vertical distance from the horizontal baseline to the lowest character coordinate.

	:rtype: float
") Descender;
		Standard_Real Descender ();
		%feature("compactdefaultargs") LineSpacing;
		%feature("autodoc", "	* returns default line spacing (the baseline-to-baseline distance).

	:rtype: float
") LineSpacing;
		Standard_Real LineSpacing ();
		%feature("compactdefaultargs") PointSize;
		%feature("autodoc", "	* Configured point size

	:rtype: float
") PointSize;
		Standard_Real PointSize ();
		%feature("compactdefaultargs") AdvanceX;
		%feature("autodoc", "	* Compute advance to the next character with kerning applied when applicable. Assuming text rendered horizontally.

	:param theUCharNext:
	:type theUCharNext: Standard_Utf32Char
	:rtype: float
") AdvanceX;
		Standard_Real AdvanceX (const Standard_Utf32Char theUCharNext);
		%feature("compactdefaultargs") AdvanceX;
		%feature("autodoc", "	* Compute advance to the next character with kerning applied when applicable. Assuming text rendered horizontally.

	:param theUChar:
	:type theUChar: Standard_Utf32Char
	:param theUCharNext:
	:type theUCharNext: Standard_Utf32Char
	:rtype: float
") AdvanceX;
		Standard_Real AdvanceX (const Standard_Utf32Char theUChar,const Standard_Utf32Char theUCharNext);
		%feature("compactdefaultargs") AdvanceY;
		%feature("autodoc", "	* Compute advance to the next character with kerning applied when applicable. Assuming text rendered vertically.

	:param theUCharNext:
	:type theUCharNext: Standard_Utf32Char
	:rtype: float
") AdvanceY;
		Standard_Real AdvanceY (const Standard_Utf32Char theUCharNext);
		%feature("compactdefaultargs") AdvanceY;
		%feature("autodoc", "	* Compute advance to the next character with kerning applied when applicable. Assuming text rendered vertically.

	:param theUChar:
	:type theUChar: Standard_Utf32Char
	:param theUCharNext:
	:type theUCharNext: Standard_Utf32Char
	:rtype: float
") AdvanceY;
		Standard_Real AdvanceY (const Standard_Utf32Char theUChar,const Standard_Utf32Char theUCharNext);
};



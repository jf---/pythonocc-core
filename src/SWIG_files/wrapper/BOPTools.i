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
%define BOPTOOLSDOCSTRING
"BOPTools module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_boptools.html"
%enddef
%module (package="OCC.Core", docstring=BOPTOOLSDOCSTRING) BOPTools


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
#include<BOPTools_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<TopoDS_module.hxx>
#include<IntTools_module.hxx>
#include<gp_module.hxx>
#include<TopAbs_module.hxx>
#include<TopTools_module.hxx>
#include<Message_module.hxx>
#include<Geom_module.hxx>
#include<Geom2d_module.hxx>
#include<BRepAdaptor_module.hxx>
#include<Extrema_module.hxx>
#include<Adaptor2d_module.hxx>
#include<Approx_module.hxx>
#include<Adaptor3d_module.hxx>
#include<GeomAdaptor_module.hxx>
#include<IntPatch_module.hxx>
#include<TopLoc_module.hxx>
#include<Geom2dAdaptor_module.hxx>
#include<Message_module.hxx>
#include<TopTools_module.hxx>
#include<AppParCurves_module.hxx>
#include<Bnd_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import TopoDS.i
%import IntTools.i
%import gp.i
%import TopAbs.i
%import TopTools.i
%import Message.i
%import Geom.i
%import Geom2d.i
%import BRepAdaptor.i

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
/* end handles declaration */

/* templates */
%template(BOPTools_IndexedDataMapOfSetShape) NCollection_IndexedDataMap<BOPTools_Set,TopoDS_Shape,BOPTools_SetMapHasher>;
%template(BOPTools_ListOfConnexityBlock) NCollection_List<BOPTools_ConnexityBlock>;
%template(BOPTools_ListOfCoupleOfShape) NCollection_List<BOPTools_CoupleOfShape>;
%template(BOPTools_MapOfSet) NCollection_Map<BOPTools_Set,BOPTools_SetMapHasher>;
/* end templates declaration */

/* typedefs */
typedef BOPTools_PairSelector<2> BOPTools_Box2dPairSelector;
typedef BOPTools_BoxSet<Standard_Real, 2, Standard_Integer> BOPTools_Box2dTree;
typedef BOPTools_BoxSelector<2> BOPTools_Box2dTreeSelector;
typedef BOPTools_PairSelector<3> BOPTools_BoxPairSelector;
typedef BOPTools_BoxSet<Standard_Real, 3, Standard_Integer> BOPTools_BoxTree;
typedef BOPTools_BoxSelector<3> BOPTools_BoxTreeSelector;
typedef NCollection_IndexedDataMap<BOPTools_Set, TopoDS_Shape, BOPTools_SetMapHasher> BOPTools_IndexedDataMapOfSetShape;
typedef BOPTools_ListOfConnexityBlock::Iterator BOPTools_ListIteratorOfListOfConnexityBlock;
typedef BOPTools_ListOfCoupleOfShape::Iterator BOPTools_ListIteratorOfListOfCoupleOfShape;
typedef NCollection_List<BOPTools_ConnexityBlock> BOPTools_ListOfConnexityBlock;
typedef NCollection_List<BOPTools_CoupleOfShape> BOPTools_ListOfCoupleOfShape;
typedef BOPTools_MapOfSet::Iterator BOPTools_MapIteratorOfMapOfSet;
typedef NCollection_Map<BOPTools_Set, BOPTools_SetMapHasher> BOPTools_MapOfSet;
/* end typedefs declaration */

/***************************
* class BOPTools_AlgoTools *
***************************/
class BOPTools_AlgoTools {
	public:
		/****************** AreFacesSameDomain ******************/
		%feature("compactdefaultargs") AreFacesSameDomain;
		%feature("autodoc", "Checks if the given faces are same-domain, i.e. coincide.

Parameters
----------
theF1: TopoDS_Face
theF2: TopoDS_Face
theContext: IntTools_Context
theFuzz: float,optional
	default value is Precision::Confusion()

Returns
-------
bool
") AreFacesSameDomain;
		static Standard_Boolean AreFacesSameDomain(const TopoDS_Face & theF1, const TopoDS_Face & theF2, const opencascade::handle<IntTools_Context> & theContext, const Standard_Real theFuzz = Precision::Confusion());

		/****************** ComputeState ******************/
		%feature("compactdefaultargs") ComputeState;
		%feature("autodoc", "Computes the 3-d state of the point thepoint toward solid thesolid. thetol - value of precision of computation thecontext- cahed geometrical tools returns 3-d state.

Parameters
----------
thePoint: gp_Pnt
theSolid: TopoDS_Solid
theTol: float
theContext: IntTools_Context

Returns
-------
TopAbs_State
") ComputeState;
		static TopAbs_State ComputeState(const gp_Pnt & thePoint, const TopoDS_Solid & theSolid, const Standard_Real theTol, const opencascade::handle<IntTools_Context> & theContext);

		/****************** ComputeState ******************/
		%feature("compactdefaultargs") ComputeState;
		%feature("autodoc", "Computes the 3-d state of the vertex thevertex toward solid thesolid. thetol - value of precision of computation thecontext- cahed geometrical tools returns 3-d state.

Parameters
----------
theVertex: TopoDS_Vertex
theSolid: TopoDS_Solid
theTol: float
theContext: IntTools_Context

Returns
-------
TopAbs_State
") ComputeState;
		static TopAbs_State ComputeState(const TopoDS_Vertex & theVertex, const TopoDS_Solid & theSolid, const Standard_Real theTol, const opencascade::handle<IntTools_Context> & theContext);

		/****************** ComputeState ******************/
		%feature("compactdefaultargs") ComputeState;
		%feature("autodoc", "Computes the 3-d state of the edge theedge toward solid thesolid. thetol - value of precision of computation thecontext- cahed geometrical tools returns 3-d state.

Parameters
----------
theEdge: TopoDS_Edge
theSolid: TopoDS_Solid
theTol: float
theContext: IntTools_Context

Returns
-------
TopAbs_State
") ComputeState;
		static TopAbs_State ComputeState(const TopoDS_Edge & theEdge, const TopoDS_Solid & theSolid, const Standard_Real theTol, const opencascade::handle<IntTools_Context> & theContext);

		/****************** ComputeState ******************/
		%feature("compactdefaultargs") ComputeState;
		%feature("autodoc", "Computes the 3-d state of the face theface toward solid thesolid. thetol - value of precision of computation thebounds - set of edges of <thesolid> to avoid thecontext- cahed geometrical tools returns 3-d state.

Parameters
----------
theFace: TopoDS_Face
theSolid: TopoDS_Solid
theTol: float
theBounds: TopTools_IndexedMapOfShape
theContext: IntTools_Context

Returns
-------
TopAbs_State
") ComputeState;
		static TopAbs_State ComputeState(const TopoDS_Face & theFace, const TopoDS_Solid & theSolid, const Standard_Real theTol, const TopTools_IndexedMapOfShape & theBounds, const opencascade::handle<IntTools_Context> & theContext);

		/****************** ComputeStateByOnePoint ******************/
		%feature("compactdefaultargs") ComputeStateByOnePoint;
		%feature("autodoc", "Computes the 3-d state of the shape theshape toward solid thesolid. thetol - value of precision of computation thecontext- cahed geometrical tools returns 3-d state.

Parameters
----------
theShape: TopoDS_Shape
theSolid: TopoDS_Solid
theTol: float
theContext: IntTools_Context

Returns
-------
TopAbs_State
") ComputeStateByOnePoint;
		static TopAbs_State ComputeStateByOnePoint(const TopoDS_Shape & theShape, const TopoDS_Solid & theSolid, const Standard_Real theTol, const opencascade::handle<IntTools_Context> & theContext);

		/****************** ComputeTolerance ******************/
		%feature("compactdefaultargs") ComputeTolerance;
		%feature("autodoc", "Computes the necessary value of the tolerance for the edge.

Parameters
----------
theFace: TopoDS_Face
theEdge: TopoDS_Edge

Returns
-------
theMaxDist: float
theMaxPar: float
") ComputeTolerance;
		static Standard_Boolean ComputeTolerance(const TopoDS_Face & theFace, const TopoDS_Edge & theEdge, Standard_Real &OutValue, Standard_Real &OutValue);

		/****************** ComputeVV ******************/
		%feature("compactdefaultargs") ComputeVV;
		%feature("autodoc", "Intersects the vertex <thev1> with the point <thep> with tolerance <thetolp>. returns the error status: - 0 - no error, meaning that the vertex intersects the point; - 1 - the distance between vertex and point is grater than the sum of tolerances.

Parameters
----------
theV: TopoDS_Vertex
theP: gp_Pnt
theTolP: float

Returns
-------
int
") ComputeVV;
		static Standard_Integer ComputeVV(const TopoDS_Vertex & theV, const gp_Pnt & theP, const Standard_Real theTolP);

		/****************** ComputeVV ******************/
		%feature("compactdefaultargs") ComputeVV;
		%feature("autodoc", "Intersects the given vertices with given fuzzy value. returns the error status: - 0 - no error, meaning that the vertices interferes with given tolerance; - 1 - the distance between vertices is grater than the sum of their tolerances.

Parameters
----------
theV1: TopoDS_Vertex
theV2: TopoDS_Vertex
theFuzz: float,optional
	default value is Precision::Confusion()

Returns
-------
int
") ComputeVV;
		static Standard_Integer ComputeVV(const TopoDS_Vertex & theV1, const TopoDS_Vertex & theV2, const Standard_Real theFuzz = Precision::Confusion());

		/****************** CopyEdge ******************/
		%feature("compactdefaultargs") CopyEdge;
		%feature("autodoc", "Makes a copy of <theedge> with vertices.

Parameters
----------
theEdge: TopoDS_Edge

Returns
-------
TopoDS_Edge
") CopyEdge;
		static TopoDS_Edge CopyEdge(const TopoDS_Edge & theEdge);

		/****************** CorrectCurveOnSurface ******************/
		%feature("compactdefaultargs") CorrectCurveOnSurface;
		%feature("autodoc", "Provides valid values of tolerances for the shape <thes> in terms of brepcheck_invalidcurveonsurface.

Parameters
----------
theS: TopoDS_Shape
theMapToAvoid: TopTools_IndexedMapOfShape
theTolMax: float,optional
	default value is 0.0001
theRunParallel: bool,optional
	default value is Standard_False

Returns
-------
None
") CorrectCurveOnSurface;
		static void CorrectCurveOnSurface(const TopoDS_Shape & theS, const TopTools_IndexedMapOfShape & theMapToAvoid, const Standard_Real theTolMax = 0.0001, const Standard_Boolean theRunParallel = Standard_False);

		/****************** CorrectPointOnCurve ******************/
		%feature("compactdefaultargs") CorrectPointOnCurve;
		%feature("autodoc", "Provides valid values of tolerances for the shape <thes> in terms of brepcheck_invalidpointoncurve.

Parameters
----------
theS: TopoDS_Shape
theMapToAvoid: TopTools_IndexedMapOfShape
theTolMax: float,optional
	default value is 0.0001
theRunParallel: bool,optional
	default value is Standard_False

Returns
-------
None
") CorrectPointOnCurve;
		static void CorrectPointOnCurve(const TopoDS_Shape & theS, const TopTools_IndexedMapOfShape & theMapToAvoid, const Standard_Real theTolMax = 0.0001, const Standard_Boolean theRunParallel = Standard_False);

		/****************** CorrectRange ******************/
		%feature("compactdefaultargs") CorrectRange;
		%feature("autodoc", "Correct shrunk range <asr> taking into account 3d-curve resolution and corresponding tolerance values of <ae1>, <ae2>.

Parameters
----------
aE1: TopoDS_Edge
aE2: TopoDS_Edge
aSR: IntTools_Range
aNewSR: IntTools_Range

Returns
-------
None
") CorrectRange;
		static void CorrectRange(const TopoDS_Edge & aE1, const TopoDS_Edge & aE2, const IntTools_Range & aSR, IntTools_Range & aNewSR);

		/****************** CorrectRange ******************/
		%feature("compactdefaultargs") CorrectRange;
		%feature("autodoc", "Correct shrunk range <asr> taking into account 3d-curve resolution and corresponding tolerance values of <ae>, <af>.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aSR: IntTools_Range
aNewSR: IntTools_Range

Returns
-------
None
") CorrectRange;
		static void CorrectRange(const TopoDS_Edge & aE, const TopoDS_Face & aF, const IntTools_Range & aSR, IntTools_Range & aNewSR);

		/****************** CorrectShapeTolerances ******************/
		%feature("compactdefaultargs") CorrectShapeTolerances;
		%feature("autodoc", "Corrects tolerance values of the sub-shapes of the shape <thes> if needed.

Parameters
----------
theS: TopoDS_Shape
theMapToAvoid: TopTools_IndexedMapOfShape
theRunParallel: bool,optional
	default value is Standard_False

Returns
-------
None
") CorrectShapeTolerances;
		static void CorrectShapeTolerances(const TopoDS_Shape & theS, const TopTools_IndexedMapOfShape & theMapToAvoid, const Standard_Boolean theRunParallel = Standard_False);

		/****************** CorrectTolerances ******************/
		%feature("compactdefaultargs") CorrectTolerances;
		%feature("autodoc", "Provides valid values of tolerances for the shape <thes> <thetolmax> is max value of the tolerance that can be accepted for correction. if real value of the tolerance will be greater than <atolmax>, the correction does not perform.

Parameters
----------
theS: TopoDS_Shape
theMapToAvoid: TopTools_IndexedMapOfShape
theTolMax: float,optional
	default value is 0.0001
theRunParallel: bool,optional
	default value is Standard_False

Returns
-------
None
") CorrectTolerances;
		static void CorrectTolerances(const TopoDS_Shape & theS, const TopTools_IndexedMapOfShape & theMapToAvoid, const Standard_Real theTolMax = 0.0001, const Standard_Boolean theRunParallel = Standard_False);

		/****************** Dimension ******************/
		%feature("compactdefaultargs") Dimension;
		%feature("autodoc", "Retutns dimension of the shape <thes>.

Parameters
----------
theS: TopoDS_Shape

Returns
-------
int
") Dimension;
		static Standard_Integer Dimension(const TopoDS_Shape & theS);

		/****************** GetEdgeOff ******************/
		%feature("compactdefaultargs") GetEdgeOff;
		%feature("autodoc", "Returns true if the face theface contains the edge theedge but with opposite orientation. if the method returns true theedgeoff is the edge founded.

Parameters
----------
theEdge: TopoDS_Edge
theFace: TopoDS_Face
theEdgeOff: TopoDS_Edge

Returns
-------
bool
") GetEdgeOff;
		static Standard_Boolean GetEdgeOff(const TopoDS_Edge & theEdge, const TopoDS_Face & theFace, TopoDS_Edge & theEdgeOff);

		/****************** GetEdgeOnFace ******************/
		%feature("compactdefaultargs") GetEdgeOnFace;
		%feature("autodoc", "For the face theface gets the edge theedgeonf that is the same as theedge returns true if such edge exists returns false if there is no such edge.

Parameters
----------
theEdge: TopoDS_Edge
theFace: TopoDS_Face
theEdgeOnF: TopoDS_Edge

Returns
-------
bool
") GetEdgeOnFace;
		static Standard_Boolean GetEdgeOnFace(const TopoDS_Edge & theEdge, const TopoDS_Face & theFace, TopoDS_Edge & theEdgeOnF);

		/****************** GetFaceOff ******************/
		%feature("compactdefaultargs") GetFaceOff;
		%feature("autodoc", "For the face theface and its edge theedge finds the face suitable to produce shell. thelcef - set of faces to search. all faces from thelcef must share edge theedge.

Parameters
----------
theEdge: TopoDS_Edge
theFace: TopoDS_Face
theLCEF: BOPTools_ListOfCoupleOfShape
theFaceOff: TopoDS_Face
theContext: IntTools_Context

Returns
-------
bool
") GetFaceOff;
		static Standard_Boolean GetFaceOff(const TopoDS_Edge & theEdge, const TopoDS_Face & theFace, BOPTools_ListOfCoupleOfShape & theLCEF, TopoDS_Face & theFaceOff, const opencascade::handle<IntTools_Context> & theContext);

		/****************** IsBlockInOnFace ******************/
		%feature("compactdefaultargs") IsBlockInOnFace;
		%feature("autodoc", "Returns true if paveblock <apb> lays on the face <af>, i.e the <pb> is in or on in 2d of <af>.

Parameters
----------
aShR: IntTools_Range
aF: TopoDS_Face
aE: TopoDS_Edge
aContext: IntTools_Context

Returns
-------
bool
") IsBlockInOnFace;
		static Standard_Boolean IsBlockInOnFace(const IntTools_Range & aShR, const TopoDS_Face & aF, const TopoDS_Edge & aE, const opencascade::handle<IntTools_Context> & aContext);

		/****************** IsHole ******************/
		%feature("compactdefaultargs") IsHole;
		%feature("autodoc", "Checks if the wire is a hole for the face.

Parameters
----------
theW: TopoDS_Shape
theF: TopoDS_Shape

Returns
-------
bool
") IsHole;
		static Standard_Boolean IsHole(const TopoDS_Shape & theW, const TopoDS_Shape & theF);

		/****************** IsInternalFace ******************/
		%feature("compactdefaultargs") IsInternalFace;
		%feature("autodoc", "Returns true if the face theface is inside of the couple of faces theface1, theface2. the faces theface, theface1, theface2 must share the edge theedge return values: * 0 state is not in * 1 state is in * 2 state can not be found by the method of angles.

Parameters
----------
theFace: TopoDS_Face
theEdge: TopoDS_Edge
theFace1: TopoDS_Face
theFace2: TopoDS_Face
theContext: IntTools_Context

Returns
-------
int
") IsInternalFace;
		static Standard_Integer IsInternalFace(const TopoDS_Face & theFace, const TopoDS_Edge & theEdge, const TopoDS_Face & theFace1, const TopoDS_Face & theFace2, const opencascade::handle<IntTools_Context> & theContext);

		/****************** IsInternalFace ******************/
		%feature("compactdefaultargs") IsInternalFace;
		%feature("autodoc", "Returns true if the face theface is inside of the appropriate couple of faces (from the set thelf) . the faces of the set thelf and theface must share the edge theedge * 0 state is not in * 1 state is in * 2 state can not be found by the method of angles.

Parameters
----------
theFace: TopoDS_Face
theEdge: TopoDS_Edge
theLF: TopTools_ListOfShape
theContext: IntTools_Context

Returns
-------
int
") IsInternalFace;
		static Standard_Integer IsInternalFace(const TopoDS_Face & theFace, const TopoDS_Edge & theEdge, TopTools_ListOfShape & theLF, const opencascade::handle<IntTools_Context> & theContext);

		/****************** IsInternalFace ******************/
		%feature("compactdefaultargs") IsInternalFace;
		%feature("autodoc", "Returns true if the face theface is inside the solid thesolid. themef - map edge/faces for thesolid thetol - value of precision of computation thecontext- cahed geometrical tools.

Parameters
----------
theFace: TopoDS_Face
theSolid: TopoDS_Solid
theMEF: TopTools_IndexedDataMapOfShapeListOfShape
theTol: float
theContext: IntTools_Context

Returns
-------
bool
") IsInternalFace;
		static Standard_Boolean IsInternalFace(const TopoDS_Face & theFace, const TopoDS_Solid & theSolid, TopTools_IndexedDataMapOfShapeListOfShape & theMEF, const Standard_Real theTol, const opencascade::handle<IntTools_Context> & theContext);

		/****************** IsInvertedSolid ******************/
		%feature("compactdefaultargs") IsInvertedSolid;
		%feature("autodoc", "Returns true if the solid <thesolid> is inverted.

Parameters
----------
theSolid: TopoDS_Solid

Returns
-------
bool
") IsInvertedSolid;
		static Standard_Boolean IsInvertedSolid(const TopoDS_Solid & theSolid);

		/****************** IsMicroEdge ******************/
		%feature("compactdefaultargs") IsMicroEdge;
		%feature("autodoc", "Checks if it is possible to compute shrunk range for the edge <ae> flag <thechecksplittable> defines whether to take into account the possibility to split the edge or not.

Parameters
----------
theEdge: TopoDS_Edge
theContext: IntTools_Context
theCheckSplittable: bool,optional
	default value is Standard_True

Returns
-------
bool
") IsMicroEdge;
		static Standard_Boolean IsMicroEdge(const TopoDS_Edge & theEdge, const opencascade::handle<IntTools_Context> & theContext, const Standard_Boolean theCheckSplittable = Standard_True);

		/****************** IsOpenShell ******************/
		%feature("compactdefaultargs") IsOpenShell;
		%feature("autodoc", "Returns true if the shell <theshell> is open.

Parameters
----------
theShell: TopoDS_Shell

Returns
-------
bool
") IsOpenShell;
		static Standard_Boolean IsOpenShell(const TopoDS_Shell & theShell);

		/****************** IsSplitToReverse ******************/
		%feature("compactdefaultargs") IsSplitToReverse;
		%feature("autodoc", "Checks if the direction of the split shape is opposite to the direction of the original shape. the method is an overload for (edge,edge) and (face,face) corresponding methods and checks only these types of shapes. for faces the method checks if normal directions are opposite. for edges the method checks if tangent vectors are opposite. //! in case the directions do not coincide, it returns true, meaning that split shape has to be reversed to match the direction of the original shape. //! if requested (<theerror> is not null), the method returns the status of the operation: - 0 - no error; - error from (edge,edge) or (face,face) corresponding method - 100 - bad types. in case of any error the method always returns false. //! @param thesplit [in] split shape @param theshape [in] original shape @param thecontext [in] cashed geometrical tools @param theerror [out] error status of the operation.

Parameters
----------
theSplit: TopoDS_Shape
theShape: TopoDS_Shape
theContext: IntTools_Context
theError: int *,optional
	default value is NULL

Returns
-------
bool
") IsSplitToReverse;
		static Standard_Boolean IsSplitToReverse(const TopoDS_Shape & theSplit, const TopoDS_Shape & theShape, const opencascade::handle<IntTools_Context> & theContext, Standard_Integer * theError = NULL);

		/****************** IsSplitToReverse ******************/
		%feature("compactdefaultargs") IsSplitToReverse;
		%feature("autodoc", "Checks if the normal direction of the split face is opposite to the normal direction of the original face. the normal directions for both faces are taken in the same point - point inside the split face is projected onto the original face. returns true if the normals do not coincide, meaning the necessity to revert the orientation of the split face to match the direction of the original face. //! if requested (<theerror> is not null), the method returns the status of the operation: - 0 - no error; - 1 - unable to find the point inside split face; - 2 - unable to compute the normal for the split face; - 3 - unable to project the point inside the split face on the original face; - 4 - unable to compute the normal for the original face. in case of any error the method always returns false. //! @param thesplit [in] split face @param theshape [in] original face @param thecontext [in] cashed geometrical tools @param theerror [out] error status of the operation.

Parameters
----------
theSplit: TopoDS_Face
theShape: TopoDS_Face
theContext: IntTools_Context
theError: int *,optional
	default value is NULL

Returns
-------
bool
") IsSplitToReverse;
		static Standard_Boolean IsSplitToReverse(const TopoDS_Face & theSplit, const TopoDS_Face & theShape, const opencascade::handle<IntTools_Context> & theContext, Standard_Integer * theError = NULL);

		/****************** IsSplitToReverse ******************/
		%feature("compactdefaultargs") IsSplitToReverse;
		%feature("autodoc", "Checks if the tangent vector of the split edge is opposite to the tangent vector of the original edge. the tangent vectors for both edges are computed in the same point - point inside the split edge is projected onto the original edge. returns true if the tangent vectors do not coincide, meaning the necessity to revert the orientation of the split edge to match the direction of the original edge. //! if requested (<theerror> is not null), the method returns the status of the operation: - 0 - no error; - 1 - degenerated edges are given; - 2 - unable to compute the tangent vector for the split edge; - 3 - unable to project the point inside the split edge on the original edge; - 4 - unable to compute the tangent vector for the original edge; in case of any error the method always returns false. //! @param thesplit [in] split edge @param theshape [in] original edge @param thecontext [in] cashed geometrical tools @param theerror [out] error status of the operation.

Parameters
----------
theSplit: TopoDS_Edge
theShape: TopoDS_Edge
theContext: IntTools_Context
theError: int *,optional
	default value is NULL

Returns
-------
bool
") IsSplitToReverse;
		static Standard_Boolean IsSplitToReverse(const TopoDS_Edge & theSplit, const TopoDS_Edge & theShape, const opencascade::handle<IntTools_Context> & theContext, Standard_Integer * theError = NULL);

		/****************** IsSplitToReverseWithWarn ******************/
		%feature("compactdefaultargs") IsSplitToReverseWithWarn;
		%feature("autodoc", "Add-on for the *issplittoreverse()* to check for its errors and in case of any add the *bopalgo_alertunabletoorienttheshape* warning to the report.

Parameters
----------
theSplit: TopoDS_Shape
theShape: TopoDS_Shape
theContext: IntTools_Context
theReport: Message_Report,optional
	default value is NULL

Returns
-------
bool
") IsSplitToReverseWithWarn;
		static Standard_Boolean IsSplitToReverseWithWarn(const TopoDS_Shape & theSplit, const TopoDS_Shape & theShape, const opencascade::handle<IntTools_Context> & theContext, const opencascade::handle<Message_Report> & theReport = NULL);

		/****************** MakeConnexityBlock ******************/
		%feature("compactdefaultargs") MakeConnexityBlock;
		%feature("autodoc", "For the list of faces thels build block thelscb in terms of connexity by edges themapavoid - set of edges to avoid for the treatment.

Parameters
----------
theLS: TopTools_ListOfShape
theMapAvoid: TopTools_IndexedMapOfShape
theLSCB: TopTools_ListOfShape
theAllocator: NCollection_BaseAllocator

Returns
-------
None
") MakeConnexityBlock;
		static void MakeConnexityBlock(TopTools_ListOfShape & theLS, TopTools_IndexedMapOfShape & theMapAvoid, TopTools_ListOfShape & theLSCB, const opencascade::handle<NCollection_BaseAllocator> & theAllocator);

		/****************** MakeConnexityBlocks ******************/
		%feature("compactdefaultargs") MakeConnexityBlocks;
		%feature("autodoc", "For the compound <thes> builds the blocks (compounds) of elements of type <theelementtype> connected through the shapes of the type <theconnectiontype>. the blocks are stored into the list <thelcb>.

Parameters
----------
theS: TopoDS_Shape
theConnectionType: TopAbs_ShapeEnum
theElementType: TopAbs_ShapeEnum
theLCB: TopTools_ListOfShape

Returns
-------
None
") MakeConnexityBlocks;
		static void MakeConnexityBlocks(const TopoDS_Shape & theS, const TopAbs_ShapeEnum theConnectionType, const TopAbs_ShapeEnum theElementType, TopTools_ListOfShape & theLCB);

		/****************** MakeConnexityBlocks ******************/
		%feature("compactdefaultargs") MakeConnexityBlocks;
		%feature("autodoc", "For the compound <thes> builds the blocks (compounds) of elements of type <theelementtype> connected through the shapes of the type <theconnectiontype>. the blocks are stored into the list of lists <thelcb>. returns also the connection map <theconnectionmap>, filled during operation.

Parameters
----------
theS: TopoDS_Shape
theConnectionType: TopAbs_ShapeEnum
theElementType: TopAbs_ShapeEnum
theLCB: TopTools_ListOfListOfShape
theConnectionMap: TopTools_IndexedDataMapOfShapeListOfShape

Returns
-------
None
") MakeConnexityBlocks;
		static void MakeConnexityBlocks(const TopoDS_Shape & theS, const TopAbs_ShapeEnum theConnectionType, const TopAbs_ShapeEnum theElementType, TopTools_ListOfListOfShape & theLCB, TopTools_IndexedDataMapOfShapeListOfShape & theConnectionMap);

		/****************** MakeConnexityBlocks ******************/
		%feature("compactdefaultargs") MakeConnexityBlocks;
		%feature("autodoc", "Makes connexity blocks of elements of the given type with the given type of the connecting elements. the blocks are checked on regularity (multi-connectivity) and stored to the list of blocks <thelcb>.

Parameters
----------
theLS: TopTools_ListOfShape
theConnectionType: TopAbs_ShapeEnum
theElementType: TopAbs_ShapeEnum
theLCB: BOPTools_ListOfConnexityBlock

Returns
-------
None
") MakeConnexityBlocks;
		static void MakeConnexityBlocks(const TopTools_ListOfShape & theLS, const TopAbs_ShapeEnum theConnectionType, const TopAbs_ShapeEnum theElementType, BOPTools_ListOfConnexityBlock & theLCB);

		/****************** MakeContainer ******************/
		%feature("compactdefaultargs") MakeContainer;
		%feature("autodoc", "Makes empty container of requested type.

Parameters
----------
theType: TopAbs_ShapeEnum
theShape: TopoDS_Shape

Returns
-------
None
") MakeContainer;
		static void MakeContainer(const TopAbs_ShapeEnum theType, TopoDS_Shape & theShape);

		/****************** MakeEdge ******************/
		%feature("compactdefaultargs") MakeEdge;
		%feature("autodoc", "Makes the edge based on the given curve with given bounding vertices.

Parameters
----------
theCurve: IntTools_Curve
theV1: TopoDS_Vertex
theT1: float
theV2: TopoDS_Vertex
theT2: float
theTolR3D: float
theE: TopoDS_Edge

Returns
-------
None
") MakeEdge;
		static void MakeEdge(const IntTools_Curve & theCurve, const TopoDS_Vertex & theV1, const Standard_Real theT1, const TopoDS_Vertex & theV2, const Standard_Real theT2, const Standard_Real theTolR3D, TopoDS_Edge & theE);

		/****************** MakeNewVertex ******************/
		%feature("compactdefaultargs") MakeNewVertex;
		%feature("autodoc", "Make a vertex using 3d-point <ap1> and 3d-tolerance value <atol>.

Parameters
----------
aP1: gp_Pnt
aTol: float
aNewVertex: TopoDS_Vertex

Returns
-------
None
") MakeNewVertex;
		static void MakeNewVertex(const gp_Pnt & aP1, const Standard_Real aTol, TopoDS_Vertex & aNewVertex);

		/****************** MakeNewVertex ******************/
		%feature("compactdefaultargs") MakeNewVertex;
		%feature("autodoc", "Make a vertex using couple of vertices <av1, av2>.

Parameters
----------
aV1: TopoDS_Vertex
aV2: TopoDS_Vertex
aNewVertex: TopoDS_Vertex

Returns
-------
None
") MakeNewVertex;
		static void MakeNewVertex(const TopoDS_Vertex & aV1, const TopoDS_Vertex & aV2, TopoDS_Vertex & aNewVertex);

		/****************** MakeNewVertex ******************/
		%feature("compactdefaultargs") MakeNewVertex;
		%feature("autodoc", "Make a vertex in place of intersection between two edges <ae1, ae2> with parameters <ap1, ap2>.

Parameters
----------
aE1: TopoDS_Edge
aP1: float
aE2: TopoDS_Edge
aP2: float
aNewVertex: TopoDS_Vertex

Returns
-------
None
") MakeNewVertex;
		static void MakeNewVertex(const TopoDS_Edge & aE1, const Standard_Real aP1, const TopoDS_Edge & aE2, const Standard_Real aP2, TopoDS_Vertex & aNewVertex);

		/****************** MakeNewVertex ******************/
		%feature("compactdefaultargs") MakeNewVertex;
		%feature("autodoc", "Make a vertex in place of intersection between the edge <ae1> with parameter <ap1> and the face <af2>.

Parameters
----------
aE1: TopoDS_Edge
aP1: float
aF2: TopoDS_Face
aNewVertex: TopoDS_Vertex

Returns
-------
None
") MakeNewVertex;
		static void MakeNewVertex(const TopoDS_Edge & aE1, const Standard_Real aP1, const TopoDS_Face & aF2, TopoDS_Vertex & aNewVertex);

		/****************** MakePCurve ******************/
		%feature("compactdefaultargs") MakePCurve;
		%feature("autodoc", "Makes 2d curve of the edge <thee> on the faces <thef1> and <thef2>. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
theE: TopoDS_Edge
theF1: TopoDS_Face
theF2: TopoDS_Face
theCurve: IntTools_Curve
thePC1: bool
thePC2: bool
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
None
") MakePCurve;
		static void MakePCurve(const TopoDS_Edge & theE, const TopoDS_Face & theF1, const TopoDS_Face & theF2, const IntTools_Curve & theCurve, const Standard_Boolean thePC1, const Standard_Boolean thePC2, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** MakeSectEdge ******************/
		%feature("compactdefaultargs") MakeSectEdge;
		%feature("autodoc", "Make the edge from 3d-curve <aic> and two vertices <av1,av2> at parameters <ap1,ap2>.

Parameters
----------
aIC: IntTools_Curve
aV1: TopoDS_Vertex
aP1: float
aV2: TopoDS_Vertex
aP2: float
aNewEdge: TopoDS_Edge

Returns
-------
None
") MakeSectEdge;
		static void MakeSectEdge(const IntTools_Curve & aIC, const TopoDS_Vertex & aV1, const Standard_Real aP1, const TopoDS_Vertex & aV2, const Standard_Real aP2, TopoDS_Edge & aNewEdge);

		/****************** MakeSplitEdge ******************/
		%feature("compactdefaultargs") MakeSplitEdge;
		%feature("autodoc", "Make the edge from base edge <ae1> and two vertices <av1,av2> at parameters <ap1,ap2>.

Parameters
----------
aE1: TopoDS_Edge
aV1: TopoDS_Vertex
aP1: float
aV2: TopoDS_Vertex
aP2: float
aNewEdge: TopoDS_Edge

Returns
-------
None
") MakeSplitEdge;
		static void MakeSplitEdge(const TopoDS_Edge & aE1, const TopoDS_Vertex & aV1, const Standard_Real aP1, const TopoDS_Vertex & aV2, const Standard_Real aP2, TopoDS_Edge & aNewEdge);

		/****************** MakeVertex ******************/
		%feature("compactdefaultargs") MakeVertex;
		%feature("autodoc", "Makes the vertex in the middle of given vertices with the tolerance covering all tolerance spheres of vertices.

Parameters
----------
theLV: TopTools_ListOfShape
theV: TopoDS_Vertex

Returns
-------
None
") MakeVertex;
		static void MakeVertex(const TopTools_ListOfShape & theLV, TopoDS_Vertex & theV);

		/****************** OrientEdgesOnWire ******************/
		%feature("compactdefaultargs") OrientEdgesOnWire;
		%feature("autodoc", "Correctly orients edges on the wire.

Parameters
----------
theWire: TopoDS_Shape

Returns
-------
None
") OrientEdgesOnWire;
		static void OrientEdgesOnWire(TopoDS_Shape & theWire);

		/****************** OrientFacesOnShell ******************/
		%feature("compactdefaultargs") OrientFacesOnShell;
		%feature("autodoc", "Correctly orients faces on the shell.

Parameters
----------
theShell: TopoDS_Shape

Returns
-------
None
") OrientFacesOnShell;
		static void OrientFacesOnShell(TopoDS_Shape & theShell);

		/****************** PointOnEdge ******************/
		%feature("compactdefaultargs") PointOnEdge;
		%feature("autodoc", "Compute a 3d-point on the edge <aedge> at parameter <aprm>.

Parameters
----------
aEdge: TopoDS_Edge
aPrm: float
aP: gp_Pnt

Returns
-------
None
") PointOnEdge;
		static void PointOnEdge(const TopoDS_Edge & aEdge, const Standard_Real aPrm, gp_Pnt & aP);

		/****************** Sense ******************/
		%feature("compactdefaultargs") Sense;
		%feature("autodoc", "Checks if the normals direction of the given faces computed near the shared edge coincide. returns the status of operation: * 0 - in case of error (shared edge not found or directions are not collinear) * 1 - normal directions coincide; * -1 - normal directions are opposite.

Parameters
----------
theF1: TopoDS_Face
theF2: TopoDS_Face
theContext: IntTools_Context

Returns
-------
int
") Sense;
		static Standard_Integer Sense(const TopoDS_Face & theF1, const TopoDS_Face & theF2, const opencascade::handle<IntTools_Context> & theContext);

		/****************** UpdateVertex ******************/
		%feature("compactdefaultargs") UpdateVertex;
		%feature("autodoc", "Update the tolerance value for vertex <av> taking into account the fact that <av> lays on the curve <aic>.

Parameters
----------
aIC: IntTools_Curve
aT: float
aV: TopoDS_Vertex

Returns
-------
None
") UpdateVertex;
		static void UpdateVertex(const IntTools_Curve & aIC, const Standard_Real aT, const TopoDS_Vertex & aV);

		/****************** UpdateVertex ******************/
		%feature("compactdefaultargs") UpdateVertex;
		%feature("autodoc", "Update the tolerance value for vertex <av> taking into account the fact that <av> lays on the edge <ae>.

Parameters
----------
aE: TopoDS_Edge
aT: float
aV: TopoDS_Vertex

Returns
-------
None
") UpdateVertex;
		static void UpdateVertex(const TopoDS_Edge & aE, const Standard_Real aT, const TopoDS_Vertex & aV);

		/****************** UpdateVertex ******************/
		%feature("compactdefaultargs") UpdateVertex;
		%feature("autodoc", "Update the tolerance value for vertex <avn> taking into account the fact that <avn> should cover tolerance zone of <avf>.

Parameters
----------
aVF: TopoDS_Vertex
aVN: TopoDS_Vertex

Returns
-------
None
") UpdateVertex;
		static void UpdateVertex(const TopoDS_Vertex & aVF, const TopoDS_Vertex & aVN);

};


%extend BOPTools_AlgoTools {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BOPTools_AlgoTools2D *
*****************************/
class BOPTools_AlgoTools2D {
	public:
		/****************** AdjustPCurveOnFace ******************/
		%feature("compactdefaultargs") AdjustPCurveOnFace;
		%feature("autodoc", "Adjust p-curve <thec2d> (3d-curve <thec3d>) on surface of the face <thef>. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
theF: TopoDS_Face
theC3D: Geom_Curve
theC2D: Geom2d_Curve
theC2DA: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
None
") AdjustPCurveOnFace;
		static void AdjustPCurveOnFace(const TopoDS_Face & theF, const opencascade::handle<Geom_Curve> & theC3D, const opencascade::handle<Geom2d_Curve> & theC2D, opencascade::handle<Geom2d_Curve> & theC2DA, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** AdjustPCurveOnFace ******************/
		%feature("compactdefaultargs") AdjustPCurveOnFace;
		%feature("autodoc", "Adjust p-curve <ac2d> (3d-curve <c3d>) on surface <af> . [at1, at2] - range to adjust <thecontext> - storage for caching the geometrical tools.

Parameters
----------
theF: TopoDS_Face
theFirst: float
theLast: float
theC2D: Geom2d_Curve
theC2DA: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
None
") AdjustPCurveOnFace;
		static void AdjustPCurveOnFace(const TopoDS_Face & theF, const Standard_Real theFirst, const Standard_Real theLast, const opencascade::handle<Geom2d_Curve> & theC2D, opencascade::handle<Geom2d_Curve> & theC2DA, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** AdjustPCurveOnSurf ******************/
		%feature("compactdefaultargs") AdjustPCurveOnSurf;
		%feature("autodoc", "Adjust p-curve <ac2d> (3d-curve <c3d>) on surface <af> . [at1, at2] - range to adjust.

Parameters
----------
aF: BRepAdaptor_Surface
aT1: float
aT2: float
aC2D: Geom2d_Curve
aC2DA: Geom2d_Curve

Returns
-------
None
") AdjustPCurveOnSurf;
		static void AdjustPCurveOnSurf(const BRepAdaptor_Surface & aF, const Standard_Real aT1, const Standard_Real aT2, const opencascade::handle<Geom2d_Curve> & aC2D, opencascade::handle<Geom2d_Curve> & aC2DA);

		/****************** AttachExistingPCurve ******************/
		%feature("compactdefaultargs") AttachExistingPCurve;
		%feature("autodoc", "Attach p-curve from the edge <aeold> on surface <af> to the edge <aenew> returns 0 in case of success.

Parameters
----------
aEold: TopoDS_Edge
aEnew: TopoDS_Edge
aF: TopoDS_Face
aCtx: IntTools_Context

Returns
-------
int
") AttachExistingPCurve;
		static Standard_Integer AttachExistingPCurve(const TopoDS_Edge & aEold, const TopoDS_Edge & aEnew, const TopoDS_Face & aF, const opencascade::handle<IntTools_Context> & aCtx);

		/****************** BuildPCurveForEdgeOnFace ******************/
		%feature("compactdefaultargs") BuildPCurveForEdgeOnFace;
		%feature("autodoc", "Compute p-curve for the edge <ae> on the face <af>. raises exception standard_constructionerror if projection algorithm fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
None
") BuildPCurveForEdgeOnFace;
		static void BuildPCurveForEdgeOnFace(const TopoDS_Edge & aE, const TopoDS_Face & aF, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** CurveOnSurface ******************/
		%feature("compactdefaultargs") CurveOnSurface;
		%feature("autodoc", "Get p-curve <ac> for the edge <ae> on surface <af> . if the p-curve does not exist, build it using make2d(). [atoler] - reached tolerance raises exception standard_constructionerror if algorithm make2d() fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aC: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
aToler: float
") CurveOnSurface;
		static void CurveOnSurface(const TopoDS_Edge & aE, const TopoDS_Face & aF, opencascade::handle<Geom2d_Curve> & aC, Standard_Real &OutValue, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** CurveOnSurface ******************/
		%feature("compactdefaultargs") CurveOnSurface;
		%feature("autodoc", "Get p-curve <ac> for the edge <ae> on surface <af> . if the p-curve does not exist, build it using make2d(). [afirst, alast] - range of the p-curve [atoler] - reached tolerance raises exception standard_constructionerror if algorithm make2d() fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aC: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
aFirst: float
aLast: float
aToler: float
") CurveOnSurface;
		static void CurveOnSurface(const TopoDS_Edge & aE, const TopoDS_Face & aF, opencascade::handle<Geom2d_Curve> & aC, Standard_Real &OutValue, Standard_Real &OutValue, Standard_Real &OutValue, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** EdgeTangent ******************/
		%feature("compactdefaultargs") EdgeTangent;
		%feature("autodoc", "Compute tangent for the edge <ae> [in 3d] at parameter <at>.

Parameters
----------
anE: TopoDS_Edge
aT: float
Tau: gp_Vec

Returns
-------
bool
") EdgeTangent;
		static Standard_Boolean EdgeTangent(const TopoDS_Edge & anE, const Standard_Real aT, gp_Vec & Tau);

		/****************** HasCurveOnSurface ******************/
		%feature("compactdefaultargs") HasCurveOnSurface;
		%feature("autodoc", "Returns true if the edge <ae> has p-curve <ac> on surface <af> . [afirst, alast] - range of the p-curve [atoler] - reached tolerance if the p-curve does not exist, ac.isnull()=true.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aC: Geom2d_Curve

Returns
-------
aFirst: float
aLast: float
aToler: float
") HasCurveOnSurface;
		static Standard_Boolean HasCurveOnSurface(const TopoDS_Edge & aE, const TopoDS_Face & aF, opencascade::handle<Geom2d_Curve> & aC, Standard_Real &OutValue, Standard_Real &OutValue, Standard_Real &OutValue);

		/****************** HasCurveOnSurface ******************/
		%feature("compactdefaultargs") HasCurveOnSurface;
		%feature("autodoc", "Returns true if the edge <ae> has p-curve <ac> on surface <af> . if the p-curve does not exist, ac.isnull()=true.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face

Returns
-------
bool
") HasCurveOnSurface;
		static Standard_Boolean HasCurveOnSurface(const TopoDS_Edge & aE, const TopoDS_Face & aF);

		/****************** IntermediatePoint ******************/
		%feature("compactdefaultargs") IntermediatePoint;
		%feature("autodoc", "Compute intermediate value in between [afirst, alast] .

Parameters
----------
aFirst: float
aLast: float

Returns
-------
float
") IntermediatePoint;
		static Standard_Real IntermediatePoint(const Standard_Real aFirst, const Standard_Real aLast);

		/****************** IntermediatePoint ******************/
		%feature("compactdefaultargs") IntermediatePoint;
		%feature("autodoc", "Compute intermediate value of parameter for the edge <ane>.

Parameters
----------
anE: TopoDS_Edge

Returns
-------
float
") IntermediatePoint;
		static Standard_Real IntermediatePoint(const TopoDS_Edge & anE);

		/****************** IsEdgeIsoline ******************/
		%feature("compactdefaultargs") IsEdgeIsoline;
		%feature("autodoc", "Checks if curveonsurface of thee on thef matches with isoline of thef surface. sets corresponding values for istheuiso and istheviso variables. attention!!! this method is based on comparation between direction of surface (which thef is based on) iso-lines and the direction of the edge p-curve (on thef) in middle-point of the p-curve. this method should be used carefully (e.g. brep_tool::isclosed(...) together) in order to avoid false classification some p-curves as isoline (e.g. circle on a plane).

Parameters
----------
theE: TopoDS_Edge
theF: TopoDS_Face

Returns
-------
isTheUIso: bool
isTheVIso: bool
") IsEdgeIsoline;
		static void IsEdgeIsoline(const TopoDS_Edge & theE, const TopoDS_Face & theF, Standard_Boolean &OutValue, Standard_Boolean &OutValue);

		/****************** Make2D ******************/
		%feature("compactdefaultargs") Make2D;
		%feature("autodoc", "Make p-curve <ac> for the edge <ae> on surface <af> . [afirst, alast] - range of the p-curve [atoler] - reached tolerance raises exception standard_constructionerror if algorithm fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aC: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
aFirst: float
aLast: float
aToler: float
") Make2D;
		static void Make2D(const TopoDS_Edge & aE, const TopoDS_Face & aF, opencascade::handle<Geom2d_Curve> & aC, Standard_Real &OutValue, Standard_Real &OutValue, Standard_Real &OutValue, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** MakePCurveOnFace ******************/
		%feature("compactdefaultargs") MakePCurveOnFace;
		%feature("autodoc", "Make p-curve <ac> for the 3d-curve <c3d> on surface <af> . [atoler] - reached tolerance raises exception standard_constructionerror if projection algorithm fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aF: TopoDS_Face
C3D: Geom_Curve
aC: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
aToler: float
") MakePCurveOnFace;
		static void MakePCurveOnFace(const TopoDS_Face & aF, const opencascade::handle<Geom_Curve> & C3D, opencascade::handle<Geom2d_Curve> & aC, Standard_Real &OutValue, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** MakePCurveOnFace ******************/
		%feature("compactdefaultargs") MakePCurveOnFace;
		%feature("autodoc", "Make p-curve <ac> for the 3d-curve <c3d> on surface <af> . [at1, at2] - range to build [atoler] - reached tolerance raises exception standard_constructionerror if projection algorithm fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aF: TopoDS_Face
C3D: Geom_Curve
aT1: float
aT2: float
aC: Geom2d_Curve
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
aToler: float
") MakePCurveOnFace;
		static void MakePCurveOnFace(const TopoDS_Face & aF, const opencascade::handle<Geom_Curve> & C3D, const Standard_Real aT1, const Standard_Real aT2, opencascade::handle<Geom2d_Curve> & aC, Standard_Real &OutValue, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** PointOnSurface ******************/
		%feature("compactdefaultargs") PointOnSurface;
		%feature("autodoc", "Compute surface parameters <u,v> of the face <af> for the point from the edge <ae> at parameter <at>. if <ae> has't pcurve on surface, algorithm tries to get it by projection and can raise exception standard_constructionerror if projection algorithm fails. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aT: float
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
U: float
V: float
") PointOnSurface;
		static void PointOnSurface(const TopoDS_Edge & aE, const TopoDS_Face & aF, const Standard_Real aT, Standard_Real &OutValue, Standard_Real &OutValue, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

};


%extend BOPTools_AlgoTools2D {
	%pythoncode {
	__repr__ = _dumps_object

	@methodnotwrapped
	def MakeCurveOnSurface(self):
		pass
	}
};

/*****************************
* class BOPTools_AlgoTools3D *
*****************************/
class BOPTools_AlgoTools3D {
	public:
		/****************** DoSplitSEAMOnFace ******************/
		%feature("compactdefaultargs") DoSplitSEAMOnFace;
		%feature("autodoc", "Make the edge <asp> seam edge for the face <af>.

Parameters
----------
aSp: TopoDS_Edge
aF: TopoDS_Face

Returns
-------
None
") DoSplitSEAMOnFace;
		static void DoSplitSEAMOnFace(const TopoDS_Edge & aSp, const TopoDS_Face & aF);

		/****************** GetApproxNormalToFaceOnEdge ******************/
		%feature("compactdefaultargs") GetApproxNormalToFaceOnEdge;
		%feature("autodoc", "Computes normal to the face <af> for the 3d-point that belongs to the edge <ae> at parameter <at>. output: apx - the 3d-point where the normal computed ad - the normal; warning: the normal is computed not exactly in the point on the edge, but in point that is near to the edge towards to the face material (so, we'll have approx. normal); the point is computed using pointnearedge function, with the shifting value boptools_algotools3d::minstepin2d(), from the edge, but if this value is too big, the point will be computed using hatcher (pointinface function). returns true in case of success.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aT: float
aPx: gp_Pnt
aD: gp_Dir
theContext: IntTools_Context

Returns
-------
bool
") GetApproxNormalToFaceOnEdge;
		static Standard_Boolean GetApproxNormalToFaceOnEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, const Standard_Real aT, gp_Pnt & aPx, gp_Dir & aD, const opencascade::handle<IntTools_Context> & theContext);

		/****************** GetApproxNormalToFaceOnEdge ******************/
		%feature("compactdefaultargs") GetApproxNormalToFaceOnEdge;
		%feature("autodoc", "Computes normal to the face <af> for the 3d-point that belongs to the edge <ae> at parameter <at>. output: apx - the 3d-point where the normal computed ad - the normal; warning: the normal is computed not exactly in the point on the edge, but in point that is near to the edge towards to the face material (so, we'll have approx. normal); the point is computed using pointnearedge function with the shifting value <adt2d> from the edge; no checks on this value will be done. returns true in case of success.

Parameters
----------
theE: TopoDS_Edge
theF: TopoDS_Face
aT: float
aP: gp_Pnt
aDNF: gp_Dir
aDt2D: float

Returns
-------
bool
") GetApproxNormalToFaceOnEdge;
		static Standard_Boolean GetApproxNormalToFaceOnEdge(const TopoDS_Edge & theE, const TopoDS_Face & theF, const Standard_Real aT, gp_Pnt & aP, gp_Dir & aDNF, const Standard_Real aDt2D);

		/****************** GetApproxNormalToFaceOnEdge ******************/
		%feature("compactdefaultargs") GetApproxNormalToFaceOnEdge;
		%feature("autodoc", "Computes normal to the face <af> for the 3d-point that belongs to the edge <ae> at parameter <at>. output: apx - the 3d-point where the normal computed ad - the normal; warning: the normal is computed not exactly in the point on the edge, but in point that is near to the edge towards to the face material (so, we'll have approx. normal); the point is computed using pointnearedge function with the shifting value <adt2d> from the edge, but if this value is too big the point will be computed using hatcher (pointinface function). returns true in case of success.

Parameters
----------
theE: TopoDS_Edge
theF: TopoDS_Face
aT: float
aDt2D: float
aP: gp_Pnt
aDNF: gp_Dir
theContext: IntTools_Context

Returns
-------
bool
") GetApproxNormalToFaceOnEdge;
		static Standard_Boolean GetApproxNormalToFaceOnEdge(const TopoDS_Edge & theE, const TopoDS_Face & theF, const Standard_Real aT, const Standard_Real aDt2D, gp_Pnt & aP, gp_Dir & aDNF, const opencascade::handle<IntTools_Context> & theContext);

		/****************** GetNormalToFaceOnEdge ******************/
		%feature("compactdefaultargs") GetNormalToFaceOnEdge;
		%feature("autodoc", "Computes normal to the face <af> for the point on the edge <ae> at parameter <at>. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aT: float
aD: gp_Dir
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
None
") GetNormalToFaceOnEdge;
		static void GetNormalToFaceOnEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, const Standard_Real aT, gp_Dir & aD, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** GetNormalToFaceOnEdge ******************/
		%feature("compactdefaultargs") GetNormalToFaceOnEdge;
		%feature("autodoc", "Computes normal to the face <af> for the point on the edge <ae> at arbitrary intermediate parameter. <thecontext> - storage for caching the geometrical tools.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aD: gp_Dir
theContext: IntTools_Context,optional
	default value is opencascade::handle<IntTools_Context>()

Returns
-------
None
") GetNormalToFaceOnEdge;
		static void GetNormalToFaceOnEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, gp_Dir & aD, const opencascade::handle<IntTools_Context> & theContext = opencascade::handle<IntTools_Context>());

		/****************** GetNormalToSurface ******************/
		%feature("compactdefaultargs") GetNormalToSurface;
		%feature("autodoc", "Compute normal <ad> to surface <as> in point (u,v) returns true if directions ad1u, ad1v coincide.

Parameters
----------
aS: Geom_Surface
U: float
V: float
aD: gp_Dir

Returns
-------
bool
") GetNormalToSurface;
		static Standard_Boolean GetNormalToSurface(const opencascade::handle<Geom_Surface> & aS, const Standard_Real U, const Standard_Real V, gp_Dir & aD);

		/****************** IsEmptyShape ******************/
		%feature("compactdefaultargs") IsEmptyShape;
		%feature("autodoc", "Returns true if the shape <as> does not contain geometry information (e.g. empty compound).

Parameters
----------
aS: TopoDS_Shape

Returns
-------
bool
") IsEmptyShape;
		static Standard_Boolean IsEmptyShape(const TopoDS_Shape & aS);

		/****************** MinStepIn2d ******************/
		%feature("compactdefaultargs") MinStepIn2d;
		%feature("autodoc", "Returns simple step value that is used in 2d-computations = 1.e-5.

Returns
-------
float
") MinStepIn2d;
		static Standard_Real MinStepIn2d();

		/****************** OrientEdgeOnFace ******************/
		%feature("compactdefaultargs") OrientEdgeOnFace;
		%feature("autodoc", "Get the edge <aer> from the face <af> that is the same as the edge <ae>.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aER: TopoDS_Edge

Returns
-------
None
") OrientEdgeOnFace;
		static void OrientEdgeOnFace(const TopoDS_Edge & aE, const TopoDS_Face & aF, TopoDS_Edge & aER);

		/****************** PointInFace ******************/
		%feature("compactdefaultargs") PointInFace;
		%feature("autodoc", "Computes arbitrary point <thep> inside the face <thef>. <thep2d> - 2d representation of <thep> on the surface of <thef> returns 0 in case of success.

Parameters
----------
theF: TopoDS_Face
theP: gp_Pnt
theP2D: gp_Pnt2d
theContext: IntTools_Context

Returns
-------
int
") PointInFace;
		static Standard_Integer PointInFace(const TopoDS_Face & theF, gp_Pnt & theP, gp_Pnt2d & theP2D, const opencascade::handle<IntTools_Context> & theContext);

		/****************** PointInFace ******************/
		%feature("compactdefaultargs") PointInFace;
		%feature("autodoc", "Computes a point <thep> inside the face <thef> using starting point taken by the parameter <thet> from the 2d curve of the edge <thee> on the face <thef> in the direction perpendicular to the tangent vector of the 2d curve of the edge. the point will be distanced on <thedt2d> from the 2d curve. <thep2d> - 2d representation of <thep> on the surface of <thef> returns 0 in case of success.

Parameters
----------
theF: TopoDS_Face
theE: TopoDS_Edge
theT: float
theDt2D: float
theP: gp_Pnt
theP2D: gp_Pnt2d
theContext: IntTools_Context

Returns
-------
int
") PointInFace;
		static Standard_Integer PointInFace(const TopoDS_Face & theF, const TopoDS_Edge & theE, const Standard_Real theT, const Standard_Real theDt2D, gp_Pnt & theP, gp_Pnt2d & theP2D, const opencascade::handle<IntTools_Context> & theContext);

		/****************** PointInFace ******************/
		%feature("compactdefaultargs") PointInFace;
		%feature("autodoc", "Computes a point <thep> inside the face <thef> using the line <thel> so that 2d point <thep2d>, 2d representation of <thep> on the surface of <thef>, lies on that line. returns 0 in case of success.

Parameters
----------
theF: TopoDS_Face
theL: Geom2d_Curve
theP: gp_Pnt
theP2D: gp_Pnt2d
theContext: IntTools_Context
theDt2D: float,optional
	default value is 0.0

Returns
-------
int
") PointInFace;
		static Standard_Integer PointInFace(const TopoDS_Face & theF, const opencascade::handle<Geom2d_Curve> & theL, gp_Pnt & theP, gp_Pnt2d & theP2D, const opencascade::handle<IntTools_Context> & theContext, const Standard_Real theDt2D = 0.0);

		/****************** PointNearEdge ******************/
		%feature("compactdefaultargs") PointNearEdge;
		%feature("autodoc", "Compute the point <apx>, (<ap2d>) that is near to the edge <ae> at parameter <at> towards to the material of the face <af>. the value of shifting in 2d is <adt2d> if the value of shifting is too big the point will be computed using hatcher (pointinface function). returns error status: 0 - in case of success; 1 - <ae> does not have 2d curve on the face <af>; 2 - the computed point is out of the face.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aT: float
aDt2D: float
aP2D: gp_Pnt2d
aPx: gp_Pnt
theContext: IntTools_Context

Returns
-------
int
") PointNearEdge;
		static Standard_Integer PointNearEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, const Standard_Real aT, const Standard_Real aDt2D, gp_Pnt2d & aP2D, gp_Pnt & aPx, const opencascade::handle<IntTools_Context> & theContext);

		/****************** PointNearEdge ******************/
		%feature("compactdefaultargs") PointNearEdge;
		%feature("autodoc", "Compute the point <apx>, (<ap2d>) that is near to the edge <ae> at parameter <at> towards to the material of the face <af>. the value of shifting in 2d is <adt2d>. no checks on this value will be done. returns error status: 0 - in case of success; 1 - <ae> does not have 2d curve on the face <af>.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aT: float
aDt2D: float
aP2D: gp_Pnt2d
aPx: gp_Pnt

Returns
-------
int
") PointNearEdge;
		static Standard_Integer PointNearEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, const Standard_Real aT, const Standard_Real aDt2D, gp_Pnt2d & aP2D, gp_Pnt & aPx);

		/****************** PointNearEdge ******************/
		%feature("compactdefaultargs") PointNearEdge;
		%feature("autodoc", "Computes the point <apx>, (<ap2d>) that is near to the edge <ae> at parameter <at> towards to the material of the face <af>. the value of shifting in 2d is dt2d=boptools_algotools3d::minstepin2d() if the value of shifting is too big the point will be computed using hatcher (pointinface function). returns error status: 0 - in case of success; 1 - <ae> does not have 2d curve on the face <af>; 2 - the computed point is out of the face.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aT: float
aP2D: gp_Pnt2d
aPx: gp_Pnt
theContext: IntTools_Context

Returns
-------
int
") PointNearEdge;
		static Standard_Integer PointNearEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, const Standard_Real aT, gp_Pnt2d & aP2D, gp_Pnt & aPx, const opencascade::handle<IntTools_Context> & theContext);

		/****************** PointNearEdge ******************/
		%feature("compactdefaultargs") PointNearEdge;
		%feature("autodoc", "Compute the point <apx>, (<ap2d>) that is near to the edge <ae> at arbitrary parameter towards to the material of the face <af>. the value of shifting in 2d is dt2d=boptools_algotools3d::minstepin2d(). if the value of shifting is too big the point will be computed using hatcher (pointinface function). returns error status: 0 - in case of success; 1 - <ae> does not have 2d curve on the face <af>; 2 - the computed point is out of the face.

Parameters
----------
aE: TopoDS_Edge
aF: TopoDS_Face
aP2D: gp_Pnt2d
aPx: gp_Pnt
theContext: IntTools_Context

Returns
-------
int
") PointNearEdge;
		static Standard_Integer PointNearEdge(const TopoDS_Edge & aE, const TopoDS_Face & aF, gp_Pnt2d & aP2D, gp_Pnt & aPx, const opencascade::handle<IntTools_Context> & theContext);

		/****************** SenseFlag ******************/
		%feature("compactdefaultargs") SenseFlag;
		%feature("autodoc", "Returns 1 if scalar product anf1* anf2>0. returns 0 if directions anf1 anf2 coincide returns -1 if scalar product anf1* anf2<0.

Parameters
----------
aNF1: gp_Dir
aNF2: gp_Dir

Returns
-------
int
") SenseFlag;
		static Standard_Integer SenseFlag(const gp_Dir & aNF1, const gp_Dir & aNF2);

};


%extend BOPTools_AlgoTools3D {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*****************************
* class BOPTools_BoxSelector *
*****************************/
/************************
* class BOPTools_BoxSet *
************************/
/********************************
* class BOPTools_ConnexityBlock *
********************************/
class BOPTools_ConnexityBlock {
	public:
		/****************** BOPTools_ConnexityBlock ******************/
		%feature("compactdefaultargs") BOPTools_ConnexityBlock;
		%feature("autodoc", "No available documentation.

Returns
-------
None
") BOPTools_ConnexityBlock;
		 BOPTools_ConnexityBlock();

		/****************** BOPTools_ConnexityBlock ******************/
		%feature("compactdefaultargs") BOPTools_ConnexityBlock;
		%feature("autodoc", "No available documentation.

Parameters
----------
theAllocator: NCollection_BaseAllocator

Returns
-------
None
") BOPTools_ConnexityBlock;
		 BOPTools_ConnexityBlock(const opencascade::handle<NCollection_BaseAllocator> & theAllocator);

		/****************** ChangeLoops ******************/
		%feature("compactdefaultargs") ChangeLoops;
		%feature("autodoc", "No available documentation.

Returns
-------
TopTools_ListOfShape
") ChangeLoops;
		TopTools_ListOfShape & ChangeLoops();

		/****************** ChangeShapes ******************/
		%feature("compactdefaultargs") ChangeShapes;
		%feature("autodoc", "No available documentation.

Returns
-------
TopTools_ListOfShape
") ChangeShapes;
		TopTools_ListOfShape & ChangeShapes();

		/****************** IsRegular ******************/
		%feature("compactdefaultargs") IsRegular;
		%feature("autodoc", "No available documentation.

Returns
-------
bool
") IsRegular;
		Standard_Boolean IsRegular();

		/****************** Loops ******************/
		%feature("compactdefaultargs") Loops;
		%feature("autodoc", "No available documentation.

Returns
-------
TopTools_ListOfShape
") Loops;
		const TopTools_ListOfShape & Loops();

		/****************** SetRegular ******************/
		%feature("compactdefaultargs") SetRegular;
		%feature("autodoc", "No available documentation.

Parameters
----------
theFlag: bool

Returns
-------
None
") SetRegular;
		void SetRegular(const Standard_Boolean theFlag);

		/****************** Shapes ******************/
		%feature("compactdefaultargs") Shapes;
		%feature("autodoc", "No available documentation.

Returns
-------
TopTools_ListOfShape
") Shapes;
		const TopTools_ListOfShape & Shapes();

};


%extend BOPTools_ConnexityBlock {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*******************************
* class BOPTools_CoupleOfShape *
*******************************/
class BOPTools_CoupleOfShape {
	public:
		/****************** BOPTools_CoupleOfShape ******************/
		%feature("compactdefaultargs") BOPTools_CoupleOfShape;
		%feature("autodoc", "No available documentation.

Returns
-------
None
") BOPTools_CoupleOfShape;
		 BOPTools_CoupleOfShape();

		/****************** SetShape1 ******************/
		%feature("compactdefaultargs") SetShape1;
		%feature("autodoc", "No available documentation.

Parameters
----------
theShape: TopoDS_Shape

Returns
-------
None
") SetShape1;
		void SetShape1(const TopoDS_Shape & theShape);

		/****************** SetShape2 ******************/
		%feature("compactdefaultargs") SetShape2;
		%feature("autodoc", "No available documentation.

Parameters
----------
theShape: TopoDS_Shape

Returns
-------
None
") SetShape2;
		void SetShape2(const TopoDS_Shape & theShape);

		/****************** Shape1 ******************/
		%feature("compactdefaultargs") Shape1;
		%feature("autodoc", "No available documentation.

Returns
-------
TopoDS_Shape
") Shape1;
		const TopoDS_Shape Shape1();

		/****************** Shape2 ******************/
		%feature("compactdefaultargs") Shape2;
		%feature("autodoc", "No available documentation.

Returns
-------
TopoDS_Shape
") Shape2;
		const TopoDS_Shape Shape2();

};


%extend BOPTools_CoupleOfShape {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/******************************
* class BOPTools_PairSelector *
******************************/
/**************************
* class BOPTools_Parallel *
**************************/
/*********************
* class BOPTools_Set *
*********************/
class BOPTools_Set {
	public:
		/****************** BOPTools_Set ******************/
		%feature("compactdefaultargs") BOPTools_Set;
		%feature("autodoc", "No available documentation.

Returns
-------
None
") BOPTools_Set;
		 BOPTools_Set();

		/****************** BOPTools_Set ******************/
		%feature("compactdefaultargs") BOPTools_Set;
		%feature("autodoc", "No available documentation.

Parameters
----------
theAllocator: NCollection_BaseAllocator

Returns
-------
None
") BOPTools_Set;
		 BOPTools_Set(const opencascade::handle<NCollection_BaseAllocator> & theAllocator);

		/****************** Add ******************/
		%feature("compactdefaultargs") Add;
		%feature("autodoc", "No available documentation.

Parameters
----------
theS: TopoDS_Shape
theType: TopAbs_ShapeEnum

Returns
-------
None
") Add;
		void Add(const TopoDS_Shape & theS, const TopAbs_ShapeEnum theType);

		/****************** Assign ******************/
		%feature("compactdefaultargs") Assign;
		%feature("autodoc", "No available documentation.

Parameters
----------
Other: BOPTools_Set

Returns
-------
BOPTools_Set
") Assign;
		BOPTools_Set & Assign(const BOPTools_Set & Other);

		/****************** HashCode ******************/
		%feature("compactdefaultargs") HashCode;
		%feature("autodoc", "Computes a hash code for this set, in the range [1, theupperbound] @param theupperbound the upper bound of the range a computing hash code must be within returns a computed hash code, in the range [1, theupperbound].

Parameters
----------
theUpperBound: int

Returns
-------
int
") HashCode;
		Standard_Integer HashCode(Standard_Integer theUpperBound);

        %extend {
            Standard_Integer __hash__() {
            return $self->HashCode(2147483647);
            }
        };

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "No available documentation.

Parameters
----------
aOther: BOPTools_Set

Returns
-------
bool
") IsEqual;
		Standard_Boolean IsEqual(const BOPTools_Set & aOther);

		/****************** NbShapes ******************/
		%feature("compactdefaultargs") NbShapes;
		%feature("autodoc", "No available documentation.

Returns
-------
int
") NbShapes;
		Standard_Integer NbShapes();

		/****************** Shape ******************/
		%feature("compactdefaultargs") Shape;
		%feature("autodoc", "No available documentation.

Returns
-------
TopoDS_Shape
") Shape;
		const TopoDS_Shape Shape();

};


%extend BOPTools_Set {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/******************************
* class BOPTools_SetMapHasher *
******************************/
class BOPTools_SetMapHasher {
	public:
		/****************** HashCode ******************/
		%feature("compactdefaultargs") HashCode;
		%feature("autodoc", "Computes a hash code for the given set, in the range [1, theupperbound] @param theset the set which hash code is to be computed @param theupperbound the upper bound of the range a computing hash code must be within returns a computed hash code, in the range [1, theupperbound].

Parameters
----------
theSet: BOPTools_Set
theUpperBound: int

Returns
-------
int
") HashCode;
		static Standard_Integer HashCode(const BOPTools_Set & theSet, Standard_Integer theUpperBound);

		/****************** IsEqual ******************/
		%feature("compactdefaultargs") IsEqual;
		%feature("autodoc", "No available documentation.

Parameters
----------
aSet1: BOPTools_Set
aSet2: BOPTools_Set

Returns
-------
bool
") IsEqual;
		static Standard_Boolean IsEqual(const BOPTools_Set & aSet1, const BOPTools_Set & aSet2);

};


%extend BOPTools_SetMapHasher {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* python proxy for excluded classes */
%pythoncode {
@classnotwrapped
class BOPTools_Parallel:
	pass

@classnotwrapped
class BOPTools_BoxSelector:
	pass

@classnotwrapped
class BOPTools_BoxSet:
	pass

@classnotwrapped
class BOPTools_PairSelector:
	pass

}
/* end python proxy for excluded classes */
/* harray1 classes */
/* harray2 classes */
/* hsequence classes */

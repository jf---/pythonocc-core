
##Copyright 2010 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.


from OCC.Utils.Construct import *

# Create the shape to be splitted. S1 is a TopoDS_Shape object
S1 = make_cube(10,20,30)

# Create the face to be used as the tool
P = gp_Pnt(5,10,15)
D = gp_Dir(gp_Vec(0,0,1))
pln = gp_Pln(P,D)
tool_face = make_face(pln,-20,20,-20,20)
shp_result = splitter(tool_face, S1)

if __name__ == "__main__":
    # Display
    from OCC.Display.SimpleGui import *
    display, start_display, add_menu, add_function_to_menu = init_display()
    # Before split
    display.DisplayColoredShape(S1,'RED')
    display.DisplayColoredShape(tool_face,'BLUE')
    # Result
    display.DisplayShape(shp_result)
    start_display()


 // do a section
     BRepAlgoAPI_Section asect(aBody,aPlane, Standard_False);
     asect.ComputePCurveOn1(Standard_True);
     asect.Approximation(Standard_True);
     asect.Build();

     if (asect.IsDone()) {
          // do a split
          TopoDS_Shape R=asect.Shape();
          QList<TopoDS_Edge> edges;
          BRepFeat_SplitShape asplit(aBody);
          for (TopExp_Explorer Ex(R,TopAbs_EDGE); Ex.More(); Ex.Next()) {
               TopoDS_Shape anEdge=Ex.Current();
               TopoDS_Shape aFace;
               if (asect.HasAncestorFaceOn1(anEdge,aFace)) {
                    TopoDS_Face F=TopoDS::Face(aFace);
                    TopoDS_Edge E=TopoDS::Edge(anEdge);
                    edges.append(E);
                    asplit.Add(E,F);
               }
          }
          asplit.Build();

          // no edge, shape stay the same, means no intersection between plane and body
          if (edges.count()==0)
               return;
          
          // split is done
          if (asplit.IsDone()) {

               // go through all faces and keep those you want
               // in my case, I keept all those that are one the positive side of my 
               // section plane
               for (TopExp_Explorer iter(asplit.Shape(),TopAbs_FACE);iter.More();iter.Next()) {
                    if (iter.Current().ShapeType()==TopAbs_FACE) {
                         
}
}
}
}

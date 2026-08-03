from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import IAcadObjectCollection, AcadObject
from ...Types.Ge import (
    PyGePoint3d,
    PyGeVector3d,
    PyGePoint3dArray,
)
from ...Types.VarType import (
    Variant,
    vDoubleArray,
    vObjectArray,
)
from ...Types.Ac import AcBlockScaling, AcInsertUnits

if TYPE_CHECKING:
    from ..AcadEntity import AcadEntity
    from .AcadLayout import AcadLayout
    from .AcadDatabase import AcadDatabase
    from ..Entities.Acad3DFace import Acad3DFace
    from ..Entities.Acad3DPolyline import Acad3DPolyline
    from ..Entities.Acad3DSolid import Acad3DSolid
    from ..Entities.AcadArc import AcadArc
    from ..Entities.AcadAttribute import AcadAttribute
    from ..Entities.AcadBlockReference import AcadBlockReference
    from ..Entities.AcadCircle import AcadCircle
    from ..Entities.AcadDim3PointAngular import AcadDim3PointAngular
    from ..Entities.AcadDimAligned import AcadDimAligned
    from ..Entities.AcadDimAngular import AcadDimAngular
    from ..Entities.AcadDimArcLength import AcadDimArcLength
    from ..Entities.AcadDimDiametric import AcadDimDiametric
    from ..Entities.AcadDimOrdinate import AcadDimOrdinate
    from ..Entities.AcadDimRadial import AcadDimRadial
    from ..Entities.AcadDimRadialLarge import AcadDimRadialLarge
    from ..Entities.AcadDimRotated import AcadDimRotated
    from ..Entities.AcadEllipse import AcadEllipse
    from ..Entities.AcadExternalReference import AcadExternalReference
    from ..Entities.AcadHatch import AcadHatch
    from ..Entities.AcadLeader import AcadLeader
    from ..Entities.AcadLine import AcadLine
    from ..Entities.AcadLWPolyline import AcadLWPolyline
    from ..Entities.AcadMInsertBlock import AcadMInsertBlock
    from ..Entities.AcadMLine import AcadMLine
    from ..Entities.AcadMtext import AcadMtext
    from ..Entities.AcadPoint import AcadPoint
    from ..Entities.AcadPolyfaceMesh import AcadPolyfaceMesh
    from ..Entities.AcadPolygonMesh import AcadPolygonMesh
    from ..Entities.AcadPolyline import AcadPolyline
    from ..Entities.AcadRasterImage import AcadRasterImage
    from ..Entities.AcadRay import AcadRay
    from ..Entities.AcadRegion import AcadRegion
    from ..Entities.AcadSection import AcadSection
    from ..Entities.AcadShape import AcadShape
    from ..Entities.AcadSolid import AcadSolid
    from ..Entities.AcadSpline import AcadSpline
    from ..Entities.AcadTable import AcadTable
    from ..Entities.AcadText import AcadText
    from ..Entities.AcadTolerance import AcadTolerance
    from ..Entities.AcadTrace import AcadTrace
    from ..Entities.AcadXline import AcadXline

class AcadBlock(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BlockScaling: AcBlockScaling = proxy_property('AcBlockScaling', 'BlockScaling', AccessMode.ReadWrite)
    Comments: str = proxy_property(str, 'Comments', AccessMode.ReadWrite)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Explodable: bool = proxy_property(bool, 'Explodable', AccessMode.ReadWrite)
    IsDynamicBlock: bool = proxy_property(bool, 'IsDynamicBlock', AccessMode.ReadOnly)
    IsLayout: bool = proxy_property(bool, 'IsLayout', AccessMode.ReadOnly)
    IsXRef: bool = proxy_property(bool, 'IsXRef', AccessMode.ReadOnly)
    Layout: AcadLayout = proxy_property('AcadLayout', 'Layout', AccessMode.ReadOnly)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Origin: PyGePoint3d = proxy_property('PyGePoint3d', 'Origin', AccessMode.ReadWrite)
    Path: str = proxy_property(str, 'Path', AccessMode.ReadWrite)
    Units: AcInsertUnits = proxy_property('AcInsertUnits', 'Units', AccessMode.ReadWrite)
    XRefDatabase: AcadDatabase = proxy_property('AcadDatabase', 'XRefDatabase', AccessMode.ReadOnly)

    def Add3DFace(self, Point1: PyGePoint3d, Point2: PyGePoint3d, Point3: PyGePoint3d, Point4: PyGePoint3d) -> Acad3DFace:
        from ..Entities.Acad3DFace import Acad3DFace
        return Acad3DFace(self._obj.Add3DFace(Point1(), Point2(), Point3(), Point4()))

    def Add3DMesh(self, M: int, N: int, PointsMatrix: PyGePoint3dArray) -> AcadPolygonMesh:
        from ..Entities.AcadPolygonMesh import AcadPolygonMesh
        return AcadPolygonMesh(self._obj.Add3DMesh(M, N, PointsMatrix()))

    def Add3DPoly(self, PointsArray: PyGePoint3dArray) -> Acad3DPolyline:
        from ..Entities.Acad3DPolyline import Acad3DPolyline
        return Acad3DPolyline(self._obj.Add3DPoly(PointsArray()))

    def AddArc(self, Center: PyGePoint3d, Radius: float, StartAngle: float, EndAngle: float) -> AcadArc:
        from ..Entities.AcadArc import AcadArc
        return AcadArc(self._obj.AddArc(Center(), Radius, StartAngle, EndAngle))

    def AddAttribute(self, Height: float, Mode: int, Prompt: str, InsertionPoint: PyGePoint3d, Tag: str, Value: str) -> AcadAttribute:
        from ..Entities.AcadAttribute import AcadAttribute
        return AcadAttribute(self._obj.AddAttribute(Height, Mode, Prompt, InsertionPoint(), Tag, Value))

    def AddBox(self, Origin: PyGePoint3d, Length: float, Width: float, Height: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddBox(Origin(), Length, Width, Height))

    def AddCircle(self, Center: PyGePoint3d, Radius: float) -> AcadCircle:
        from ..Entities.AcadCircle import AcadCircle
        return AcadCircle(self._obj.AddCircle(Center(), Radius))

    def AddCone(self, Center: PyGePoint3d, BaseRadius: float, Height: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddCone(Center(), BaseRadius, Height))

    def AddCylinder(self, Center: PyGePoint3d, Radius: float, Height: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddCylinder(Center(), Radius, Height))

    def AddDim3PointAngular(self, AngleVertex: PyGePoint3d, FirstEndPoint: PyGePoint3d, SecondEndPoint: PyGePoint3d, TextPoint: PyGePoint3d) -> AcadDim3PointAngular:
        from ..Entities.AcadDim3PointAngular import AcadDim3PointAngular
        return AcadDim3PointAngular(self._obj.AddDim3PointAngular(AngleVertex(), FirstEndPoint(), SecondEndPoint(), TextPoint()))

    def AddDimAligned(self, ExtLine1Point: PyGePoint3d, ExtLine2Point: PyGePoint3d, TextPosition: PyGePoint3d) -> AcadDimAligned:
        from ..Entities.AcadDimAligned import AcadDimAligned
        return AcadDimAligned(self._obj.AddDimAligned(ExtLine1Point(), ExtLine2Point(), TextPosition()))

    def AddDimAngular(self, AngleVertex: PyGePoint3d, FirstEndPoint: PyGePoint3d, SecondEndPoint: PyGePoint3d, TextPoint: PyGePoint3d) -> AcadDimAngular:
        from ..Entities.AcadDimAngular import AcadDimAngular
        return AcadDimAngular(self._obj.AddDimAngular(AngleVertex(), FirstEndPoint(), SecondEndPoint(), TextPoint()))

    def AddDimArc(self, ArcCenter: PyGePoint3d, FirstEndPoint: PyGePoint3d, SecondEndPoint: PyGePoint3d, ArcPoint: PyGePoint3d) -> AcadDimArcLength:
        from ..Entities.AcadDimArcLength import AcadDimArcLength
        return AcadDimArcLength(self._obj.AddDimArc(ArcCenter(), FirstEndPoint(), SecondEndPoint(), ArcPoint()))

    def AddDimDiametric(self, ChordPoint: PyGePoint3d, FarChordPoint: PyGePoint3d, LeaderLength: float) -> AcadDimDiametric:
        from ..Entities.AcadDimDiametric import AcadDimDiametric
        return AcadDimDiametric(self._obj.AddDimDiametric(ChordPoint(), FarChordPoint(), LeaderLength))

    def AddDimOrdinate(self, DefinitionPoint: PyGePoint3d, LeaderEndPoint: PyGePoint3d, UseXAxis: int) -> AcadDimOrdinate:
        from ..Entities.AcadDimOrdinate import AcadDimOrdinate
        return AcadDimOrdinate(self._obj.AddDimOrdinate(DefinitionPoint(), LeaderEndPoint(), UseXAxis))

    def AddDimRadial(self, Center: PyGePoint3d, ChordPoint: PyGePoint3d, LeaderLength: float) -> AcadDimRadial:
        from ..Entities.AcadDimRadial import AcadDimRadial
        return AcadDimRadial(self._obj.AddDimRadial(Center(), ChordPoint(), LeaderLength))

    def AddDimRadialLarge(self, Center: PyGePoint3d, ChordPoint: PyGePoint3d, OverrideCenter: PyGePoint3d, JogPoint: PyGePoint3d, JogAngle: float) -> AcadDimRadialLarge:
        from ..Entities.AcadDimRadialLarge import AcadDimRadialLarge
        return AcadDimRadialLarge(self._obj.AddDimRadialLarge(Center(), ChordPoint(), OverrideCenter(), JogPoint(), JogAngle))

    def AddDimRotated(self, ExtLine1Point: PyGePoint3d, ExtLine2Point: PyGePoint3d, DimLineLocation: PyGePoint3d, RotationAngle: float) -> AcadDimRotated:
        from ..Entities.AcadDimRotated import AcadDimRotated
        return AcadDimRotated(self._obj.AddDimRotated(ExtLine1Point(), ExtLine2Point(), DimLineLocation(), RotationAngle))

    def AddEllipse(self, Center: PyGePoint3d, MajorAxis: PyGeVector3d, RadiusRatio: float) -> AcadEllipse:
        from ..Entities.AcadEllipse import AcadEllipse
        return AcadEllipse(self._obj.AddEllipse(Center(), MajorAxis(), RadiusRatio))

    def AddEllipticalCone(self, Center: PyGePoint3d, MajorRadius: float, MinorRadius: float, Height: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddEllipticalCone(Center(), MajorRadius, MinorRadius, Height))

    def AddEllipticalCylinder(self, Center: PyGePoint3d, MajorRadius: float, MinorRadius: float, Height: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddEllipticalCylinder(Center(), MajorRadius, MinorRadius, Height))

    def AddExtrudedSolid(self, Profile: AcadRegion, Height: float, TaperAngle: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddExtrudedSolid(Profile(), Height, TaperAngle))

    def AddExtrudedSolidAlongPath(self, Profile: AcadRegion, Path: AcadEntity) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddExtrudedSolidAlongPath(Profile(), Path()))

    def AddHatch(self, PatternType: int, PatternName: str, Associativity: bool) -> AcadHatch:
        from ..Entities.AcadHatch import AcadHatch
        return AcadHatch(self._obj.AddHatch(PatternType, PatternName, Associativity))

    def AddLeader(self, PointsArray: PyGePoint3dArray, Annotation: AcadEntity, Type: int) -> AcadLeader:
        from ..Entities.AcadLeader import AcadLeader
        return AcadLeader(self._obj.AddLeader(PointsArray(), Annotation(), Type))

    def AddLightWeightPolyline(self, VerticesList: vDoubleArray) -> AcadLWPolyline:
        from ..Entities.AcadLWPolyline import AcadLWPolyline
        return AcadLWPolyline(self._obj.AddLightWeightPolyline(VerticesList()))

    def AddLine(self, StartPoint: PyGePoint3d, EndPoint: PyGePoint3d) -> AcadLine:
        from ..Entities.AcadLine import AcadLine
        return AcadLine(self._obj.AddLine(StartPoint(), EndPoint()))

    def AddMInsertBlock(self, InsertionPoint: PyGePoint3d, Name: str, Xscale: float, Yscale: float, Zscale: float, Rotation: float, NumRows: int, NumColumns: int, RowSpacing: float, ColumnSpacing: float) -> AcadMInsertBlock:
        from ..Entities.AcadMInsertBlock import AcadMInsertBlock
        return AcadMInsertBlock(self._obj.AddMInsertBlock(InsertionPoint(), Name, Xscale, Yscale, Zscale, Rotation, NumRows, NumColumns, RowSpacing, ColumnSpacing))

    def AddMLine(self, VertexList: PyGePoint3dArray) -> AcadMLine:
        from ..Entities.AcadMLine import AcadMLine
        return AcadMLine(self._obj.AddMLine(VertexList()))

    def AddMText(self, InsertionPoint: PyGePoint3d, Width: float, Text: str) -> AcadMtext:
        from ..Entities.AcadMtext import AcadMtext
        return AcadMtext(self._obj.AddMText(InsertionPoint(), Width, Text))

    def AddPoint(self, Point: PyGePoint3d) -> AcadPoint:
        from ..Entities.AcadPoint import AcadPoint
        return AcadPoint(self._obj.AddPoint(Point()))

    def AddPolyfaceMesh(self, VertexList: PyGePoint3dArray, FaceList: vDoubleArray) -> AcadPolyfaceMesh:
        from ..Entities.AcadPolyfaceMesh import AcadPolyfaceMesh
        return AcadPolyfaceMesh(self._obj.AddPolyfaceMesh(VertexList(), FaceList()))

    def AddPolyline(self, VerticesList: vDoubleArray) -> AcadPolyline:
        from ..Entities.AcadPolyline import AcadPolyline
        return AcadPolyline(self._obj.AddPolyline(VerticesList()))

    def AddRaster(self, imageFileName: str, InsertionPoint: PyGePoint3d, ScaleFactor: float, RotationAngle: float) -> AcadRasterImage:
        from ..Entities.AcadRasterImage import AcadRasterImage
        return AcadRasterImage(self._obj.AddRaster(imageFileName, InsertionPoint(), ScaleFactor, RotationAngle))

    def AddRay(self, Point1: PyGePoint3d, Point2: PyGePoint3d) -> AcadRay:
        from ..Entities.AcadRay import AcadRay
        return AcadRay(self._obj.AddRay(Point1(), Point2()))

    def AddRegion(self, ObjectList: vObjectArray) -> list:
        return list(self._obj.AddRegion(ObjectList()))

    def AddRevolvedSolid(self, Profile: AcadRegion, AxisPoint: PyGePoint3d, AxisDir: PyGeVector3d, Angle: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddRevolvedSolid(Profile(), AxisPoint(), AxisDir(), Angle))

    def AddSection(self, FromPoint: PyGePoint3d, ToPoint: PyGePoint3d, planeVector: PyGeVector3d) -> AcadSection:
        from ..Entities.AcadSection import AcadSection
        return AcadSection(self._obj.AddSection(FromPoint(), ToPoint(), planeVector()))

    def AddShape(self, Name: str, InsertionPoint: PyGePoint3d, ScaleFactor: float, RotationAngle: float) -> AcadShape:
        from ..Entities.AcadShape import AcadShape
        return AcadShape(self._obj.AddShape(Name, InsertionPoint(), ScaleFactor, RotationAngle))

    def AddSolid(self, Point1: PyGePoint3d, Point2: PyGePoint3d, Point3: PyGePoint3d, Point4: PyGePoint3d) -> AcadSolid:
        from ..Entities.AcadSolid import AcadSolid
        return AcadSolid(self._obj.AddSolid(Point1(), Point2(), Point3(), Point4()))

    def AddSphere(self, Center: PyGePoint3d, Radius: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddSphere(Center(), Radius))

    def AddSpline(self, PointsArray: PyGePoint3dArray, StartTangent: PyGeVector3d, EndTangent: PyGeVector3d) -> AcadSpline:
        from ..Entities.AcadSpline import AcadSpline
        return AcadSpline(self._obj.AddSpline(PointsArray(), StartTangent(), EndTangent()))

    def AddTable(self, InsertionPoint: PyGePoint3d, NumRows: int, NumColumns: int, RowHeight: float, ColWidth: float) -> AcadTable:
        from ..Entities.AcadTable import AcadTable
        return AcadTable(self._obj.AddTable(InsertionPoint(), NumRows, NumColumns, RowHeight, ColWidth))

    def AddText(self, TextString: str, InsertionPoint: PyGePoint3d, Height: float) -> AcadText:
        from ..Entities.AcadText import AcadText
        return AcadText(self._obj.AddText(TextString, InsertionPoint(), Height))

    def AddTolerance(self, Text: str, InsertionPoint: PyGePoint3d, Direction: PyGeVector3d) -> AcadTolerance:
        from ..Entities.AcadTolerance import AcadTolerance
        return AcadTolerance(self._obj.AddTolerance(Text, InsertionPoint(), Direction()))

    def AddTorus(self, Center: PyGePoint3d, TorusRadius: float, TubeRadius: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddTorus(Center(), TorusRadius, TubeRadius))

    def AddTrace(self, PointsArray: PyGePoint3dArray) -> AcadTrace:
        from ..Entities.AcadTrace import AcadTrace
        return AcadTrace(self._obj.AddTrace(PointsArray()))

    def AddWedge(self, Center: PyGePoint3d, Length: float, Width: float, Height: float) -> Acad3DSolid:
        from ..Entities.Acad3DSolid import Acad3DSolid
        return Acad3DSolid(self._obj.AddWedge(Center(), Length, Width, Height))

    def AddXline(self, Point1: PyGePoint3d, Point2: PyGePoint3d) -> AcadXline:
        from ..Entities.AcadXline import AcadXline
        return AcadXline(self._obj.AddXline(Point1(), Point2()))

    def AttachExternalReference(self, PathName: str, Name: str, InsertionPoint: PyGePoint3d, Xscale: float, Yscale: float, Zscale: float, Rotation: float, bOverlay: bool) -> AcadExternalReference:
        from ..Entities.AcadExternalReference import AcadExternalReference
        return AcadExternalReference(self._obj.AttachExternalReference(PathName, Name, InsertionPoint(), Xscale, Yscale, Zscale, Rotation, bOverlay))

    def Bind(self, bPrefixName: bool) -> None:
        self._obj.Bind(bPrefixName)

    def Detach(self) -> None:
        self._obj.Detach()

    def InsertBlock(self, InsertionPoint: PyGePoint3d, Name: str, Xscale: float, Yscale: float, Zscale: float, Rotation: float) -> AcadBlockReference:
        from ..Entities.AcadBlockReference import AcadBlockReference
        return AcadBlockReference(self._obj.InsertBlock(InsertionPoint(), Name, Xscale, Yscale, Zscale, Rotation))

    def Item(self, Index: Variant) -> AcadEntity:
        from ..AcadEntity import AcadEntity
        return AcadEntity(self._obj.Item(Index()))

    def Reload(self) -> None:
        self._obj.Reload()

    def Unload(self) -> None:
        self._obj.Unload()

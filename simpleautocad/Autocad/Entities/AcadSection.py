from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ac import AcSectionSubItem
from ...Types.Ge import PyGePoint3d
from ...Types.VarType import Variant, vObjectArray


class AcadSection(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BottomHeight = proxy_property(int, 'BottomHeight', AccessMode.ReadWrite)
    Elevation = proxy_property(float, 'Elevation', AccessMode.ReadWrite)
    IndicatorFillColor = proxy_property('AcadAcCmColor', 'IndicatorFillColor', AccessMode.ReadWrite)
    IndicatorTransparency = proxy_property(int, 'IndicatorTransparency', AccessMode.ReadWrite)
    LiveSectionEnabled = proxy_property(bool, 'LiveSectionEnabled', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    NumVertices = proxy_property(int, 'NumVertices', AccessMode.ReadWrite)
    SectionPlaneOffset = proxy_property(float, 'SectionPlaneOffset', AccessMode.ReadWrite)
    Settings = proxy_property('AcadSectionSettings', 'Settings', AccessMode.ReadOnly)
    SliceDepth = proxy_property(float, 'SliceDepth', AccessMode.ReadWrite)
    State = proxy_property('AcSectionState', 'State', AccessMode.ReadWrite)
    State2 = proxy_property('AcSectionState2', 'State2', AccessMode.ReadWrite)
    TopHeight = proxy_property(float, 'TopHeight', AccessMode.ReadWrite)
    VerticalDirection = proxy_property('PyGeVector3d', 'VerticalDirection', AccessMode.ReadWrite)
    Vertices = proxy_property('PyGePoint3dArray', 'Vertices', AccessMode.ReadWrite)
    ViewingDirection = proxy_property('PyGeVector3d', 'ViewingDirection', AccessMode.ReadWrite)

    def Coordinate(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.Coordinate(Index))

    def AddVertex(self, Index: int, Point: PyGePoint3d) -> None:
        self._obj.AddVertex(Index, Point())

    def Copy(self) -> AcadSection:
        return AcadSection(self._obj.Copy())

    def CreateJog(self, varPt: PyGePoint3d) -> None:
        self._obj.CreateJog(varPt())

    def GenerateSectionGeometry(self, pEntity: AcadEntity):
        (
            pIntersectionBoundaryObjs,
            pIntersectionFillObjs,
            pBackgroudnObjs,
            pForegroudObjs,
            pCurveTangencyObjs,
        ) = self._obj.GenerateSectionGeometry(pEntity)
        return (
            vObjectArray(pIntersectionBoundaryObjs),
            vObjectArray(pIntersectionFillObjs),
            vObjectArray(pBackgroudnObjs),
            vObjectArray(pForegroudObjs),
            vObjectArray(pCurveTangencyObjs),
        )

    def HitTest(self, varPtHit: PyGePoint3d):
        pHit, pSegmentIndex, pPtOnSegment, pSubItem = self._obj.HitTest(varPtHit())
        return bool(pHit), int(pSegmentIndex), Variant(pPtOnSegment), AcSectionSubItem(pSubItem)

    def RemoveVertex(self, nIndex: int) -> None:
        self._obj.RemoveVertex(nIndex)

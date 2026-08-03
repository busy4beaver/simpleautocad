from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadSection(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BottomHeight: float = proxy_property(float, 'BottomHeight', AccessMode.ReadWrite)
    Elevation: float = proxy_property(float, 'Elevation', AccessMode.ReadWrite)
    IndicatorFillColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'IndicatorFillColor', AccessMode.ReadWrite)
    IndicatorTransparency: int = proxy_property(int, 'IndicatorTransparency', AccessMode.ReadWrite)
    LiveSectionEnabled: bool = proxy_property(bool, 'LiveSectionEnabled', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadOnly)
    NumberOfVertices: int = proxy_property(int, 'NumberOfVertices', AccessMode.ReadOnly)
    Settings: AcadSectionSettings = proxy_property('AcadSectionSettings', 'Settings', AccessMode.ReadOnly)
    State: AcSectionState = proxy_property('AcSectionState', 'State', AccessMode.ReadWrite)
    TopHeight: float = proxy_property(float, 'TopHeight', AccessMode.ReadWrite)
    ViewingDirection: PyGeVector3d = proxy_property('PyGeVector3d', 'ViewingDirection', AccessMode.ReadWrite)
    VerticalDirection: PyGeVector3d = proxy_property('PyGeVector3d', 'VerticalDirection', AccessMode.ReadWrite)

    def AddVertex(self, Index: int, Point: PyGePoint3d) -> None:
        self._obj.AddVertex(Index, Point())

    def CreateJog(self, Point: PyGePoint3d) -> None:
        self._obj.CreateJog(Point())

    def GenerateSectionGeometry(self, Objects: list) -> None:
        self._obj.GenerateSectionGeometry(Objects)

    def HitTest(self, Point: PyGePoint3d) -> tuple:
        return self._obj.HitTest(Point())

    def RemoveVertex(self, Index: int) -> None:
        self._obj.RemoveVertex(Index)

    def SetVertices(self, Points: PyGePoint3dArray) -> None:
        self._obj.SetVertices(Points())

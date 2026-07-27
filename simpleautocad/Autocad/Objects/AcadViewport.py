from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.VarType import vDoubleArray
from .AcadView import AcadView


class AcadViewport(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ArcSmoothness = proxy_property(int, 'ArcSmoothness', AccessMode.ReadWrite)
    Center = proxy_property('PyGePoint2d', 'Center', AccessMode.ReadWrite)
    Direction = proxy_property('PyGeVector3d', 'Direction', AccessMode.ReadWrite)
    GridOn = proxy_property(bool, 'GridOn', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    LowerLeftCorner = proxy_property('vDoubleArray', 'LowerLeftCorner', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    OrthoOn = proxy_property(bool, 'OrthoOn', AccessMode.ReadWrite)
    SnapBasePoint = proxy_property('vDoubleArray', 'SnapBasePoint', AccessMode.ReadWrite)
    SnapOn = proxy_property(bool, 'SnapOn', AccessMode.ReadWrite)
    SnapRotationAngle = proxy_property(float, 'SnapRotationAngle', AccessMode.ReadWrite)
    Target = proxy_property('PyGePoint3d', 'Target', AccessMode.ReadWrite)
    UCSIconAtOrigin = proxy_property(bool, 'UCSIconAtOrigin', AccessMode.ReadWrite)
    UCSIconOn = proxy_property(bool, 'UCSIconOn', AccessMode.ReadWrite)
    UpperRightCorner = proxy_property('vDoubleArray', 'UpperRightCorner', AccessMode.ReadOnly)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def GetGridSpacing(self) -> vDoubleArray:
        XSpacing, YSpacing = self._obj.GetGridSpacing()
        return vDoubleArray(XSpacing, YSpacing)

    def GetSnapSpacing(self) -> vDoubleArray:
        XSpacing, YSpacing = self._obj.GetSnapSpacing()
        return vDoubleArray(XSpacing, YSpacing)

    def SetGridSpacing(self, XSpacing: float, YSpacing: float) -> None:
        self._obj.SetGridSpacing(XSpacing, YSpacing)

    def SetSnapSpacing(self, XSpacing: float, YSpacing: float) -> None:
        self._obj.SetSnapSpacing(XSpacing, YSpacing)

    def SetView(self, View: AcadView) -> None:
        self._obj.SetView(View())

    def Split(self, NumWins) -> None:
        self._obj.Split(NumWins)

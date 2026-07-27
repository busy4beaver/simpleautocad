from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadPViewport(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ArcSmoothness = proxy_property(int, 'ArcSmoothness', AccessMode.ReadWrite)
    Center = proxy_property('PyGePoint3d', 'Center', AccessMode.ReadWrite)
    Clipped = proxy_property(bool, 'Clipped', AccessMode.ReadOnly)
    CustomScale = proxy_property(float, 'CustomScale', AccessMode.ReadWrite)
    Direction = proxy_property('PyGeVector3d', 'Direction', AccessMode.ReadWrite)
    DisplayLocked = proxy_property(bool, 'DisplayLocked', AccessMode.ReadWrite)
    GridOn = proxy_property(bool, 'GridOn', AccessMode.ReadWrite)
    HasSheetView = proxy_property(bool, 'HasSheetView', AccessMode.ReadOnly)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    LabelBlockId = proxy_property(int, 'LabelBlockId', AccessMode.ReadWrite)
    LayerPropertyOverrides = proxy_property(bool, 'LayerPropertyOverrides', AccessMode.ReadOnly)
    LensLength = proxy_property(float, 'LensLength', AccessMode.ReadWrite)
    ModelView = proxy_property('AcadView', 'ModelView', AccessMode.ReadWrite)
    ShadePlot = proxy_property('AcShadePlot', 'ShadePlot', AccessMode.ReadWrite)
    SheetView = proxy_property('AcadView', 'SheetView', AccessMode.ReadWrite)
    SnapBasePoint = proxy_property('PyGePoint2d', 'SnapBasePoint', AccessMode.ReadWrite)
    SnapOn = proxy_property(bool, 'SnapOn', AccessMode.ReadWrite)
    SnapRotationAngle = proxy_property(float, 'SnapRotationAngle', AccessMode.ReadWrite)
    StandardScale = proxy_property('AcViewportScale', 'StandardScale', AccessMode.ReadWrite)
    StandardScale2 = proxy_property(int, 'StandardScale2', AccessMode.ReadWrite)
    Target = proxy_property('PyGePoint3d', 'Target', AccessMode.ReadWrite)
    TwistAngle = proxy_property(float, 'TwistAngle', AccessMode.ReadWrite)
    UCSIconAtOrigin = proxy_property(bool, 'UCSIconAtOrigin', AccessMode.ReadWrite)
    UCSIconOn = proxy_property(bool, 'UCSIconOn', AccessMode.ReadWrite)
    UCSPerViewport = proxy_property(bool, 'UCSPerViewport', AccessMode.ReadWrite)
    ViewportOn = proxy_property(bool, 'ViewportOn', AccessMode.ReadWrite)
    VisualStyle = proxy_property(int, 'VisualStyle', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def Copy(self) -> AcadPViewport:
        return AcadPViewport(self._obj.Copy())

    def GetGridSpacing(self) -> tuple:
        XSpacing, YSpacing = self._obj.GetGridSpacing()
        return XSpacing, YSpacing

    def GetSnapSpacing(self) -> tuple:
        XSpacing, YSpacing = self._obj.GetSnapSpacing()
        return XSpacing, YSpacing

    def SetGridSpacing(self, XSpacing: float, YSpacing: float) -> None:
        self._obj.SetGridSpacing(XSpacing, YSpacing)

    def SetSnapSpacing(self, XSpacing: float, YSpacing: float) -> None:
        self._obj.SetSnapSpacing(XSpacing, YSpacing)

    def SyncModelView(self) -> None:
        self._obj.SyncModelView()

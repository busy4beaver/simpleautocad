from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadPViewport(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ArcSmoothness: int = proxy_property(int, 'ArcSmoothness', AccessMode.ReadWrite)
    Center: PyGePoint3d = proxy_property('PyGePoint3d', 'Center', AccessMode.ReadWrite)
    CustomScale: float = proxy_property(float, 'CustomScale', AccessMode.ReadWrite)
    Direction: PyGeVector3d = proxy_property('PyGeVector3d', 'Direction', AccessMode.ReadWrite)
    DisplayLocked: bool = proxy_property(bool, 'DisplayLocked', AccessMode.ReadWrite)
    GridOn: bool = proxy_property(bool, 'GridOn', AccessMode.ReadWrite)
    Height: float = proxy_property(float, 'Height', AccessMode.ReadWrite)
    LabelBlockId: int = proxy_property(int, 'LabelBlockId', AccessMode.ReadWrite)
    LayerPropertyOverrides: bool = proxy_property(bool, 'LayerPropertyOverrides', AccessMode.ReadOnly)
    LensLength: float = proxy_property(float, 'LensLength', AccessMode.ReadWrite)
    ModelView: AcadView = proxy_property('AcadView', 'ModelView', AccessMode.ReadWrite)
    ShadePlot: AcShadePlot = proxy_property('AcShadePlot', 'ShadePlot', AccessMode.ReadWrite)
    SheetView: AcadView = proxy_property('AcadView', 'SheetView', AccessMode.ReadWrite)
    StandardScale: AcViewportScale = proxy_property('AcViewportScale', 'StandardScale', AccessMode.ReadWrite)
    StandardScale2: AcStandardScale = proxy_property('AcStandardScale', 'StandardScale2', AccessMode.ReadWrite)
    Target: PyGePoint3d = proxy_property('PyGePoint3d', 'Target', AccessMode.ReadWrite)
    TwistAngle: float = proxy_property(float, 'TwistAngle', AccessMode.ReadWrite)
    UCSIconAtOrigin: bool = proxy_property(bool, 'UCSIconAtOrigin', AccessMode.ReadWrite)
    UCSIconOn: bool = proxy_property(bool, 'UCSIconOn', AccessMode.ReadWrite)
    UCSPerViewport: bool = proxy_property(bool, 'UCSPerViewport', AccessMode.ReadWrite)
    ViewportOn: bool = proxy_property(bool, 'ViewportOn', AccessMode.ReadWrite)
    Visible: bool = proxy_property(bool, 'Visible', AccessMode.ReadWrite)
    Width: float = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def Copy(self) -> AcadPViewport:
        return AcadPViewport(self._obj.Copy())

    def Display(self, Status: bool) -> None:
        self._obj.Display(Status)

    def GetGridSpacing(self) -> tuple:
        return self._obj.GetGridSpacing()

    def GetSnapSpacing(self) -> tuple:
        return self._obj.GetSnapSpacing()

    def SetGridSpacing(self, XSpacing: float, YSpacing: float) -> None:
        self._obj.SetGridSpacing(XSpacing, YSpacing)

    def SetSnapSpacing(self, XSpacing: float, YSpacing: float) -> None:
        self._obj.SetSnapSpacing(XSpacing, YSpacing)

    def SyncModelView(self) -> None:
        self._obj.SyncModelView()

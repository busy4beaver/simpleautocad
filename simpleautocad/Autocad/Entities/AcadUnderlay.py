from __future__ import annotations

from abc import ABC, abstractmethod

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3dArray


class AcadUnderlay(AcadEntity, ABC):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    AdjustForBackground = proxy_property(bool, 'AdjustForBackground', AccessMode.ReadWrite)
    ClippingEnabled = proxy_property(bool, 'ClippingEnabled', AccessMode.ReadWrite)
    Contrast = proxy_property(int, 'Contrast', AccessMode.ReadWrite)
    Fade = proxy_property(int, 'Fade', AccessMode.ReadWrite)
    File = proxy_property(str, 'File', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    ItemName = proxy_property(str, 'ItemName', AccessMode.ReadWrite)
    Monochrome = proxy_property(bool, 'Monochrome', AccessMode.ReadWrite)
    Position = proxy_property('PyGePoint3d', 'Position', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    UnderlayLayerOverrideApplied = proxy_property(bool, 'UnderlayLayerOverrideApplied', AccessMode.ReadWrite)
    UnderlayName = proxy_property(str, 'UnderlayName', AccessMode.ReadWrite)
    UnderlayVisibility = proxy_property(bool, 'UnderlayVisibility', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def ClipBoundary(self, PointsArray: PyGePoint3dArray) -> None:
        self._obj.ClipBoundary(PointsArray())

    @abstractmethod
    def Copy(self):
        ...

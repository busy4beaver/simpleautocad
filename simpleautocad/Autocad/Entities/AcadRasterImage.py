from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint2dArray


class AcadRasterImage(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Brightness = proxy_property(int, 'Brightness', AccessMode.ReadWrite)
    ClippingEnabled = proxy_property(bool, 'ClippingEnabled', AccessMode.ReadWrite)
    Contrast = proxy_property(int, 'Contrast', AccessMode.ReadWrite)
    Fade = proxy_property(int, 'Fade', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadOnly)
    ImageFile = proxy_property(str, 'ImageFile', AccessMode.ReadWrite)
    ImageHeight = proxy_property(float, 'ImageHeight', AccessMode.ReadWrite)
    ImageVisibility = proxy_property(bool, 'ImageVisibility', AccessMode.ReadWrite)
    ImageWidth = proxy_property(float, 'ImageWidth', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Origin = proxy_property('PyGePoint3d', 'Origin', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    ShowRotation = proxy_property(bool, 'ShowRotation', AccessMode.ReadWrite)
    Transparency = proxy_property(bool, 'Transparency', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadOnly)

    def ClipBoundary(self, PointsArray: PyGePoint2dArray) -> None:
        self._obj.ClipBoundary(PointsArray())

    def Copy(self) -> AcadRasterImage:
        return AcadRasterImage(self._obj.Copy())

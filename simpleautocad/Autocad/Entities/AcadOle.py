from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadOle(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    LockAspectRatio = proxy_property(bool, 'LockAspectRatio', AccessMode.ReadWrite)
    OleItemType = proxy_property('AcOleType', 'OleItemType', AccessMode.ReadWrite)
    OlePlotQuality = proxy_property('AcOlePlotQuality', 'OlePlotQuality', AccessMode.ReadWrite)
    OleSourceApp = proxy_property(str, 'OleSourceApp', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleHeight = proxy_property(float, 'ScaleHeight', AccessMode.ReadWrite)
    ScaleWidth = proxy_property(float, 'ScaleWidth', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def Copy(self) -> AcadOle:
        return AcadOle(self._obj.Copy())

from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadMLine(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates = proxy_property('PyGePoint3d', 'Coordinates', AccessMode.ReadWrite)
    Justification = proxy_property('AcMLineJustification', 'Justification', AccessMode.ReadWrite)
    MLineScale = proxy_property(float, 'MLineScale', AccessMode.ReadWrite)
    StyleName = proxy_property(str, 'StyleName', AccessMode.ReadOnly)

    def Copy(self) -> AcadMLine:
        return AcadMLine(self._obj.Copy())

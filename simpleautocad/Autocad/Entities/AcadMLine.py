from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3dArray, PyGeVector3d


class AcadMLine(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates: PyGePoint3dArray = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    Justification: AcMLineJustification = proxy_property('AcMLineJustification', 'Justification', AccessMode.ReadWrite)
    MLineScale: float = proxy_property(float, 'MLineScale', AccessMode.ReadWrite)
    StyleName: str = proxy_property(str, 'StyleName', AccessMode.ReadOnly)

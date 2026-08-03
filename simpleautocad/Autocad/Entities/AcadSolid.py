from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3dArray


class AcadSolid(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates: PyGePoint3dArray = proxy_property('PyGePoint3dArray', 'Coordinates', AccessMode.ReadWrite)
    Thickness: float = proxy_property(float, 'Thickness', AccessMode.ReadWrite)

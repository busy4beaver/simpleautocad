from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d, PyGeVector3d


class AcadPoint(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates: PyGePoint3d = proxy_property('PyGePoint3d', 'Coordinates', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Thickness: float = proxy_property(float, 'Thickness', AccessMode.ReadWrite)

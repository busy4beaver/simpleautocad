from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d, PyGeVector3d


class AcadCircle(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Center: PyGePoint3d = proxy_property('PyGePoint3d', 'Center', AccessMode.ReadWrite)
    Diameter: float = proxy_property(float, 'Diameter', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Radius: float = proxy_property(float, 'Radius', AccessMode.ReadWrite)
    Thickness: float = proxy_property(float, 'Thickness', AccessMode.ReadWrite)
    Area: float = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Circumference: float = proxy_property(float, 'Circumference', AccessMode.ReadOnly)

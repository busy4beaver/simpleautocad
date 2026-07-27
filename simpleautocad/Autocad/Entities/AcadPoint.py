from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadPoint(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Coordinates = proxy_property('PyGePoint3d', 'Coordinates', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)

    def Copy(self) -> AcadPoint:
        return AcadPoint(self._obj.Copy())

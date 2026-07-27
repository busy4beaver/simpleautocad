from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSurface import AcadSurface


class AcadExtrudedSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Direction = proxy_property('PyGeVector3d', 'Direction', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    TaperAngle = proxy_property(float, 'TaperAngle', AccessMode.ReadWrite)

    def Copy(self) -> AcadExtrudedSurface:
        return AcadExtrudedSurface(self._obj.Copy())

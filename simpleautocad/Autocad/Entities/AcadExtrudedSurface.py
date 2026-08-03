from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSurface import AcadSurface
from ...Types.Ge import PyGeVector3d


class AcadExtrudedSurface(AcadSurface):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Direction: PyGeVector3d = proxy_property('PyGeVector3d', 'Direction', AccessMode.ReadOnly)
    Height: float = proxy_property(float, 'Height', AccessMode.ReadWrite)
    TaperAngle: float = proxy_property(float, 'TaperAngle', AccessMode.ReadWrite)

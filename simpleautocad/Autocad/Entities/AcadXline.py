from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d, PyGeVector3d


class AcadXline(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BasePoint: PyGePoint3d = proxy_property('PyGePoint3d', 'BasePoint', AccessMode.ReadWrite)
    DirectionVector: PyGeVector3d = proxy_property('PyGeVector3d', 'DirectionVector', AccessMode.ReadWrite)
    SecondPoint: PyGePoint3d = proxy_property('PyGePoint3d', 'SecondPoint', AccessMode.ReadWrite)

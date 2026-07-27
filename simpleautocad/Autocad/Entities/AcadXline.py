from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadXline(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BasePoint = proxy_property('PyGePoint3d', 'BasePoint', AccessMode.ReadWrite)
    DirectionVector = proxy_property('PyGeVector3d', 'DirectionVector', AccessMode.ReadWrite)
    SecondPoint = proxy_property('PyGePoint3d', 'SecondPoint', AccessMode.ReadWrite)

    def Copy(self) -> AcadXline:
        return AcadXline(self._obj.Copy())

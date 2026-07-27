from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadHelix(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BaseRadius = proxy_property(float, 'BaseRadius', AccessMode.ReadWrite)
    Constrain = proxy_property('AcHelixConstrainType', 'Constrain', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    Position = proxy_property('PyGePoint3d', 'Position', AccessMode.ReadWrite)
    TopRadius = proxy_property(float, 'TopRadius', AccessMode.ReadWrite)
    TotalLength = proxy_property(float, 'TotalLength', AccessMode.ReadWrite)
    TurnHeight = proxy_property(float, 'TurnHeight', AccessMode.ReadWrite)
    Turns = proxy_property(int, 'Turns', AccessMode.ReadWrite)
    TurnSlope = proxy_property(float, 'TurnSlope', AccessMode.ReadWrite)
    Twist = proxy_property('AcHelixTwistType', 'Twist', AccessMode.ReadWrite)

    def Copy(self) -> AcadHelix:
        return AcadHelix(self._obj.Copy())

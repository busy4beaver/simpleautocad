from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadShape(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ObliqueAngle = proxy_property(float, 'ObliqueAngle', AccessMode.ReadWrite)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleFactor = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    Thickness = proxy_property(float, 'Thickness', AccessMode.ReadWrite)

    def Copy(self) -> AcadShape:
        return AcadShape(self._obj.Copy())

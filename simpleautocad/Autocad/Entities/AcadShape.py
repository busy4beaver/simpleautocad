from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d, PyGeVector3d


class AcadShape(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Height: float = proxy_property(float, 'Height', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    ObliqueAngle: float = proxy_property(float, 'ObliqueAngle', AccessMode.ReadWrite)
    Rotation: float = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    ScaleFactor: float = proxy_property(float, 'ScaleFactor', AccessMode.ReadWrite)
    Thickness: float = proxy_property(float, 'Thickness', AccessMode.ReadWrite)
    InsertionPoint: PyGePoint3d = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)

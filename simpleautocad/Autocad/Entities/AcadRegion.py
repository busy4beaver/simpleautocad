from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ac import AcBooleanType
from ...Types.Ge import PyGePoint2d, PyGePoint3d, PyGeVector3d
from ...Types.VarType import vObjectArray


class AcadRegion(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Area: float = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Centroid: PyGePoint2d = proxy_property('PyGePoint2d', 'Centroid', AccessMode.ReadOnly)
    MomentOfInertia: PyGePoint3d = proxy_property('PyGePoint3d', 'MomentOfInertia', AccessMode.ReadOnly)
    Normal: PyGeVector3d = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Perimeter: float = proxy_property(float, 'Perimeter', AccessMode.ReadOnly)
    PrincipalDirections: PyGeVector3d = proxy_property('PyGeVector3d', 'PrincipalDirections', AccessMode.ReadOnly)
    PrincipalMoments: PyGeVector3d = proxy_property('PyGeVector3d', 'PrincipalMoments', AccessMode.ReadOnly)
    ProductOfInertia: PyGeVector3d = proxy_property('PyGeVector3d', 'ProductOfInertia', AccessMode.ReadOnly)
    RadiiOfGyration: PyGeVector3d = proxy_property('PyGeVector3d', 'RadiiOfGyration', AccessMode.ReadOnly)

    def Boolean(self, Operation: AcBooleanType, Object) -> None:
        self._obj.Boolean(Operation.value, Object())

    def Copy(self) -> AcadRegion:
        return AcadRegion(self._obj.Copy())

    def Explode(self) -> vObjectArray:
        return vObjectArray(self._obj.Explode())

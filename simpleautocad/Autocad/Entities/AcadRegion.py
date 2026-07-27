from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ac import AcBooleanType
from ...Types.VarType import vObjectArray


class AcadRegion(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Area = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Centroid = proxy_property('PyGePoint2d', 'Centroid', AccessMode.ReadOnly)
    MomentOfInertia = proxy_property('PyGePoint3d', 'MomentOfInertia', AccessMode.ReadOnly)
    Normal = proxy_property('PyGeVector3d', 'Normal', AccessMode.ReadWrite)
    Perimeter = proxy_property(float, 'Perimeter', AccessMode.ReadOnly)
    PrincipalDirections = proxy_property('PyGeVector3d', 'PrincipalDirections', AccessMode.ReadOnly)
    PrincipalMoments = proxy_property('PyGeVector3d', 'PrincipalMoments', AccessMode.ReadOnly)
    ProductOfInertia = proxy_property('PyGeVector3d', 'ProductOfInertia', AccessMode.ReadOnly)
    RadiiOfGyration = proxy_property('PyGeVector3d', 'RadiiOfGyration', AccessMode.ReadOnly)

    def Boolean(self, Operation: AcBooleanType, Object) -> None:
        self._obj.Boolean(Operation.value, Object())

    def Copy(self) -> AcadRegion:
        return AcadRegion(self._obj.Copy())

    def Explode(self) -> vObjectArray:
        return vObjectArray(self._obj.Explode())

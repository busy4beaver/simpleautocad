from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ac import AcBooleanType
from ...Types.Ge import PyGePoint3d
from .AcadRegion import AcadRegion


class Acad3DSolid(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Centroid = proxy_property('PyGePoint2d', 'Centroid', AccessMode.ReadOnly)
    History = proxy_property(bool, 'History', AccessMode.ReadWrite)
    MomentOfInertia = proxy_property('PyGePoint3d', 'MomentOfInertia', AccessMode.ReadOnly)
    Position = proxy_property('PyGePoint3d', 'Position', AccessMode.ReadOnly)
    PrincipalDirections = proxy_property('PyGeVector3d', 'PrincipalDirections', AccessMode.ReadOnly)
    PrincipalMoments = proxy_property('PyGeVector3d', 'PrincipalMoments', AccessMode.ReadOnly)
    ProductOfInertia = proxy_property('PyGeVector3d', 'ProductOfInertia', AccessMode.ReadOnly)
    RadiiOfGyration = proxy_property('PyGeVector3d', 'RadiiOfGyration', AccessMode.ReadOnly)
    ShowHistory = proxy_property(bool, 'ShowHistory', AccessMode.ReadWrite)
    SolidType = proxy_property(str, 'SolidType', AccessMode.ReadWrite)
    Volume = proxy_property(float, 'Volume', AccessMode.ReadOnly)

    def Boolean(self, Operation: AcBooleanType, Object) -> None:
        self._obj.Boolean(Operation.value, Object())

    def CheckInterference(self, Object, CreateInterferenceSolid: bool) -> bool:
        return self._obj.CheckInterference(Object(), CreateInterferenceSolid)

    def Delete(self) -> None:
        self._obj.Delete()

    def Copy(self) -> Acad3DSolid:
        return Acad3DSolid(self._obj.Copy())

    def SectionSolid(
        self, Point1: PyGePoint3d, Point2: PyGePoint3d, Point3: PyGePoint3d
    ) -> AcadRegion:
        return AcadRegion(self._obj.SectionSolid(Point1(), Point2(), Point3()))

    def SliceSolid(
        self, Point1: PyGePoint3d, Point2: PyGePoint3d, Point3: PyGePoint3d, Negative: bool
    ) -> Acad3DSolid:
        return Acad3DSolid(self._obj.SliceSolid(Point1(), Point2(), Point3(), Negative))

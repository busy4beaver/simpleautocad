from __future__ import annotations

from typing import TYPE_CHECKING

from .Base import AppObject
from .Proxy import proxy_property, AccessMode
from .AcadObject import AcadObject
from ..Types.Ac import AcExtendOption, AcLineWeight, AcColor
from ..Types.Ge import PyGePoint3d, PyGePoint3dArray, PyGeMatrix3d
from ..Types.VarType import vObjectArray

if TYPE_CHECKING:
    from .Objects.AcadHyperlinks import AcadHyperlinks
    from .Objects.AcadAcCmColor import AcadAcCmColor


class AcadEntity(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    EntityTransparency: str = proxy_property(str, 'EntityTransparency', AccessMode.ReadWrite)
    Hyperlinks: AcadHyperlinks = proxy_property('AcadHyperlinks', 'Hyperlinks', AccessMode.ReadOnly)
    Layer: str = proxy_property(str, 'Layer', AccessMode.ReadWrite)
    Linetype: str = proxy_property(str, 'Linetype', AccessMode.ReadWrite)
    LinetypeScale: float = proxy_property(float, 'LinetypeScale', AccessMode.ReadWrite)
    Lineweight: AcLineWeight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    Material: str = proxy_property(str, 'Material', AccessMode.ReadWrite)
    PlotStyleName: str = proxy_property(str, 'PlotStyleName', AccessMode.ReadWrite)
    TrueColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'TrueColor', AccessMode.ReadWrite)
    Visible: bool = proxy_property(bool, 'Visible', AccessMode.ReadWrite)

    def ArrayPolar(self, NumberOfObjects: int, AngleToFill: float, CenterPoint: PyGePoint3d):
        return self._obj.ArrayPolar(NumberOfObjects, AngleToFill, CenterPoint())

    def ArrayRectangular(
        self,
        NumberOfRows: int,
        NumberOfColumns: int,
        NumberOfLevels: int,
        DistBetweenRows: float,
        DistBetweenColumns: float,
        DistBetweenLevels: float,
    ):
        return self._obj.ArrayRectangular(
            NumberOfRows,
            NumberOfColumns,
            NumberOfLevels,
            DistBetweenRows,
            DistBetweenColumns,
            DistBetweenLevels,
        )

    def Copy(self) -> AcadEntity:
        return AcadEntity(self._obj.Copy())

    def GetBoundingBox(self) -> PyGePoint3dArray:
        return PyGePoint3dArray(self._obj.GetBoundingBox())

    def Highlight(self, HighlightFlag: bool) -> None:
        self._obj.Highlight(HighlightFlag)

    def IntersectWith(self, IntersectObject: AcadEntity, ExtendOption: AcExtendOption) -> PyGePoint3dArray:
        return self._obj.IntersectWith(IntersectObject(), ExtendOption)

    def Mirror(self, Point1: PyGePoint3d, Point2: PyGePoint3d):
        return self._obj.Mirror(Point1(), Point2())

    def Mirror3D(self, Point1: PyGePoint3d, Point2: PyGePoint3d, Point3: PyGePoint3d):
        return self._obj.Mirror3D(Point1(), Point2(), Point3())

    def Move(self, Point1: PyGePoint3d, Point2: PyGePoint3d) -> None:
        self._obj.Move(Point1(), Point2())

    def Rotate(self, BasePoint: PyGePoint3d, RotationAngle: float) -> None:
        self._obj.Rotate(BasePoint(), RotationAngle)

    def Rotate3D(self, Point1: PyGePoint3d, Point2: PyGePoint3d, RotationAngle: float) -> None:
        self._obj.Rotate3D(Point1(), Point2(), RotationAngle)

    def ScaleEntity(self, BasePoint: PyGePoint3d, ScaleFactor: float) -> None:
        self._obj.ScaleEntity(BasePoint(), ScaleFactor)

    def TransformBy(self, TransformationMatrix: PyGeMatrix3d) -> None:
        self._obj.TransformBy(TransformationMatrix())

    def Update(self) -> None:
        self._obj.Update()


class AcadSubEntity(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Color: AcColor = proxy_property('AcColor', 'Color', AccessMode.ReadWrite)
    Hyperlinks: AcadHyperlinks = proxy_property('AcadHyperlinks', 'Hyperlinks', AccessMode.ReadOnly)
    Layer: str = proxy_property(str, 'Layer', AccessMode.ReadWrite)
    Linetype: str = proxy_property(str, 'Linetype', AccessMode.ReadWrite)
    LinetypeScale: float = proxy_property(float, 'LinetypeScale', AccessMode.ReadWrite)
    Lineweight: AcLineWeight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    ObjectName: str = proxy_property(str, 'ObjectName', AccessMode.ReadOnly)
    PlotStyleName: str = proxy_property(str, 'PlotStyleName', AccessMode.ReadWrite)

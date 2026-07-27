from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.Ge import PyGePoint3d, PyGePoint3dArray
from ...Types.VarType import vObjectArray, Variant


class AcadSelectionSet(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Name = proxy_property(str, 'Name', AccessMode.ReadOnly)

    def AddItems(self, Items: vObjectArray) -> None:
        self._obj.AddItems(Items())

    def Clear(self) -> None:
        self._obj.Clear()

    def Delete(self) -> None:
        self._obj.Delete()

    def Erase(self) -> None:
        self._obj.Erase()

    def Highlight(self, HighlightFlag: bool) -> None:
        self._obj.Highlight(HighlightFlag)

    def Item(self, Index: int | str) -> AcadObject:
        return AcadObject(self._obj.Item(Index))

    def RemoveItems(self, Objects: vObjectArray) -> None:
        self._obj.RemoveItems(Objects())

    def Select(
        self,
        Mode,
        Point1: PyGePoint3d = None,
        Point2: PyGePoint3d = None,
        FilterType: Variant = None,
        FilterData: Variant = None,
    ) -> None:
        kwargs = {'Mode': Mode}
        if Point1 is not None:
            kwargs['Point1'] = Point1()
        if Point2 is not None:
            kwargs['Point2'] = Point2()
        if FilterType is not None and FilterData is not None:
            kwargs['FilterType'] = FilterType()
            kwargs['FilterData'] = FilterData()
        self._obj.Select(**kwargs)

    def SelectAtPoint(
        self,
        Point: PyGePoint3d,
        FilterType: Variant = None,
        FilterData: Variant = None,
    ) -> None:
        kwargs = {'Point': Point()}
        if FilterType is not None and FilterData is not None:
            kwargs['FilterType'] = FilterType()
            kwargs['FilterData'] = FilterData()
        self._obj.SelectAtPoint(**kwargs)

    def SelectByPolygon(
        self,
        Mode,
        PointsList: PyGePoint3dArray,
        FilterType: Variant = None,
        FilterData: Variant = None,
    ) -> None:
        kwargs = {'Mode': Mode, 'PointsList': PointsList()}
        if FilterType is not None and FilterData is not None:
            kwargs['FilterType'] = FilterType()
            kwargs['FilterData'] = FilterData()
        self._obj.SelectByPolygon(**kwargs)

    def SelectOnScreen(
        self, FilterType: Variant = None, FilterData: Variant = None
    ) -> None:
        if FilterType is not None and FilterData is not None:
            self._obj.SelectOnScreen(FilterType(), FilterData())
        else:
            self._obj.SelectOnScreen()

    def Update(self) -> None:
        self._obj.Update()

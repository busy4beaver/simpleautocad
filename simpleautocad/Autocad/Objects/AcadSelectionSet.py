from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.VarType import vObjectArray, Variant
from ...Types.Ac import AcSelect

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication
    from ..AcadEntity import AcadEntity


class AcadSelectionSet(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadOnly)

    def AddItems(self, Objects: vObjectArray) -> None:
        self._obj.AddItems(Objects)

    def Clear(self) -> None:
        self._obj.Clear()

    def Delete(self) -> None:
        self._obj.Delete()

    def Erase(self) -> None:
        self._obj.Erase()

    def Highlight(self, bFlag: bool) -> None:
        self._obj.Highlight(bFlag)

    def Item(self, Index: Variant) -> AcadEntity:
        from ..AcadEntity import AcadEntity

        return AcadEntity(self._obj.Item(Index))

    def RemoveItems(self, Objects: vObjectArray) -> None:
        self._obj.RemoveItems(Objects)

    def Select(
        self,
        Mode: AcSelect,
        Point1: Optional[Variant] = None,
        Point2: Optional[Variant] = None,
        FilterType: Optional[Variant] = None,
        FilterData: Optional[Variant] = None,
    ) -> None:
        args = [Mode]
        # Trailing optional COM args must be omitted, not passed as None.
        if Point1 is not None or Point2 is not None or FilterType is not None or FilterData is not None:
            args.append(Point1)
        if Point2 is not None or FilterType is not None or FilterData is not None:
            args.append(Point2)
        if FilterType is not None or FilterData is not None:
            args.append(FilterType)
        if FilterData is not None:
            args.append(FilterData)
        self._obj.Select(*args)

    def SelectAtPoint(
        self,
        Point: Variant,
        FilterType: Optional[Variant] = None,
        FilterData: Optional[Variant] = None,
    ) -> None:
        if FilterType is None and FilterData is None:
            self._obj.SelectAtPoint(Point)
        elif FilterData is None:
            self._obj.SelectAtPoint(Point, FilterType)
        else:
            self._obj.SelectAtPoint(Point, FilterType, FilterData)

    def SelectByPolygon(
        self,
        Mode: AcSelect,
        PointsList: Variant,
        FilterType: Optional[Variant] = None,
        FilterData: Optional[Variant] = None,
    ) -> None:
        if FilterType is None and FilterData is None:
            self._obj.SelectByPolygon(Mode, PointsList)
        elif FilterData is None:
            self._obj.SelectByPolygon(Mode, PointsList, FilterType)
        else:
            self._obj.SelectByPolygon(Mode, PointsList, FilterType, FilterData)

    def SelectOnScreen(
        self,
        FilterType: Optional[Variant] = None,
        FilterData: Optional[Variant] = None,
    ) -> None:
        if FilterType is None and FilterData is None:
            self._obj.SelectOnScreen()
        elif FilterData is None:
            self._obj.SelectOnScreen(FilterType)
        else:
            self._obj.SelectOnScreen(FilterType, FilterData)

    def Update(self) -> None:
        self._obj.Update()

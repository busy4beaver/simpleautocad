from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from ...Types.Ge import PyGePoint3d
from .AcadLayout import AcadLayout


class AcadLayouts(IAcadObjectCollection[AcadLayout]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, InsertionPoint: PyGePoint3d, Name: str) -> AcadLayout:
        return AcadLayout(self._obj.Add(InsertionPoint(), Name))

    def Item(self, Index: int | str) -> AcadLayout:
        return AcadLayout(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadLayout]:
        for item in self._obj:
            yield AcadLayout(item)

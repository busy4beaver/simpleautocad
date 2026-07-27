from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadView import AcadView


class AcadViews(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadView:
        return AcadView(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadView:
        return AcadView(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadView(item)

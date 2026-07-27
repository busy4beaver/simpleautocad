from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadTextStyle import AcadTextStyle


class AcadTextStyles(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str = None) -> AcadTextStyle:
        return AcadTextStyle(self._obj.Add(Name))

    def Item(self, Index: int) -> AcadTextStyle:
        return AcadTextStyle(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadTextStyle(item)

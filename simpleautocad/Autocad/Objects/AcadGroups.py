from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadGroup import AcadGroup


class AcadGroups(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadGroup:
        return AcadGroup(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadGroup:
        return AcadGroup(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadGroup(item)

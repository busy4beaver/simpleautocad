from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadLayer import AcadLayer


class AcadLayers(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadLayer:
        return AcadLayer(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadLayer:
        return AcadLayer(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadLayer(item)

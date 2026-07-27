from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadViewport import AcadViewport


class AcadViewports(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadViewport:
        return AcadViewport(self._obj.Add(Name))

    def DeleteConfiguration(self, Name: str) -> None:
        self._obj.DeleteConfiguration(Name)

    def Item(self, Index: int | str) -> AcadViewport:
        return AcadViewport(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadViewport(item)

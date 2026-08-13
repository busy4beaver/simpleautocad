from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from .AcadDimStyle import AcadDimStyle


class AcadDimStyles(IAcadObjectCollection[AcadDimStyle]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadDimStyle:
        return AcadDimStyle(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadDimStyle:
        return AcadDimStyle(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadDimStyle]:
        for item in self._obj:
            yield AcadDimStyle(item)

from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from ...Types.Ge import PyGePoint3d
from .AcadBlock import AcadBlock


class AcadBlocks(IAcadObjectCollection[AcadBlock]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, InsertionPoint: PyGePoint3d, Name: str) -> AcadBlock:
        return AcadBlock(self._obj.Add(InsertionPoint(), Name))

    def Item(self, Index: int | str) -> AcadBlock:
        return AcadBlock(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadBlock]:
        for item in self._obj:
            yield AcadBlock(item)

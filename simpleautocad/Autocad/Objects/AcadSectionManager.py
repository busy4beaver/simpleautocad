from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from ..Entities.AcadSection import AcadSection


class AcadSectionManager(IAcadObjectCollection[AcadSection]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def GetLiveSection(self) -> AcadSection:
        return AcadSection(self._obj.GetLiveSection())

    def GetUniqueSectionName(self) -> str:
        return self._obj.GetUniqueSectionName()

    def Item(self, Index: int | str) -> AcadSection:
        return AcadSection(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadSection]:
        for item in self._obj:
            yield AcadSection(item)

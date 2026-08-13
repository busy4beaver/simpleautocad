from __future__ import annotations

from typing import Iterator

from ..AcadObject import IAcadObjectCollection
from .AcadMaterial import AcadMaterial


class AcadMaterials(IAcadObjectCollection[AcadMaterial]):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str) -> AcadMaterial:
        return AcadMaterial(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadMaterial:
        return AcadMaterial(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadMaterial]:
        for item in self._obj:
            yield AcadMaterial(item)

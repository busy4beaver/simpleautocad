from __future__ import annotations

from typing import Iterator, Optional

from ..AcadObject import IAcadObjectCollection
from .AcadDictionary import AcadDictionary


class AcadDictionaries(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: Optional[str] = None) -> AcadDictionary:
        if Name is None:
            return AcadDictionary(self._obj.Add())
        return AcadDictionary(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadDictionary:
        return AcadDictionary(self._obj.Item(Index))

    def __iter__(self) -> Iterator[AcadDictionary]:
        for item in self._obj:
            yield AcadDictionary(item)

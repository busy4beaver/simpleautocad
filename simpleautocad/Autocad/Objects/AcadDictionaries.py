from __future__ import annotations

from ..AcadObject import IAcadObjectCollection
from .AcadDictionary import AcadDictionary


class AcadDictionaries(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def Add(self, Name: str = None) -> AcadDictionary:
        if Name is None:
            return AcadDictionary(self._obj.Add())
        return AcadDictionary(self._obj.Add(Name))

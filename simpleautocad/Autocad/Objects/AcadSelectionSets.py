from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject


class AcadSelectionSets(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, Name: str) -> AcadSelectionSet:
        return AcadSelectionSet(self._obj.Add(Name))

    def Item(self, Index) -> AcadSelectionSet:
        return AcadSelectionSet(self._obj.Item(Index))

from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode
from .AcadSelectionSet import AcadSelectionSet


class AcadSelectionSets(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, Name: str = None) -> AcadSelectionSet:
        return AcadSelectionSet(self._obj.Add(Name))

    def Item(self, Index: int | str) -> AcadSelectionSet:
        return AcadSelectionSet(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadSelectionSet(item)

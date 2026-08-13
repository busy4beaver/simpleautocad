from __future__ import annotations

from typing import Iterator, Union

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject
from .AcadSelectionSet import AcadSelectionSet


class AcadSelectionSets(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, Name: str) -> AcadSelectionSet:
        return AcadSelectionSet(self._obj.Add(Name))

    def Item(self, Index: Union[int, str]) -> AcadSelectionSet:
        return AcadSelectionSet(self._obj.Item(Index))

    def __getitem__(self, Index: Union[int, str]) -> AcadSelectionSet:
        return self.Item(Index)

    def __iter__(self) -> Iterator[AcadSelectionSet]:
        for item in self._obj:
            yield AcadSelectionSet(item)

    def __len__(self) -> int:
        return int(self.Count)

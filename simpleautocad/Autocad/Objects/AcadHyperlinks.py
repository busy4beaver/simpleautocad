from __future__ import annotations

from ..Base import AppObjectCollection
from ..Proxy import proxy_property, AccessMode
from .AcadHyperlink import AcadHyperlink


class AcadHyperlinks(AppObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, Name: str, Description: str = '', NamedLocation: str = '') -> AcadHyperlink:
        return AcadHyperlink(self._obj.Add(Name, Description, NamedLocation))

    def Item(self, Index: int | str) -> AcadHyperlink:
        return AcadHyperlink(self._obj.Item(Index))

    def __iter__(self):
        for item in self._obj:
            yield AcadHyperlink(item)

from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject

if TYPE_CHECKING:
    from .AcadHyperlink import AcadHyperlink


class AcadHyperlinks(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(self, Name: str, Description: str = None, NamedLocation: str = None) -> AcadHyperlink:
        from .AcadHyperlink import AcadHyperlink
        return AcadHyperlink(self._obj.Add(Name, Description, NamedLocation))

    def Item(self, Index) -> AcadHyperlink:
        from .AcadHyperlink import AcadHyperlink
        return AcadHyperlink(self._obj.Item(Index))

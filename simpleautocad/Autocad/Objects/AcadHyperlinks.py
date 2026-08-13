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
        """Add a hyperlink. Optional COM args must be omitted, not passed as None."""
        from .AcadHyperlink import AcadHyperlink
        if Description is None and NamedLocation is None:
            result = self._obj.Add(Name)
        elif NamedLocation is None:
            result = self._obj.Add(Name, Description)
        else:
            # Description is positional before NamedLocation — empty string if omitted
            result = self._obj.Add(Name, Description if Description is not None else '', NamedLocation)
        return AcadHyperlink(result)

    def Item(self, Index) -> AcadHyperlink:
        from .AcadHyperlink import AcadHyperlink
        return AcadHyperlink(self._obj.Item(Index))

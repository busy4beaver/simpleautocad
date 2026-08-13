from __future__ import annotations

from typing import TYPE_CHECKING, Iterator, Optional, Union

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject

if TYPE_CHECKING:
    from .AcadHyperlink import AcadHyperlink
    from .AcadApplication import AcadApplication


class AcadHyperlinks(AppObject):
    """Collection of hyperlinks attached to an entity."""

    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)

    def Add(
        self,
        Name: str,
        Description: Optional[str] = None,
        NamedLocation: Optional[str] = None,
    ) -> AcadHyperlink:
        """Add a hyperlink.

        Optional COM args must be omitted, not passed as None (otherwise
        AutoCAD raises E_INVALIDARG / -2147024809).
        """
        from .AcadHyperlink import AcadHyperlink

        if Description is None and NamedLocation is None:
            result = self._obj.Add(Name)
        elif NamedLocation is None:
            result = self._obj.Add(Name, Description)
        else:
            # Description is positional before NamedLocation
            result = self._obj.Add(
                Name,
                Description if Description is not None else '',
                NamedLocation,
            )
        return AcadHyperlink(result)

    def Item(self, Index: Union[int, str]) -> AcadHyperlink:
        from .AcadHyperlink import AcadHyperlink

        return AcadHyperlink(self._obj.Item(Index))

    def __getitem__(self, Index: Union[int, str]) -> AcadHyperlink:
        return self.Item(Index)

    def __iter__(self) -> Iterator[AcadHyperlink]:
        from .AcadHyperlink import AcadHyperlink

        for item in self._obj:
            yield AcadHyperlink(item)

    def __len__(self) -> int:
        return int(self.Count)

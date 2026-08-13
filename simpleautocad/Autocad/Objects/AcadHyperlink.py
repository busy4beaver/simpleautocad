from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication


class AcadHyperlink(AppObject):
    """A URL and optional description / named location on an entity."""

    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    URL: str = proxy_property(str, 'URL', AccessMode.ReadWrite)
    URLDescription: str = proxy_property(str, 'URLDescription', AccessMode.ReadWrite)
    URLNamedLocation: str = proxy_property(str, 'URLNamedLocation', AccessMode.ReadWrite)

    def Delete(self) -> None:
        self._obj.Delete()

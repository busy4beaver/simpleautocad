from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadHyperlink(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    URL = proxy_property(str, 'URL', AccessMode.ReadWrite)
    URLDescription = proxy_property(str, 'URLDescription', AccessMode.ReadWrite)
    URLNamedLocation = proxy_property(str, 'URLNamedLocation', AccessMode.ReadWrite)

    def Delete(self) -> None:
        self._obj.Delete()

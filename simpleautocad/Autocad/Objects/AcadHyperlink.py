from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject


class AcadHyperlink(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    URL: str = proxy_property(str, 'URL', AccessMode.ReadWrite)
    URLDescription: str = proxy_property(str, 'URLDescription', AccessMode.ReadWrite)
    URLNamedLocation: str = proxy_property(str, 'URLNamedLocation', AccessMode.ReadWrite)

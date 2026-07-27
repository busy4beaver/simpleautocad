from __future__ import annotations

from ..Base import AppObject, AppObjectCollection
from ..Proxy import proxy_property, AccessMode


class AcadMenuBar(AppObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Parent = proxy_property('AppObject', 'Parent', AccessMode.ReadWrite)

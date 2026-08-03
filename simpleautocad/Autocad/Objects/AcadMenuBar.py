from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject


class AcadMenuBar(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Parent: AcadApplication = proxy_property('AcadApplication', 'Parent', AccessMode.ReadOnly)

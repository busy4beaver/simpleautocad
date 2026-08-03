from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject

if TYPE_CHECKING:
    from .AcadApplication import AcadApplication


class AcadMenuBar(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Count: int = proxy_property(int, 'Count', AccessMode.ReadOnly)
    Parent: AcadApplication = proxy_property('AcadApplication', 'Parent', AccessMode.ReadOnly)

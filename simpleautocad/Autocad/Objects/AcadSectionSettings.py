from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadSectionSettings(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    CurrentSectionType = proxy_property('AcSectionType', 'CurrentSectionType', AccessMode.ReadWrite)

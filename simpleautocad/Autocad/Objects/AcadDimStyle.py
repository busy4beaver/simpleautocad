from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadDimStyle(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)

    def CopyFrom(self, SourceObject) -> None:
        self._obj.CopyFrom(SourceObject)

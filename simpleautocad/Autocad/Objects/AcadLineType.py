from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadLineType(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Description = proxy_property(str, 'Description', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)

from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadBlock import IAcadBlock


class AcadModelSpace(IAcadBlock):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Comments = proxy_property(str, 'Comments', AccessMode.ReadWrite)
    Layout = proxy_property('AcadLayout', 'Layout', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadOnly)
    Origin = proxy_property('PyGePoint3d', 'Origin', AccessMode.ReadWrite)
    Units = proxy_property('AcInsertUnits', 'Units', AccessMode.ReadWrite)

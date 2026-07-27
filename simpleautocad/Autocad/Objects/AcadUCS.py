from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.VarType import vDoubleArray


class AcadUCS(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Origin = proxy_property('PyGePoint3d', 'Origin', AccessMode.ReadWrite)
    XVector = proxy_property('PyGeVector3d', 'XVector', AccessMode.ReadWrite)
    YVector = proxy_property('PyGeVector3d', 'YVector', AccessMode.ReadWrite)

    def GetUCSMatrix(self) -> vDoubleArray:
        return vDoubleArray(self._obj.GetUCSMatrix())

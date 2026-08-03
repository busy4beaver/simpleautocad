from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject
from ...Types.Ge import PyGePoint3d, PyGeVector3d, PyGeMatrix3d


class AcadUCS(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Origin: PyGePoint3d = proxy_property('PyGePoint3d', 'Origin', AccessMode.ReadWrite)
    XVector: PyGeVector3d = proxy_property('PyGeVector3d', 'XVector', AccessMode.ReadWrite)
    YVector: PyGeVector3d = proxy_property('PyGeVector3d', 'YVector', AccessMode.ReadWrite)

    def GetUCSMatrix(self) -> PyGeMatrix3d:
        return PyGeMatrix3d(self._obj.GetUCSMatrix())

from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadBlockReference import AcadBlockReference


class AcadMInsertBlock(AcadBlockReference):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Columns = proxy_property(int, 'Columns', AccessMode.ReadWrite)
    ColumnSpacing = proxy_property(float, 'ColumnSpacing', AccessMode.ReadWrite)

    def Copy(self) -> AcadMInsertBlock:
        return AcadMInsertBlock(self._obj.Copy())

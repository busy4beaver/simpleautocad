from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadBlockReference import AcadBlockReference


class AcadMInsertBlock(AcadBlockReference):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Columns: int = proxy_property(int, 'Columns', AccessMode.ReadWrite)
    ColumnSpacing: float = proxy_property(float, 'ColumnSpacing', AccessMode.ReadWrite)
    Rows: int = proxy_property(int, 'Rows', AccessMode.ReadWrite)
    RowSpacing: float = proxy_property(float, 'RowSpacing', AccessMode.ReadWrite)

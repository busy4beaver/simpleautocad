from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadPlotConfiguration import AcadPlotConfiguration


class AcadLayout(AcadPlotConfiguration):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Block: AcadBlock = proxy_property('AcadBlock', 'Block', AccessMode.ReadOnly)
    TabOrder: int = proxy_property(int, 'TabOrder', AccessMode.ReadWrite)

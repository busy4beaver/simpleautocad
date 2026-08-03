from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from .AcadPlotConfiguration import AcadPlotConfiguration

if TYPE_CHECKING:
    from .AcadBlock import AcadBlock


class AcadLayout(AcadPlotConfiguration):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Block: AcadBlock = proxy_property('AcadBlock', 'Block', AccessMode.ReadOnly)
    TabOrder: int = proxy_property(int, 'TabOrder', AccessMode.ReadWrite)

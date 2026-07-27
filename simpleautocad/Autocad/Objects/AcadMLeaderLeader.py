from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from .AcadSubEntity import AcadSubEntity


class AcadMLeaderLeader(AcadSubEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ArrowheadBlock = proxy_property(str, 'ArrowheadBlock', AccessMode.ReadWrite)
    ArrowheadSize = proxy_property(int, 'ArrowheadSize', AccessMode.ReadWrite)
    ArrowheadType = proxy_property('AcDimArrowheadType', 'ArrowheadType', AccessMode.ReadWrite)
    LeaderLineColor = proxy_property('AcadAcCmColor', 'LeaderLineColor', AccessMode.ReadWrite)
    LeaderLinetype = proxy_property(str, 'LeaderLinetype', AccessMode.ReadWrite)
    LeaderLineWeight = proxy_property('AcLineWeight', 'LeaderLineWeight', AccessMode.ReadWrite)
    LeaderType = proxy_property('AcMLeaderType', 'LeaderType', AccessMode.ReadWrite)

from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..Base import AppObject
from ...Types.Ge import PyGeVector3d


class AcadSubEntity(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Color: AcadAcCmColor = proxy_property('AcadAcCmColor', 'Color', AccessMode.ReadWrite)
    Hyperlinks: AcadHyperlinks = proxy_property('AcadHyperlinks', 'Hyperlinks', AccessMode.ReadOnly)
    Layer: str = proxy_property(str, 'Layer', AccessMode.ReadOnly)
    Linetype: str = proxy_property(str, 'Linetype', AccessMode.ReadOnly)
    LinetypeScale: float = proxy_property(float, 'LinetypeScale', AccessMode.ReadOnly)
    Lineweight: AcLineWeight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadOnly)
    ObjectName: str = proxy_property(str, 'ObjectName', AccessMode.ReadOnly)
    PlotStyleName: str = proxy_property(str, 'PlotStyleName', AccessMode.ReadOnly)

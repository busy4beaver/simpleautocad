from __future__ import annotations

from ..Base import AppObject
from ..Proxy import proxy_property, AccessMode


class AcadSubEntity(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Color = proxy_property('AcColor', 'Color', AccessMode.ReadWrite)
    Hyperlinks = proxy_property('AcadHyperlinks', 'Hyperlinks', AccessMode.ReadOnly)
    Layer = proxy_property(str, 'Layer', AccessMode.ReadWrite)
    Linetype = proxy_property(str, 'Linetype', AccessMode.ReadWrite)
    LinetypeScale = proxy_property(float, 'LinetypeScale', AccessMode.ReadWrite)
    Lineweight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    ObjectName = proxy_property(str, 'ObjectName', AccessMode.ReadOnly)
    PlotStyleName = proxy_property(str, 'PlotStyleName', AccessMode.ReadWrite)

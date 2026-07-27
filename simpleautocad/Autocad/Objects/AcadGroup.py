from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import IAcadObjectCollection
from ...Types.VarType import vObjectArray


class AcadGroup(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Layer = proxy_property(str, 'Layer', AccessMode.WriteOnly)
    Linetype = proxy_property(str, 'Linetype', AccessMode.WriteOnly)
    LinetypeScale = proxy_property(float, 'LinetypeScale', AccessMode.WriteOnly)
    Lineweight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    Material = proxy_property(str, 'Material', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    PlotStyleName = proxy_property(str, 'PlotStyleName', AccessMode.WriteOnly)
    TrueColor = proxy_property('AcadAcCmColor', 'TrueColor', AccessMode.WriteOnly)
    Visible = proxy_property(bool, 'Visible', AccessMode.WriteOnly)

    def AppendItems(self, Objects: vObjectArray) -> None:
        self._obj.AppendItems(Objects())

    def Highlight(self, HighlightFlag: bool) -> None:
        self._obj.Highlight(HighlightFlag)

    def RemoveItems(self, Objects: vObjectArray) -> None:
        self._obj.RemoveItems(Objects())

    def Update(self) -> None:
        self._obj.Update()

from __future__ import annotations

from typing import TYPE_CHECKING

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import IAcadObjectCollection
from ...Types.VarType import vObjectArray
from ...Types.Ac import AcLineWeight

if TYPE_CHECKING:
    from .AcadAcCmColor import AcadAcCmColor


class AcadGroup(IAcadObjectCollection):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Layer: str = proxy_property(str, 'Layer', AccessMode.WriteOnly)
    Linetype: str = proxy_property(str, 'Linetype', AccessMode.WriteOnly)
    LinetypeScale: float = proxy_property(float, 'LinetypeScale', AccessMode.WriteOnly)
    Lineweight: AcLineWeight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    Material: str = proxy_property(str, 'Material', AccessMode.ReadWrite)
    Name: str = proxy_property(str, 'Name', AccessMode.ReadWrite)
    PlotStyleName: str = proxy_property(str, 'PlotStyleName', AccessMode.WriteOnly)
    TrueColor: AcadAcCmColor = proxy_property('AcadAcCmColor', 'TrueColor', AccessMode.WriteOnly)
    Visible: bool = proxy_property(bool, 'Visible', AccessMode.WriteOnly)

    def AppendItems(self, Objects: vObjectArray) -> None:
        self._obj.AppendItems(Objects())

    def Highlight(self, HighlightFlag: bool) -> None:
        self._obj.Highlight(HighlightFlag)

    def RemoveItems(self, Objects: vObjectArray) -> None:
        self._obj.RemoveItems(Objects())

    def Update(self) -> None:
        self._obj.Update()

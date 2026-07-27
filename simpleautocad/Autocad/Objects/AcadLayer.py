from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadLayer(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Application = proxy_property('AcadApplication', 'Application', AccessMode.ReadOnly)
    Description = proxy_property(str, 'Description', AccessMode.ReadWrite)
    Document = proxy_property('AcadDocument', 'Document', AccessMode.ReadOnly)
    Freeze = proxy_property(bool, 'Freeze', AccessMode.ReadWrite)
    Handle = proxy_property(int, 'Handle', AccessMode.ReadOnly)
    HasExtensionDictionary = proxy_property(bool, 'HasExtensionDictionary', AccessMode.ReadOnly)
    LayerOn = proxy_property(bool, 'LayerOn', AccessMode.ReadWrite)
    Linetype = proxy_property(str, 'Linetype', AccessMode.ReadWrite)
    Lineweight = proxy_property('AcLineWeight', 'Lineweight', AccessMode.ReadWrite)
    Lock = proxy_property(bool, 'Lock', AccessMode.ReadWrite)
    Material = proxy_property(str, 'Material', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Plottable = proxy_property(bool, 'Plottable', AccessMode.ReadWrite)
    TrueColor = proxy_property('AcadAcCmColor', 'TrueColor', AccessMode.ReadWrite)
    Used = proxy_property(bool, 'Used', AccessMode.ReadWrite)
    ViewportDefault = proxy_property(bool, 'ViewportDefault', AccessMode.ReadWrite)

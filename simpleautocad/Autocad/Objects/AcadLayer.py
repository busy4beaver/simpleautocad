from __future__ import annotations
from ..Base import *
from ..Proxy import *
from ..AcadObject import *



class AcadLayer(AcadObject):
    def __init__(self, obj) -> None: super().__init__(obj)

    Application: AcadApplication = proxy_property('AcadApplication','Application', AccessMode.ReadOnly)
    Description: str = proxy_property(str,'Description',AccessMode.ReadWrite)
    Document: AcadDocument = proxy_property('AcadDocument','Document',AccessMode.ReadOnly)
    Freeze: bool = proxy_property(bool,'Freeze',AccessMode.ReadWrite)
    Handle: int = proxy_property(int,'Handle',AccessMode.ReadOnly)
    HasExtensionDictionary: bool = proxy_property(bool,'HasExtensionDictionary',AccessMode.ReadOnly)
    LayerOn: bool = proxy_property(bool,'LayerOn',AccessMode.ReadWrite)
    Linetype: str = proxy_property(str,'Linetype',AccessMode.ReadWrite)
    Lineweight: AcLineWeight = proxy_property('AcLineWeight','Lineweight',AccessMode.ReadWrite)
    Lock: bool = proxy_property(bool,'Lock',AccessMode.ReadWrite)
    Material: str = proxy_property(str,'Material',AccessMode.ReadWrite)
    Name: str = proxy_property(str,'Name',AccessMode.ReadWrite)
    Plottable: bool = proxy_property(bool,'Plottable',AccessMode.ReadWrite)
    TrueColor: AcadAcCmColor  = proxy_property('AcadAcCmColor','TrueColor',AccessMode.ReadWrite)
    Used: bool  = proxy_property(bool,'Used',AccessMode.ReadWrite)
    ViewportDefault: bool  = proxy_property(bool,'ViewportDefault',AccessMode.ReadWrite)


# class acDefaultLinetype(Enum):
#     Continuous = 'Continuous'
#     ByLayer = 'ByLayer'
#     ByBlock = 'ByBlock'

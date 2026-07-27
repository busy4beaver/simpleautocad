from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadPointCloudEx(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    ColorScheme = proxy_property(str, 'ColorScheme', AccessMode.ReadWrite)
    Geolocate = proxy_property(bool, 'Geolocate', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    Locked = proxy_property(bool, 'Locked', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Path = proxy_property(str, 'Path', AccessMode.ReadOnly)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    Scale = proxy_property(float, 'Scale', AccessMode.ReadWrite)
    Segmentation = proxy_property(str, 'Segmentation', AccessMode.ReadOnly)
    ShowCropped = proxy_property(bool, 'ShowCropped', AccessMode.ReadWrite)
    Stylization = proxy_property('AcPointCloudExStylizationType', 'Stylization', AccessMode.ReadWrite)
    Unit = proxy_property(str, 'Unit', AccessMode.ReadOnly)
    UnitFactor = proxy_property(str, 'UnitFactor', AccessMode.ReadOnly)

    def Copy(self) -> AcadPointCloudEx:
        return AcadPointCloudEx(self._obj.Copy())

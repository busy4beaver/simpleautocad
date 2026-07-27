from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity


class AcadPointCloud(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    InsertionPoint = proxy_property('PyGePoint3d', 'InsertionPoint', AccessMode.ReadWrite)
    IntensityColorScheme = proxy_property('AcPointCloudIntensityStyle', 'IntensityColorScheme', AccessMode.ReadWrite)
    Locked = proxy_property(bool, 'Locked', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadWrite)
    Path = proxy_property(str, 'Path', AccessMode.ReadOnly)
    Rotation = proxy_property(float, 'Rotation', AccessMode.ReadWrite)
    Scale = proxy_property(float, 'Scale', AccessMode.ReadWrite)
    ShowClipped = proxy_property(bool, 'ShowClipped', AccessMode.ReadWrite)
    ShowIntensity = proxy_property(bool, 'ShowIntensity', AccessMode.ReadWrite)
    Stylization = proxy_property('AcPointCloudStylizationType', 'Stylization', AccessMode.ReadWrite)
    Unit = proxy_property(str, 'Unit', AccessMode.ReadOnly)
    UnitFactor = proxy_property(str, 'UnitFactor', AccessMode.ReadOnly)
    UseEntityColor = proxy_property('AcPointCloudColorType', 'UseEntityColor', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def Copy(self) -> AcadPointCloud:
        return AcadPointCloud(self._obj.Copy())

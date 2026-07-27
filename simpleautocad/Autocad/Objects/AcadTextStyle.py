from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadObject import AcadObject


class AcadTextStyle(AcadObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    BigFontFile = proxy_property(str, 'BigFontFile', AccessMode.ReadWrite)
    FontFile = proxy_property(str, 'FontFile', AccessMode.ReadWrite)
    Height = proxy_property(float, 'Height', AccessMode.ReadWrite)
    LastHeight = proxy_property(float, 'LastHeight', AccessMode.ReadWrite)
    Name = proxy_property(str, 'Name', AccessMode.ReadOnly)
    ObliqueAngle = proxy_property(float, 'ObliqueAngle', AccessMode.ReadWrite)
    TextGenerationFlag = proxy_property('AcTextGenerationFlag', 'TextGenerationFlag', AccessMode.ReadWrite)
    Width = proxy_property(float, 'Width', AccessMode.ReadWrite)

    def GetFont(self) -> tuple:
        Typeface, Bold, Italic, CharSet, PitchAndFamily = self._obj.GetFont()
        return Typeface, Bold, Italic, CharSet, PitchAndFamily

    def SetFont(
        self, Typeface: str, Bold: bool, Italic: bool, CharSet: int, PitchAndFamily: int
    ) -> None:
        self._obj.SetFont(Typeface, Bold, Italic, CharSet, PitchAndFamily)

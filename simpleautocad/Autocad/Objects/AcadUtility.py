from __future__ import annotations

from enum import IntEnum

from ..Base import AppObject
from ..AcadObject import AcadObject
from ...Types.Ge import PyGePoint3d, PyGeVector3d
from ...Types.VarType import vObjectEmpty


class AcadUtility(AppObject):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    def AngleFromXAxis(self, Point1: PyGePoint3d, Point2: PyGePoint3d) -> float:
        return self._obj.AngleFromXAxis(Point1(), Point2())

    def AngleToReal(self, Angle: str, Unit) -> float:
        return self._obj.AngleToReal(Angle, Unit)

    def AngleToString(self, Angle: float, Unit, Precision: int) -> str:
        return self._obj.AngleToString(Angle, Unit, Precision)

    def CreateTypedArray(self, Type, Value1, *args):
        VarArr = vObjectEmpty
        self._obj.CreateTypedArray(VarArr, Type, Value1, *args)
        return VarArr

    def DistanceToReal(self, Distance: str, Unit) -> float:
        return self._obj.DistanceToReal(Distance, Unit)

    def GetAngle(self, Point: PyGePoint3d = None, Prompt: str = '') -> float:
        if Point is None:
            return self._obj.GetAngle()
        return self._obj.GetAngle(Point(), Prompt)

    def GetCorner(self, Point: PyGePoint3d, Prompt: str = '') -> tuple:
        return self._obj.GetCorner(Point(), Prompt)

    def GetDistance(self, Point: PyGePoint3d = None, Prompt: str = None) -> float:
        return self._obj.GetDistance(Point(), Prompt)

    def GetEntity(self, Prompt: str = '') -> tuple:
        Object, PickedPoint = self._obj.GetEntity()
        return Object, PickedPoint

    def GetInput(self) -> str:
        return self._obj.GetInput()

    def GetInteger(self, Prompt: str = '') -> int:
        return self._obj.GetInteger(Prompt)

    def GetKeyword(self, Prompt: str = '') -> str:
        return self._obj.GetKeyword(Prompt)

    def GetObjectIdString(self, acadObject: AcadObject, bHex: bool) -> str:
        return self._obj.GetObjectIdString(acadObject(), int(bHex))

    def GetOrientation(self, Point: PyGePoint3d, Prompt: str = '') -> float:
        return self._obj.GetOrientation(Point(), Prompt)

    def GetPoint(self, Point: PyGePoint3d = None, Prompt: str = '') -> PyGePoint3d:
        if Point is None:
            return PyGePoint3d(self._obj.GetPoint())
        return PyGePoint3d(self._obj.GetPoint(Point, Prompt))

    def GetReal(self, Prompt: str = '') -> float:
        return self._obj.GetReal(Prompt)

    def GetRemoteFile(self, URL: str, IgnoreCache: bool):
        LocalFile = ''
        self._obj.GetRemoteFile(URL, LocalFile, IgnoreCache)
        return LocalFile

    def GetString(self, HasSpaces: int, Prompt: str = ''):
        return self._obj.GetString(HasSpaces, Prompt)

    def GetSubEntity(self, Prompt: str = '') -> tuple:
        Object, PickedPoint, TransMatrix, ContextData = self._obj.GetSubEntity()
        return Object, PickedPoint, TransMatrix, ContextData

    def InitializeUserInput(self, Bits: int, Keyword: str = None) -> None:
        if Keyword:
            self._obj.InitializeUserInput(Bits, Keyword)
        else:
            self._obj.InitializeUserInput(Bits)

    def IsRemoteFile(self, LocalFile: str, URL: str) -> bool:
        return self._obj.IsRemoteFile(LocalFile, URL)

    def IsURL(self, URL: str) -> bool:
        return self._obj.IsURL(URL)

    def LaunchBrowserDialog(
        self,
        DialogTitle: str,
        OpenButtonCaption: str,
        StartPageURL: str,
        RegistryRootKey: str,
        OpenButtonAlwaysEnabled: bool,
    ) -> bool:
        SelectedURL = ''
        return self._obj.LaunchBrowserDialog(
            SelectedURL,
            DialogTitle,
            OpenButtonCaption,
            StartPageURL,
            RegistryRootKey,
            OpenButtonAlwaysEnabled,
        )

    def PolarPoint(self, Point: PyGePoint3d, Angle: float, Distance: float) -> PyGePoint3d:
        return PyGePoint3d(self._obj.PolarPoint(Point(), Angle, Distance))

    def Prompt(self, Message: str) -> None:
        self._obj.Prompt(Message)

    def PutRemoteFile(self, URL: str, LocalFile: str) -> None:
        self._obj.PutRemoteFile(URL, LocalFile)

    def RealToString(self, Value: float, Unit, Precision: int) -> str:
        return self._obj.RealToString(Value, Unit, Precision)

    def SendModelessOperationEnded(self) -> str:
        return self._obj.SendModelessOperationEnded()

    def SendModelessOperationStart(self, Context: str) -> None:
        self._obj.SendModelessOperationStart(Context)

    def TranslateCoordinates(
        self,
        Point: PyGePoint3d,
        FromCoordSystem,
        ToCoordSystem,
        Displacement: int,
        OCSNormal: PyGeVector3d = None,
    ) -> tuple:
        if OCSNormal:
            return self._obj.TranslateCoordinates(
                Point(), FromCoordSystem, ToCoordSystem, Displacement, OCSNormal()
            )
        return self._obj.TranslateCoordinates(
            Point(), FromCoordSystem, ToCoordSystem, Displacement, OCSNormal
        )


class VbVarType(IntEnum):
    vbBoolean = 11
    vbInteger = 2
    vbLong = 3
    vbSingle = 4
    vbDouble = 5

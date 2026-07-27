from __future__ import annotations

from ..Proxy import proxy_property, AccessMode
from ..AcadEntity import AcadEntity
from ...Types.Ge import PyGePoint3d


class AcadSpline(AcadEntity):
    def __init__(self, obj) -> None:
        super().__init__(obj)

    Area = proxy_property(float, 'Area', AccessMode.ReadOnly)
    Closed = proxy_property(bool, 'Closed', AccessMode.ReadOnly)
    Closed2 = proxy_property(bool, 'Closed2', AccessMode.ReadWrite)
    ControlPoints = proxy_property('PyGePoint3dArray', 'ControlPoints', AccessMode.ReadWrite)
    Degree = proxy_property(int, 'Degree', AccessMode.ReadOnly)
    Degree2 = proxy_property(int, 'Degree2', AccessMode.ReadWrite)
    EndTangent = proxy_property('PyGeVector3d', 'EndTangent', AccessMode.ReadWrite)
    FitPoints = proxy_property('PyGePoint3dArray', 'FitPoints', AccessMode.ReadWrite)
    FitTolerance = proxy_property(float, 'FitTolerance', AccessMode.ReadWrite)
    IsPeriodic = proxy_property(bool, 'IsPeriodic', AccessMode.ReadOnly)
    IsPlanar = proxy_property(bool, 'IsPlanar', AccessMode.ReadOnly)
    IsRational = proxy_property(bool, 'IsRational', AccessMode.ReadOnly)
    KnotParameterization = proxy_property('AcSplineKnotParameterizationType', 'KnotParameterization', AccessMode.ReadWrite)
    Knots = proxy_property('PyGeVector3d', 'Knots', AccessMode.ReadWrite)
    NumberOfControlPoints = proxy_property(int, 'NumberOfControlPoints', AccessMode.ReadOnly)
    NumberOfFitPoints = proxy_property(int, 'NumberOfFitPoints', AccessMode.ReadOnly)
    SplineFrame = proxy_property('AcSplineFrameType', 'SplineFrame', AccessMode.ReadWrite)
    SplineMethod = proxy_property('AcSplineMethodType', 'SplineMethod', AccessMode.ReadWrite)
    StartTangent = proxy_property('PyGeVector3d', 'StartTangent', AccessMode.ReadWrite)
    Weights = proxy_property('PyGeVector3d', 'Weights', AccessMode.ReadWrite)

    def AddFitPoint(self, Index: int, FitPoint: PyGePoint3d) -> None:
        self._obj.AddFitPoint(Index, FitPoint())

    def Copy(self) -> AcadSpline:
        return AcadSpline(self._obj.Copy())

    def DeleteFitPoint(self, Index: int) -> None:
        self._obj.DeleteFitPoint(Index)

    def ElevateOrder(self, Order: int) -> None:
        self._obj.ElevateOrder(Order)

    def GetControlPoint(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.GetControlPoint(Index))

    def GetFitPoint(self, Index: int) -> PyGePoint3d:
        return PyGePoint3d(self._obj.GetFitPoint(Index))

    def GetWeight(self, Index: int) -> int:
        return self._obj.GetWeight(Index)

    def Offset(self, Distance: float) -> AcadSpline:
        return AcadSpline(self._obj.Offset(Distance))

    def PurgeFitData(self) -> None:
        self._obj.PurgeFitData()

    def Reverse(self) -> None:
        self._obj.Reverse()

    def SetControlPoint(self, Index: int, Value: PyGePoint3d) -> None:
        self._obj.SetControlPoint(Index, Value())

    def SetFitPoint(self, Index: int, Value: PyGePoint3d) -> None:
        self._obj.SetFitPoint(Index, Value())

    def SetWeight(self, Index: int, Weight: float) -> None:
        self._obj.SetWeight(Index, Weight)

from __future__ import annotations

from abc import ABC, abstractmethod

from win32com.client import CDispatch

from .Autocad.Base import get_clsid, create_new_instance_explicitly
from .Autocad.AcadObject import AcadObject
from .Autocad.Objects.AcadApplication import AcadApplication
from .Autocad.Objects.AcadAcCmColor import AcadAcCmColor
from .Autocad.Objects.AcadLayerStateManager import AcadLayerStateManager
from .Autocad.Objects.AcadSecurityParams import AcadSecurityParams
from .Autocad.Objects.AcadXRecord import AcadXRecord
from .Autocad.Objects.AcadDynamicBlockReferenceProperty import (
    AcadDynamicBlockReferenceProperty,
)
from .Autocad.Objects.AcadModelSpace import AcadModelSpace
from .Autocad.Objects.AcadPaperSpace import AcadPaperSpace
from .Autocad.Objects.AcadBlock import AcadBlock
from .Autocad.Entities.Acad3DFace import Acad3DFace
from .Autocad.Entities.Acad3DPolyline import Acad3DPolyline
from .Autocad.Entities.Acad3DSolid import Acad3DSolid
from .Autocad.Entities.AcadArc import AcadArc
from .Autocad.Entities.AcadAttribute import AcadAttribute
from .Autocad.Entities.AcadAttributeReference import AcadAttributeReference
from .Autocad.Entities.AcadBlockReference import AcadBlockReference
from .Autocad.Entities.AcadCircle import AcadCircle
from .Autocad.Entities.AcadDim3PointAngular import AcadDim3PointAngular
from .Autocad.Entities.AcadDimAligned import AcadDimAligned
from .Autocad.Entities.AcadDimDiametric import AcadDimDiametric
from .Autocad.Entities.AcadDimOrdinate import AcadDimOrdinate
from .Autocad.Entities.AcadDimRadial import AcadDimRadial
from .Autocad.Entities.AcadDimRotated import AcadDimRotated
from .Autocad.Entities.AcadEllipse import AcadEllipse
from .Autocad.Entities.AcadHatch import AcadHatch
from .Autocad.Entities.AcadLeader import AcadLeader
from .Autocad.Entities.AcadLine import AcadLine
from .Autocad.Entities.AcadLWPolyline import AcadLWPolyline
from .Autocad.Entities.AcadMInsertBlock import AcadMInsertBlock
from .Autocad.Entities.AcadMLeader import AcadMLeader
from .Autocad.Entities.AcadMLine import AcadMLine
from .Autocad.Entities.AcadMtext import AcadMtext
from .Autocad.Entities.AcadPoint import AcadPoint
from .Autocad.Entities.AcadPolyfaceMesh import AcadPolyfaceMesh
from .Autocad.Entities.AcadPolygonMesh import AcadPolygonMesh
from .Autocad.Entities.AcadPolyline import AcadPolyline
from .Autocad.Entities.AcadRasterImage import AcadRasterImage
from .Autocad.Entities.AcadRay import AcadRay
from .Autocad.Entities.AcadRegion import AcadRegion
from .Autocad.Entities.AcadSection import AcadSection
from .Autocad.Entities.AcadShape import AcadShape
from .Autocad.Entities.AcadSolid import AcadSolid
from .Autocad.Entities.AcadSpline import AcadSpline
from .Autocad.Entities.AcadTable import AcadTable
from .Autocad.Entities.AcadText import AcadText
from .Autocad.Entities.AcadTolerance import AcadTolerance
from .Autocad.Entities.AcadTrace import AcadTrace
from .Autocad.Entities.AcadWipeout import AcadWipeout
from .Autocad.Entities.AcadXline import AcadXline
from .Types.Ge import PyGePoint3d
from .Types.VarType import Variant
from .Types.Xdata import XDataManager


class AutoCAD(AcadApplication):
    _ACAD_TYPE_MAP = {
        'AcDbFace': Acad3DFace,
        'AcDbPolygonMesh': AcadPolygonMesh,
        'AcDb3dPolyline': Acad3DPolyline,
        'AcDbArc': AcadArc,
        'AcDbAttributeDefinition': AcadAttribute,
        'AcDb3dSolid': Acad3DSolid,
        'AcDbCircle': AcadCircle,
        'AcDb3PointAngularDimension': AcadDim3PointAngular,
        'AcDbAlignedDimension': AcadDimAligned,
        'AcDbDiametricDimension': AcadDimDiametric,
        'AcDbOrdinateDimension': AcadDimOrdinate,
        'AcDbRadialDimension': AcadDimRadial,
        'AcDbRotatedDimension': AcadDimRotated,
        'AcDbEllipse': AcadEllipse,
        'AcDbHatch': AcadHatch,
        'AcDbLeader': AcadLeader,
        'AcDbMText': AcadMtext,
        'AcDbText': AcadText,
        'AcDbPolyline': AcadLWPolyline,
        'AcDbLine': AcadLine,
        'AcDbMInsertBlock': AcadMInsertBlock,
        'AcDbMLeader': AcadMLeader,
        'AcDbMline': AcadMLine,
        'AcDbPoint': AcadPoint,
        'AcDbPolyFaceMesh': AcadPolyfaceMesh,
        'AcDb2dPolyline': AcadPolyline,
        'AcDbRasterImage': AcadRasterImage,
        'AcDbRay': AcadRay,
        'AcDbRegion': AcadRegion,
        'AcDbSection': AcadSection,
        'AcDbShape': AcadShape,
        'AcDbSolid': AcadSolid,
        'AcDbSpline': AcadSpline,
        'AcDbTable': AcadTable,
        'AcDbFcf': AcadTolerance,
        'AcDbTrace': AcadTrace,
        'AcDbXline': AcadXline,
        'AcDbWipeout': AcadWipeout,
        'AcDbXrecord': AcadXRecord,
    }

    def __init__(self, dispatch_object: CDispatch = None):
        super().__init__(dispatch_object)

    def uGetAcadAcCmColor(self) -> AcadAcCmColor:
        progID = AcadApplication.__app_full_name__.replace('Application', 'AcCmColor')
        obj = self.GetInterfaceObject(progID)
        return AcadAcCmColor(obj)

    def uGetAcadLayerStateManager(self) -> AcadLayerStateManager:
        progID = AcadApplication.__app_full_name__.replace(
            'Application', 'AcadLayerStateManager'
        )
        obj = self.GetInterfaceObject(progID)
        return AcadLayerStateManager(obj)

    def uGetAcadSecurityParams(self) -> AcadSecurityParams:
        progID = AcadApplication.__app_full_name__.replace('Application', 'SecurityParams')
        obj = self.GetInterfaceObject(progID)
        return AcadSecurityParams(obj)

    def uSetXData(self, obj: AcadObject, xdm: XDataManager) -> None:
        try:
            obj.Document.RegisteredApplications.Item(xdm.RegAppName)
        except Exception:
            obj.Document.RegisteredApplications.Add(xdm.RegAppName)
        obj.SetXData(xdm.xDataType, xdm.xDataValue)

    def uGetObjectType(self, obj: AcadObject) -> type | None:
        return self._ACAD_TYPE_MAP.get(obj.ObjectName, None)

    @classmethod
    def CreateNewInstance(cls) -> AutoCAD:
        clsid = get_clsid(AcadApplication)
        try:
            return AutoCAD(create_new_instance_explicitly(clsid[1]))
        except Exception as e:
            raise Exception(f'Ошибка запуска приложения: {e}') from e


class BlockReference(ABC):
    def __init__(self, acad_block_reference: AcadBlockReference = None):
        self.acad_block_reference: AcadBlockReference = acad_block_reference
        self.Attributes = self._get_block_attributes(acad_block_reference)
        self.DynamicProperties = self._get_block_dynamic_properties(acad_block_reference)

    @staticmethod
    def _get_block_attributes(
        block_ref: AcadBlockReference,
    ) -> list[AcadAttributeReference] | None:
        attrib = None
        if isinstance(block_ref, AcadBlockReference) and block_ref.HasAttributes:
            obj_arr = block_ref.GetAttributes()
            attrib = [AcadAttributeReference(attr) for attr in obj_arr]
        return attrib

    @staticmethod
    def _get_block_dynamic_properties(
        block_ref: AcadBlockReference,
    ) -> list[AcadDynamicBlockReferenceProperty] | None:
        dynprop = None
        if isinstance(block_ref, AcadBlockReference) and block_ref.IsDynamicBlock:
            dyn_arr = block_ref.GetDynamicBlockProperties()
            dynprop = [AcadDynamicBlockReferenceProperty(dattr) for dattr in dyn_arr]
        return dynprop

    @classmethod
    def read_from(cls, space: AcadModelSpace | AcadPaperSpace):
        for v in space:
            blk_ref = AcadBlockReference(v)
            if (
                blk_ref.ObjectName == 'AcDbBlockReference'
                and blk_ref.EffectiveName == cls.BlockName
            ):
                yield cls(blk_ref)

    @property
    @abstractmethod
    def BlockName(self) -> str: ...

    def insert(
        self,
        insertion_point: PyGePoint3d,
        space: AcadModelSpace | AcadPaperSpace | AcadBlock,
    ) -> AcadBlockReference:
        block = space.InsertBlock(insertion_point, self.BlockName)
        if self.acad_block_reference:
            return block

        self.Attributes = self._get_block_attributes(block)
        self.DynamicProperties = self._get_block_dynamic_properties(block)
        self.acad_block_reference = block
        return block

    def attribute(self, tag_name: str) -> AcadAttributeReference | None:
        if self.acad_block_reference and self.Attributes:
            for attr in self.Attributes:
                if attr.TagString == tag_name:
                    return attr
        return None

    def dynamic_property(
        self, dyn_name: str
    ) -> AcadDynamicBlockReferenceProperty | None:
        if self.acad_block_reference and self.DynamicProperties:
            for dyn in self.DynamicProperties:
                if dyn.PropertyName == dyn_name:
                    return dyn
        return None

    def get_attribute_value(self, tag_name) -> str | None:
        attr = self.attribute(tag_name)
        if attr:
            return attr.TextString
        return None

    def set_attribute_value(self, tag_name, value) -> None:
        attr = self.attribute(tag_name)
        if attr:
            attr.TextString = value

    def get_dynamic_property_value(self, dyn_name: str) -> Variant | None:
        dyn = self.dynamic_property(dyn_name)
        if dyn:
            return dyn.Value
        return None

    def set_dynamic_property_value(self, dyn_name, value) -> None:
        dyn = self.dynamic_property(dyn_name)
        if dyn:
            dyn.Value = value

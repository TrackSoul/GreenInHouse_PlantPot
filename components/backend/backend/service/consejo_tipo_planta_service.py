from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import ConsejoTipoPlanta
from backend.data.db.resultsets import ConsejoTipoPlantaSet
from common.data.util import ConsejoTipoPlanta as ConsejoTipoPlantaCommon, TipoPlanta as TipoPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class ConsejoTipoPlantaService():
    
    @staticmethod
    def create(esquema: Esquema, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float=0, horas_maximas:float=0) -> ConsejoTipoPlantaCommon:
        session: Session = esquema.new_session()
        out: ConsejoTipoPlantaCommon = None
        try:
            nuevo_consejo: ConsejoTipoPlanta = ConsejoTipoPlantaSet.create(session, descripcion, tipo_planta, zona_consejo,
                                                                            tipo_medida, unidad_medida, valor_minimo,
                                                                            valor_maximo, horas_minimas, horas_maximas)                                                                         
            out= ConsejoTipoPlantaCommon(nuevo_consejo.descripcion, nuevo_consejo.nombre_elemento, nuevo_consejo.zona_consejo,
                                         nuevo_consejo.tipo_medida, nuevo_consejo.unidad_medida, nuevo_consejo.valor_minimo,
                                         nuevo_consejo.valor_maximo, nuevo_consejo.horas_minimas, nuevo_consejo.horas_maximas)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, consejo: ConsejoTipoPlantaCommon) -> ConsejoTipoPlantaCommon:
        return ConsejoTipoPlantaService.create(esquema=esquema, descripcion=consejo.getDescripcion(), 
                                    tipo_planta=consejo.getNombreElemento(), zona_consejo=consejo.getZonaConsejo(), 
                                    tipo_medida=consejo.getTipoMedida(), unidad_medida=consejo.getUnidadMedida(), 
                                    valor_minimo=consejo.getValorMinimo(), valor_maximo=consejo.getValorMaximo(), 
                                    horas_minimas=consejo.getHorasMinimas(), horas_maximas=consejo.getHorasMaximas())

    @staticmethod
    def exists(esquema: Esquema, tipo_planta: str, zona_consejo:ZonaSensor, tipo_medida:TipoMedida) -> bool:
        session: Session = esquema.new_session()
        consejo_existe: bool = ConsejoTipoPlantaSet.get(session, tipo_planta, zona_consejo, tipo_medida)
        esquema.remove_session()
        return consejo_existe

    @staticmethod
    def listAll(esquema: Esquema) -> List[ConsejoTipoPlantaCommon]:
        out: List[ConsejoTipoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoTipoPlanta] = ConsejoTipoPlantaSet.listAll(session)
        for consejo in consejos:
            out.append(ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromTypePlant(esquema: Esquema, tipo_planta: str) -> List[ConsejoTipoPlantaCommon]:
        out: List[ConsejoTipoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoTipoPlanta] = ConsejoTipoPlantaSet.listAllFromTypePlant(session, tipo_planta)
        for consejo in consejos:
            out.append(ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out
    
    @staticmethod
    def listAllFromZone(esquema: Esquema, zona_consejo: ZonaSensor) -> List[ConsejoTipoPlantaCommon]:
        out: List[ConsejoTipoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoTipoPlanta] = ConsejoTipoPlantaSet.listAllFromZone(session, zona_consejo)
        for consejo in consejos:
            out.append(ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromTypeMeasure(esquema: Esquema, tipo_medida: TipoMedida) -> List[ConsejoTipoPlantaCommon]:
        out: List[ConsejoTipoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoTipoPlanta] = ConsejoTipoPlantaSet.listAllFromTypeMeasure(session, tipo_medida)
        for consejo in consejos:
            out.append(ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out
    
    @staticmethod
    def listAllFromTypePlantAndZone(esquema: Esquema, tipo_planta: str, zona_consejo: ZonaSensor) -> List[ConsejoTipoPlantaCommon]:
        out: List[ConsejoTipoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoTipoPlanta] = ConsejoTipoPlantaSet.listAllFromTypePlantAndZone(session, tipo_planta, zona_consejo)
        for consejo in consejos:
            out.append(ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromTypePlantAndTypeMeasure(esquema: Esquema, tipo_planta: str, tipo_medida: TipoMedida) -> List[ConsejoTipoPlantaCommon]:
        out: List[ConsejoTipoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoTipoPlanta] = ConsejoTipoPlantaSet.listAllFromTypePlantAndTypeMeasure(session, tipo_planta, tipo_medida)
        for consejo in consejos:
            out.append(ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, tipo_planta: str, zona_consejo:ZonaSensor, tipo_medida:TipoMedida) -> ConsejoTipoPlantaCommon:
        session: Session = esquema.new_session()
        consejo: ConsejoTipoPlanta = ConsejoTipoPlantaSet.get(session, tipo_planta, zona_consejo, tipo_medida)
        out= ConsejoTipoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                    consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                    consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float) -> ConsejoTipoPlantaCommon:
        session: Session = esquema.new_session()
        out: ConsejoTipoPlantaCommon = None
        try:
            consejo_modificado: ConsejoTipoPlanta = ConsejoTipoPlantaSet.update(session, descripcion, tipo_planta, zona_consejo,
                                                                                tipo_medida, unidad_medida, valor_minimo,
                                                                                valor_maximo, horas_minimas, horas_maximas)
            out= ConsejoTipoPlantaCommon(consejo_modificado.descripcion, consejo_modificado.nombre_elemento, consejo_modificado.zona_consejo,
                                         consejo_modificado.tipo_medida, consejo_modificado.unidad_medida, consejo_modificado.valor_minimo,
                                         consejo_modificado.valor_maximo, consejo_modificado.horas_minimas, consejo_modificado.horas_maximas)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, consejo: ConsejoTipoPlantaCommon) -> ConsejoTipoPlantaCommon:
        return ConsejoTipoPlantaService.update(esquema=esquema, descripcion=consejo.getDescripcion(), 
                                    tipo_planta=consejo.getTipoPlanta(), zona_consejo=consejo.getZonaConsejo(), 
                                    tipo_medida=consejo.getTipoMedida(), unidad_medida=consejo.getUnidadMedida(), 
                                    valor_minimo=consejo.getValorMinimo(), valor_maximo=consejo.getValorMaximo(), 
                                    horas_minimas=consejo.getHorasMinimas(), horas_maximas=consejo.getHorasMaximas())



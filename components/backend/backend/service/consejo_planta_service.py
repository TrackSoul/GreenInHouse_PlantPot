#Author: Oscar Valverde Escobar

from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import ConsejoPlanta
from backend.data.db.resultsets import ConsejoPlantaSet
from common.data.util import ConsejoPlanta as ConsejoPlantaCommon, Planta as PlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class ConsejoPlantaService():
    
    @staticmethod
    def create(esquema: Esquema, descripcion: str, nombre_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float=0, horas_maximas:float=0) -> ConsejoPlantaCommon:
        session: Session = esquema.new_session()
        out: ConsejoPlantaCommon = None
        try:
            nuevo_consejo: ConsejoPlanta = ConsejoPlantaSet.create(session, descripcion, nombre_planta, zona_consejo,
                                                                            tipo_medida, unidad_medida, valor_minimo,
                                                                            valor_maximo, horas_minimas, horas_maximas)                                                                         
            out= ConsejoPlantaCommon(nuevo_consejo.descripcion, nuevo_consejo.nombre_elemento, nuevo_consejo.zona_consejo,
                                         nuevo_consejo.tipo_medida, nuevo_consejo.unidad_medida, nuevo_consejo.valor_minimo,
                                         nuevo_consejo.valor_maximo, nuevo_consejo.horas_minimas, nuevo_consejo.horas_maximas)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, consejo: ConsejoPlantaCommon) -> ConsejoPlantaCommon:
        return ConsejoPlantaService.create(esquema=esquema, descripcion=consejo.getDescripcion(), 
                                    nombre_planta=consejo.getNombreElemento(), zona_consejo=consejo.getZonaConsejo(), 
                                    tipo_medida=consejo.getTipoMedida(), unidad_medida=consejo.getUnidadMedida(), 
                                    valor_minimo=consejo.getValorMinimo(), valor_maximo=consejo.getValorMaximo(), 
                                    horas_minimas=consejo.getHorasMinimas(), horas_maximas=consejo.getHorasMaximas())

    @staticmethod
    def exists(esquema: Esquema, nombre_planta: str, zona_consejo:ZonaSensor, tipo_medida:TipoMedida) -> bool:
        session: Session = esquema.new_session()
        consejo_existe: bool = ConsejoPlantaSet.get(session, nombre_planta, zona_consejo, tipo_medida)
        esquema.remove_session()
        return consejo_existe

    @staticmethod
    def listAll(esquema: Esquema) -> List[ConsejoPlantaCommon]:
        out: List[ConsejoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoPlanta] = ConsejoPlantaSet.listAll(session)
        for consejo in consejos:
            out.append(ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromPlant(esquema: Esquema, nombre_planta: str) -> List[ConsejoPlantaCommon]:
        out: List[ConsejoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoPlanta] = ConsejoPlantaSet.listAllFromPlant(session, nombre_planta)
        for consejo in consejos:
            out.append(ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out
    
    @staticmethod
    def listAllFromZone(esquema: Esquema, zona_consejo: ZonaSensor) -> List[ConsejoPlantaCommon]:
        out: List[ConsejoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoPlanta] = ConsejoPlantaSet.listAllFromZone(session, zona_consejo)
        for consejo in consejos:
            out.append(ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromTypeMeasure(esquema: Esquema, tipo_medida: TipoMedida) -> List[ConsejoPlantaCommon]:
        out: List[ConsejoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoPlanta] = ConsejoPlantaSet.listAllFromTypeMeasure(session, tipo_medida)
        for consejo in consejos:
            out.append(ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out
    
    @staticmethod
    def listAllFromPlantAndZone(esquema: Esquema, nombre_planta: str, zona_consejo: ZonaSensor) -> List[ConsejoPlantaCommon]:
        out: List[ConsejoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoPlanta] = ConsejoPlantaSet.listAllFromPlantAndZone(session, nombre_planta, zona_consejo)
        for consejo in consejos:
            out.append(ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromPlantAndTypeMeasure(esquema: Esquema, nombre_planta: str, tipo_medida: TipoMedida) -> List[ConsejoPlantaCommon]:
        out: List[ConsejoPlantaCommon] = []
        session: Session = esquema.new_session()
        consejos: List[ConsejoPlanta] = ConsejoPlantaSet.listAllFromPlantAndTypeMeasure(session, nombre_planta, tipo_medida)
        for consejo in consejos:
            out.append(ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                                consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                                consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, nombre_planta: str, zona_consejo:ZonaSensor, tipo_medida:TipoMedida) -> ConsejoPlantaCommon:
        session: Session = esquema.new_session()
        consejo: ConsejoPlanta = ConsejoPlantaSet.get(session, nombre_planta, zona_consejo, tipo_medida)
        out= ConsejoPlantaCommon(consejo.descripcion, consejo.nombre_elemento, consejo.zona_consejo,
                                    consejo.tipo_medida, consejo.unidad_medida, consejo.valor_minimo,
                                    consejo.valor_maximo, consejo.horas_minimas, consejo.horas_maximas)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, descripcion: str, nombre_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float) -> ConsejoPlantaCommon:
        session: Session = esquema.new_session()
        out: ConsejoPlantaCommon = None
        try:
            consejo_modificado: ConsejoPlanta = ConsejoPlantaSet.update(session, descripcion, nombre_planta, zona_consejo,
                                                                                tipo_medida, unidad_medida, valor_minimo,
                                                                                valor_maximo, horas_minimas, horas_maximas)
            out= ConsejoPlantaCommon(consejo_modificado.descripcion, consejo_modificado.nombre_elemento, consejo_modificado.zona_consejo,
                                         consejo_modificado.tipo_medida, consejo_modificado.unidad_medida, consejo_modificado.valor_minimo,
                                         consejo_modificado.valor_maximo, consejo_modificado.horas_minimas, consejo_modificado.horas_maximas)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, consejo: ConsejoPlantaCommon) -> ConsejoPlantaCommon:
        return ConsejoPlantaService.update(esquema=esquema, descripcion=consejo.getDescripcion(), 
                                    nombre_planta=consejo.getNombreElemento(), zona_consejo=consejo.getZonaConsejo(), 
                                    tipo_medida=consejo.getTipoMedida(), unidad_medida=consejo.getUnidadMedida(), 
                                    valor_minimo=consejo.getValorMinimo(), valor_maximo=consejo.getValorMaximo(), 
                                    horas_minimas=consejo.getHorasMinimas(), horas_maximas=consejo.getHorasMaximas())



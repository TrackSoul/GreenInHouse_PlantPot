from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroPlanta,  RegistroTipoPlanta
from backend.data.db.resultsets import RegistroPlantaSet
from backend.service import SensorPlantaService
from common.data.util import RegistroPlanta as RegistroPlantaCommon

class RegistroPlantaService():

    @staticmethod
    def create(esquema: Esquema, nombre_planta: str, tipo_planta: str, 
                fecha_plantacion: datetime = datetime.now(), fecha_marchitacion: datetime = None) -> RegistroPlantaCommon:
        session: Session = esquema.new_session()
        out: RegistroPlantaCommon = None
        try:
            new_registro_planta: RegistroPlanta = RegistroPlantaSet.create(session, nombre_planta, tipo_planta, 
                                                                           fecha_plantacion, fecha_marchitacion)
            out= RegistroPlantaCommon(new_registro_planta.nombre_planta,new_registro_planta.tipo_planta,
                                      new_registro_planta.fecha_plantacion,new_registro_planta.fecha_marchitacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, registro_planta: RegistroPlantaCommon) -> RegistroPlantaCommon:
        return RegistroPlantaService.create(esquema, registro_planta.getNombrePlanta(), registro_planta.getTipoPlanta())

    @staticmethod
    def exists(esquema: Esquema, nombre_planta: str) -> bool:
        session: Session = esquema.new_session()
        registro_planta_exists: bool = RegistroPlantaSet.get(session, nombre_planta)
        esquema.remove_session()
        return registro_planta_exists

    @staticmethod
    def listAll(esquema: Esquema) -> List[RegistroPlantaCommon]:
        out: List[RegistroPlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[RegistroPlanta] = RegistroPlantaSet.listAll(session)
        for registro_planta in registros_planta:
            out.append(RegistroPlantaCommon(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                            registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActive(esquema: Esquema) -> List[RegistroPlantaCommon]:
        out: List[RegistroPlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[RegistroPlanta] = RegistroPlantaSet.listAllActive(session)
        for registro_planta in registros_planta:
            out.append(RegistroPlantaCommon(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                            registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion))
        esquema.remove_session()
        return out
    
    @staticmethod
    def listAllFromType(esquema: Esquema, tipo_planta: str) -> List[RegistroPlantaCommon]:
        out: List[RegistroPlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[RegistroPlanta] = RegistroPlantaSet.listAllFromType(session, tipo_planta)
        for registro_planta in registros_planta:
            out.append(RegistroPlantaCommon(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                            registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromTypeFromCommon(esquema: Esquema, tipo_planta: RegistroTipoPlanta) -> List[RegistroPlantaCommon]:
        return RegistroPlantaService.listAllFromType(esquema, tipo_planta.getTipoPlanta())

    @staticmethod
    def listAllActiveFromType(esquema: Esquema, tipo_planta: str) -> List[RegistroPlantaCommon]:
        out: List[RegistroPlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[RegistroPlanta] = RegistroPlantaSet.listAllActiveFromType(session, tipo_planta)
        for registro_planta in registros_planta:
            out.append(RegistroPlantaCommon(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                            registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActiveFromTypeFromCommon(esquema: Esquema, tipo_planta: RegistroTipoPlanta) -> List[RegistroPlantaCommon]:
        return RegistroPlantaService.listAllActiveFromType(esquema, tipo_planta.getTipoPlanta())

    @staticmethod
    def get(esquema: Esquema, nombre_planta: str) -> RegistroPlantaCommon:
        session: Session = esquema.new_session()
        registro_planta: RegistroPlantaCommon = RegistroPlantaSet.get(session, nombre_planta)
        out= RegistroPlantaCommon(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                  registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, nombre_planta: str, tipo_planta: str, 
                fecha_plantacion: datetime, fecha_marchitacion: datetime) -> RegistroPlantaCommon:
        session: Session = esquema.new_session()
        out: RegistroPlantaCommon = None
        try:
            registro_planta_modificado: RegistroPlanta = RegistroPlantaSet.update(session, nombre_planta, tipo_planta, 
                                                                           fecha_plantacion, fecha_marchitacion)
            out= RegistroPlantaCommon(registro_planta_modificado.nombre_planta,registro_planta_modificado.tipo_planta,
                                      registro_planta_modificado.fecha_plantacion,registro_planta_modificado.fecha_marchitacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, registro_planta: RegistroPlantaCommon) -> RegistroPlantaCommon:
        return RegistroPlantaService.update(esquema, registro_planta.getNombrePlanta(),registro_planta.getTipoPlanta(),
                                            registro_planta.getFechaPlantacion(), registro_planta.getFechaMarchitacion())

    @staticmethod
    def unsubscribe(esquema: Esquema, nombre_planta: str) -> RegistroPlantaCommon:
        planta: RegistroPlantaCommon = RegistroPlantaService.get(esquema, nombre_planta)
        if planta.getFechaMarchitacion() is None:
            planta.setFechaMarchitacion(datetime.now())
            planta = RegistroPlantaService.updateFromCommon(esquema, planta)
        SensorPlantaService.unsubscribeAllFromPlantFromCommon(esquema, planta)
        return planta

    @staticmethod
    def unsubscribeFromCommon(esquema: Esquema, registro_planta: RegistroPlantaCommon) -> RegistroPlantaCommon:
        return RegistroPlantaService.unsubscribe(esquema, registro_planta.getNombrePlanta())

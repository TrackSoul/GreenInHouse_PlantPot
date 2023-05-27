from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import Planta,  TipoPlanta
from backend.data.db.resultsets import PlantaSet
from backend.service import SensorPlantaService, SensorService, ConsejoPlantaService, ConsejoTipoPlantaService
from common.data.util import Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon

class PlantaService():

    @staticmethod
    def create(esquema: Esquema, nombre_planta: str, tipo_planta: str, fecha_plantacion: datetime = datetime.now(),
                 fecha_marchitacion: datetime = None, asociar_sensores_activos = True) -> PlantaCommon:
        session: Session = esquema.new_session()
        out: PlantaCommon = None
        try:
            new_planta: Planta = PlantaSet.create(session, nombre_planta, tipo_planta, 
                                                                           fecha_plantacion, fecha_marchitacion)
            out= PlantaCommon(new_planta.nombre_planta,new_planta.tipo_planta,
                                      new_planta.fecha_plantacion,new_planta.fecha_marchitacion)
            for consejo in ConsejoTipoPlantaService.listAllFromTypePlant(esquema,tipo_planta):
                ConsejoPlantaService.create(esquema, consejo.getDescripcion(), nombre_planta, consejo.getZonaConsejo(), 
                                            consejo.getTipoMedida(), consejo.getUnidadMedida(), consejo.getValorMinimo(), 
                                            consejo.getValorMaximo(), consejo.getHorasMinimas(), consejo.getHorasMaximas())
            if asociar_sensores_activos:
                for sensor in SensorService.listAllActive(esquema):
                    SensorPlantaService.createRelationFromCommon(esquema, sensor, out)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, planta: PlantaCommon) -> PlantaCommon:
        return PlantaService.create(esquema, planta.getNombrePlanta(), planta.getTipoPlanta())

    @staticmethod
    def exists(esquema: Esquema, nombre_planta: str) -> bool:
        session: Session = esquema.new_session()
        planta_exists: bool = PlantaSet.get(session, nombre_planta)
        esquema.remove_session()
        return planta_exists

    @staticmethod
    def listAll(esquema: Esquema) -> List[PlantaCommon]:
        out: List[PlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[Planta] = PlantaSet.listAll(session)
        for planta in registros_planta:
            out.append(PlantaCommon(planta.nombre_planta,planta.tipo_planta,
                                            planta.fecha_plantacion,planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActive(esquema: Esquema) -> List[PlantaCommon]:
        out: List[PlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[Planta] = PlantaSet.listAllActive(session)
        for planta in registros_planta:
            out.append(PlantaCommon(planta.nombre_planta,planta.tipo_planta,
                                            planta.fecha_plantacion,planta.fecha_marchitacion))
        esquema.remove_session()
        return out
    
    @staticmethod
    def listAllFromType(esquema: Esquema, tipo_planta: str) -> List[PlantaCommon]:
        out: List[PlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[Planta] = PlantaSet.listAllFromType(session, tipo_planta)
        for planta in registros_planta:
            out.append(PlantaCommon(planta.nombre_planta,planta.tipo_planta,
                                            planta.fecha_plantacion,planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromTypeFromCommon(esquema: Esquema, tipo_planta: TipoPlanta) -> List[PlantaCommon]:
        return PlantaService.listAllFromType(esquema, tipo_planta.getTipoPlanta())

    @staticmethod
    def listAllActiveFromType(esquema: Esquema, tipo_planta: str) -> List[PlantaCommon]:
        out: List[PlantaCommon] = []
        session: Session = esquema.new_session()
        registros_planta: List[Planta] = PlantaSet.listAllActiveFromType(session, tipo_planta)
        for planta in registros_planta:
            out.append(PlantaCommon(planta.nombre_planta,planta.tipo_planta,
                                            planta.fecha_plantacion,planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActiveFromTypeFromCommon(esquema: Esquema, tipo_planta: TipoPlanta) -> List[PlantaCommon]:
        return PlantaService.listAllActiveFromType(esquema, tipo_planta.getTipoPlanta())

    @staticmethod
    def get(esquema: Esquema, nombre_planta: str) -> PlantaCommon:
        session: Session = esquema.new_session()
        planta: Planta = PlantaSet.get(session, nombre_planta)
        out= PlantaCommon(planta.nombre_planta,planta.tipo_planta,
                                  planta.fecha_plantacion,planta.fecha_marchitacion)
        esquema.remove_session()
        return out
    
    @staticmethod
    def getPlantFromRelationFromCommon(esquema: Esquema, sensor_planta : SensorPlantaCommon) -> PlantaCommon:
        return PlantaService.get(esquema, sensor_planta.getNombrePlanta())

    @staticmethod
    def update(esquema: Esquema, nombre_planta: str, tipo_planta: str, 
                fecha_plantacion: datetime, fecha_marchitacion: datetime) -> PlantaCommon:
        session: Session = esquema.new_session()
        out: PlantaCommon = None
        try:
            planta_modificado: Planta = PlantaSet.update(session, nombre_planta, tipo_planta, 
                                                                           fecha_plantacion, fecha_marchitacion)
            out= PlantaCommon(planta_modificado.nombre_planta,planta_modificado.tipo_planta,
                                      planta_modificado.fecha_plantacion,planta_modificado.fecha_marchitacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, planta: PlantaCommon) -> PlantaCommon:
        return PlantaService.update(esquema, planta.getNombrePlanta(),planta.getTipoPlanta(),
                                            planta.getFechaPlantacion(), planta.getFechaMarchitacion())

    @staticmethod
    def unsubscribe(esquema: Esquema, nombre_planta: str) -> PlantaCommon:
        planta: PlantaCommon = PlantaService.get(esquema, nombre_planta)
        if planta.getFechaMarchitacion() is None:
            planta.setFechaMarchitacion(datetime.now())
            planta = PlantaService.updateFromCommon(esquema, planta)
        SensorPlantaService.unsubscribeAllFromPlantFromCommon(esquema, planta)
        return planta

    @staticmethod
    def unsubscribeFromCommon(esquema: Esquema, planta: PlantaCommon) -> PlantaCommon:
        return PlantaService.unsubscribe(esquema, planta.getNombrePlanta())

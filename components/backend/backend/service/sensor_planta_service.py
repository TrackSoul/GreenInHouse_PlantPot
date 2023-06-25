#Author: Oscar Valverde Escobar

from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import SensorPlanta
from backend.data.db.resultsets import SensorPlantaSet
from common.data.util import SensorPlanta as SensorPlantaCommon, Sensor as SensorCommon, Planta as PlantaCommon
from common.data.util import TipoSensor, ZonaSensor

class SensorPlantaService():

    @staticmethod
    def create(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, 
                               numero_sensor:int, nombre_planta:str = "Sin planta", 
                               fecha_asociacion:datetime = datetime.now() ,fecha_anulacion:datetime = None) -> SensorPlantaCommon:
        session: Session = esquema.new_session()
        out: SensorPlantaCommon = None
        try:
            nuevo_sensor_planta: SensorPlanta = SensorPlantaSet.create(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, nombre_planta, 
                                                                           fecha_asociacion, fecha_anulacion)
            out= SensorPlantaCommon(nuevo_sensor_planta.tipo_sensor, nuevo_sensor_planta.zona_sensor,
                                      nuevo_sensor_planta.numero_sensor, nuevo_sensor_planta.nombre_planta, 
                                      nuevo_sensor_planta.fecha_asociacion, nuevo_sensor_planta.fecha_anulacion, 
                                      nuevo_sensor_planta.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, sensor_planta: SensorPlantaCommon) -> SensorPlantaCommon:
        return SensorPlantaService.create(esquema, sensor_planta.getTipoSensor(), sensor_planta.getZonaSensor(), 
                                          sensor_planta.getNumeroSensor(), sensor_planta.getNombrePlanta())
    
    @staticmethod
    def createRelationFromCommon(esquema: Esquema, sensor: SensorCommon, planta: PlantaCommon) -> SensorPlantaCommon:
        return SensorPlantaService.create(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), 
                                                        sensor.getNumeroSensor(), planta.getNombrePlanta())

    @staticmethod
    def exists(esquema: Esquema, id_:int) -> bool:
        session: Session = esquema.new_session()
        sensor_planta_existe: bool = SensorPlantaSet.get(session, id_)
        esquema.remove_session()
        return sensor_planta_existe
    
    @staticmethod
    def listAll(esquema: Esquema) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        registros_sensor: List[SensorPlanta] = SensorPlantaSet.listAll(session)
        for sensor_planta in registros_sensor:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActive(esquema: Esquema) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        sensores_planta: List[SensorPlanta] = SensorPlantaSet.listAllActive(session)
        for sensor_planta in sensores_planta:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllSensorsFromPlant(esquema: Esquema, nombre_planta: str) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        sensores: List[SensorPlanta] = SensorPlantaSet.listAllSensorsFromPlant(session, nombre_planta)
        for sensor_planta in sensores:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllSensorsFromPlantFromCommon(esquema: Esquema, planta: PlantaCommon) -> List[SensorPlantaCommon]:
        return SensorPlantaService.listAllSensorsFromPlant(esquema, planta.getNombrePlanta())

    @staticmethod
    def listAllActiveSensorsFromPlant(esquema: Esquema, nombre_planta: str) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        sensores: List[SensorPlanta] = SensorPlantaSet.listAllActiveSensorsFromPlant(session, nombre_planta)
        for sensor_planta in sensores:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActiveSensorsFromPlantFromCommon(esquema: Esquema, planta: PlantaCommon) -> List[SensorPlantaCommon]:
        return SensorPlantaService.listAllActiveSensorsFromPlant(esquema, planta.getNombrePlanta())

    @staticmethod
    def listAllSensorsFromPlantBetweenDates(esquema: Esquema, nombre_planta: str, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        relacciones_sensor_planta: List[SensorPlanta] = SensorPlantaSet.listAllSensorsFromPlantBetweenDates(session, nombre_planta, fecha_inicio, fecha_fin)
        for sensor_planta in relacciones_sensor_planta:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllSensorsFromPlantFromCommonBetweenDates(esquema: Esquema, planta: PlantaCommon, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[SensorPlantaCommon]:
        return SensorPlantaService.listAllSensorsFromPlantBetweenDates(esquema, planta.getNombrePlanta(), fecha_inicio, fecha_fin)


    @staticmethod
    def listAllPlantsFromSensor(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        relacciones_sensor_planta: List[SensorPlanta] = SensorPlantaSet.listAllPlantsFromSensor(session, tipo_sensor, zona_sensor, numero_sensor)
        for sensor_planta in relacciones_sensor_planta:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllPlantsFromSensorFromCommon(esquema: Esquema, sensor: SensorCommon) -> List[SensorPlantaCommon]:
        return SensorPlantaService.listAllPlantsFromSensor(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), 
                                                            sensor.getNumeroSensor())

    @staticmethod
    def listAllActivePlantsFromSensor(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        relacciones_sensor_planta: List[SensorPlanta] = SensorPlantaSet.listAllActivePlantsFromSensor(session, tipo_sensor, zona_sensor, numero_sensor)
        for sensor_planta in relacciones_sensor_planta:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllActivePlantsFromSensorFromCommon(esquema: Esquema, sensor: SensorCommon) -> List[SensorPlantaCommon]:
        return SensorPlantaService.listAllActivePlantsFromSensor(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), 
                                                            sensor.getNumeroSensor())

    @staticmethod
    def listAllPlantsFromSensorBetweenDates(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[SensorPlantaCommon]:
        out: List[SensorPlantaCommon] = []
        session: Session = esquema.new_session()
        relacciones_sensor_planta: List[SensorPlanta] = SensorPlantaSet.listAllPlantsFromSensorBetweenDates(session, tipo_sensor, zona_sensor, numero_sensor, fecha_inicio, fecha_fin)
        for sensor_planta in relacciones_sensor_planta:
            out.append(SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllPlantsFromSensorFromCommonBetweenDates(esquema: Esquema, sensor: SensorCommon, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[SensorPlantaCommon]:
        return SensorPlantaService.listAllPlantsFromSensorBetweenDates(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), 
                                                                      sensor.getNumeroSensor(), fecha_inicio, fecha_fin)

    @staticmethod
    def get(esquema: Esquema, id_ : int) -> SensorPlantaCommon:
        session : Session = esquema.new_session()
        sensor_planta : SensorPlanta = SensorPlantaSet.get(session, id_)
        out= SensorPlantaCommon(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                  sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                  sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                  sensor_planta.id_)
        esquema.remove_session()
        return out
    
    @staticmethod
    def update(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, numero_sensor:int, 
                nombre_planta:str, fecha_asociacion:datetime ,fecha_anulacion:datetime, id_: int ) -> SensorPlantaCommon:
        session: Session = esquema.new_session()
        out: SensorPlantaCommon = None
        try:
            sensor_planta_modificado: SensorPlanta = SensorPlantaSet.update(session, tipo_sensor, zona_sensor, numero_sensor,
                                                                        nombre_planta, fecha_asociacion, fecha_anulacion, id_)
            out= SensorPlantaCommon(sensor_planta_modificado.tipo_sensor, sensor_planta_modificado.zona_sensor,
                                      sensor_planta_modificado.numero_sensor, sensor_planta_modificado.nombre_planta, 
                                      sensor_planta_modificado.fecha_asociacion, sensor_planta_modificado.fecha_anulacion, 
                                      sensor_planta_modificado.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out

    @staticmethod
    def updateFromCommon(esquema: Esquema, sensor_planta: SensorPlantaCommon) -> SensorPlantaCommon:
        return SensorPlantaService.update(esquema, sensor_planta.getTipoSensor(), sensor_planta.getZonaSensor(), 
                                          sensor_planta.getNumeroSensor(), sensor_planta.getNombrePlanta(),
                                          sensor_planta.getFechaAsociacion(),sensor_planta.getFechaAnulacion(),
                                          sensor_planta.getId())

    @staticmethod
    def unsubscribe(esquema: Esquema, id_ : int) -> SensorPlantaCommon:
        sensor_planta: SensorPlantaCommon = SensorPlantaService.get(esquema, id_)
        if sensor_planta.getFechaAnulacion() is None:
            sensor_planta.setFechaAnulacion(datetime.now())
            sensor_planta = SensorPlantaService.updateFromCommon(esquema, sensor_planta)
        return sensor_planta

    @staticmethod
    def unsubscribeFromCommon(esquema: Esquema, sensor_planta: SensorPlantaCommon) -> SensorPlantaCommon:
        return SensorPlantaService.unsubscribe(esquema, sensor_planta.getId())

    @staticmethod
    def unsubscribeAllFromSensor(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> List[SensorPlantaCommon]:
        lista_plantas_sensor: List[SensorPlantaCommon] = SensorPlantaService.listAllActivePlantsFromSensor(esquema, tipo_sensor, zona_sensor, numero_sensor)
        for sensor_planta in lista_plantas_sensor:
            sensor_planta.setFechaAnulacion(datetime.now())
            sensor_planta = SensorPlantaService.updateFromCommon(esquema, sensor_planta)
        return lista_plantas_sensor

    @staticmethod
    def unsubscribeAllFromSensorFromCommon(esquema: Esquema, sensor: SensorCommon) -> List[SensorPlantaCommon]:
        return SensorPlantaService.unsubscribeAllFromSensor(esquema, sensor.getTipoSensor(),sensor.getZonaSensor(),sensor.getNumeroSensor())

    @staticmethod
    def unsubscribeAllFromPlant(esquema: Esquema, nombre_planta:str) -> List[SensorPlantaCommon]:
        lista_sensores_planta: List[SensorPlantaCommon] = SensorPlantaService.listAllActiveSensorsFromPlant(esquema, nombre_planta)
        for sensor_planta in lista_sensores_planta:
            sensor_planta.setFechaAnulacion(datetime.now())
            sensor_planta = SensorPlantaService.updateFromCommon(esquema, sensor_planta)
        return lista_sensores_planta

    @staticmethod
    def unsubscribeAllFromPlantFromCommon(esquema: Esquema, planta: PlantaCommon) -> List[SensorPlantaCommon]:
        return SensorPlantaService.unsubscribeAllFromPlant(esquema, planta.getNombrePlanta())

    #TODO
    #unsibscribeFromSensorAndPlantFromCommon
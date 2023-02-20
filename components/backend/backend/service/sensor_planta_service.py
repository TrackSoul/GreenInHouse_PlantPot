from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import SensorPlanta
from backend.data.db.resultsets import SensorPlantaSet
from common.data import SensorPlanta as CommonSensorPlanta, Sensor as CommonSensor, RegistroPlanta as CommonRegistroPlanta
from common.data import TipoSensor, ZonaSensor

class SensorPlantaService():

    @staticmethod
    def create(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, 
                               numero_sensor:int, nombre_planta:str = "Sin planta", 
                               fecha_asociacion:datetime = datetime.now() ,fecha_anulacion:datetime = None) -> CommonSensorPlanta:
        session: Session = esquema.new_session()
        out: CommonSensorPlanta = None
        try:
            nuevo_sensor_planta: SensorPlanta = SensorPlantaSet.create(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, nombre_planta, 
                                                                           fecha_asociacion, fecha_anulacion)
            out= CommonSensorPlanta(nuevo_sensor_planta.tipo_sensor, nuevo_sensor_planta.zona_sensor,
                                      nuevo_sensor_planta.numero_sensor, nuevo_sensor_planta.nombre_planta, 
                                      nuevo_sensor_planta.fecha_asociacion, nuevo_sensor_planta.fecha_anulacion, 
                                      nuevo_sensor_planta.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, sensor_planta: CommonSensorPlanta) -> CommonSensorPlanta:
        return SensorPlantaService.create(esquema, sensor_planta.getTipoSensor(), sensor_planta.getZonaSensor(), 
                                          sensor_planta.getNumeroSensor(), sensor_planta.getNombrePlanta())
    
    @staticmethod
    def createRelationFromCommon(esquema: Esquema, sensor: CommonSensor, planta: CommonRegistroPlanta) -> CommonSensorPlanta:
        return SensorPlantaService.create(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), 
                                                        sensor.getNumeroSensor(), planta.getNombrePlanta())

    @staticmethod
    def exists(esquema: Esquema, id_:int) -> bool:
        session: Session = esquema.new_session()
        sensor_planta_existe: bool = SensorPlantaSet.get(session, id_)
        esquema.remove_session()
        return sensor_planta_existe
    
    @staticmethod
    def listAll(esquema: Esquema) -> List[CommonSensorPlanta]:
        out: List[CommonSensorPlanta] = []
        session: Session = esquema.new_session()
        registros_sensor: List[SensorPlanta] = SensorPlantaSet.listAll(session)
        for sensor_planta in registros_sensor:
            out.append(CommonSensorPlanta(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllSensorsPlant(esquema: Esquema, nombre_planta: str) -> List[CommonSensorPlanta]:
        out: List[CommonSensorPlanta] = []
        session: Session = esquema.new_session()
        registros_sensor: List[SensorPlanta] = SensorPlantaSet.listAllSensorsPlant(session, nombre_planta)
        for sensor_planta in registros_sensor:
            out.append(CommonSensorPlanta(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, id_ : int) -> CommonSensorPlanta:
        session : Session = esquema.new_session()
        sensor_planta : SensorPlanta = SensorPlantaSet.get(session, id_)
        out= CommonSensorPlanta(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                  sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                  sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                  sensor_planta.id_)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, id_: int, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, numero_sensor:int, 
                nombre_planta:str, fecha_asociacion:datetime ,fecha_anulacion:datetime ) -> CommonSensorPlanta:
        session: Session = esquema.new_session()
        out: CommonSensorPlanta = None
        try:
            sensor_planta_modificado: SensorPlanta = SensorPlantaSet.update(session, tipo_sensor, zona_sensor, numero_sensor,
                                                                        nombre_planta, fecha_asociacion, fecha_anulacion, id_)
            out= CommonSensorPlanta(sensor_planta_modificado.tipo_sensor, sensor_planta_modificado.zona_sensor,
                                      sensor_planta_modificado.numero_sensor, sensor_planta_modificado.nombre_planta, 
                                      sensor_planta_modificado.fecha_asociacion, sensor_planta_modificado.fecha_anulacion, 
                                      sensor_planta_modificado.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out

    @staticmethod
    def updateFromCommon(esquema: Esquema, sensor_planta: CommonSensorPlanta) -> CommonSensorPlanta:
        return SensorPlantaService.create(esquema, sensor_planta.getTipoSensor(), sensor_planta.getZonaSensor(), 
                                          sensor_planta.getNumeroSensor(), sensor_planta.getNombrePlanta(),
                                          sensor_planta.getFechaAsociacion(),sensor_planta.getFechaAnulacion(),
                                          sensor_planta.getId())


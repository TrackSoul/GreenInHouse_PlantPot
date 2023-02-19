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
    # def create_sensor_planta(tipo_sensor: Union[TipoSensor,str], zona_sensor:Union[ZonaSensor,str] ,numero_sensor:int, valor:float, schema: Esquema) -> CommonSensorPlanta:
    def create_sensor_planta(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, 
                               numero_sensor:int, nombre_planta:str = "Sin planta", 
                               fecha_asociacion:datetime = datetime.now() ,fecha_anulacion:datetime = None) -> CommonSensorPlanta:
        session: Session = esquema.new_session()
        out: CommonSensorPlanta = None
        try:
            # if isinstance(tipo_sensor, str):
            #     tipo_sensor = TipoSensor[tipo_sensor]
            # if isinstance(zona_sensor, str):
            #     zona_sensor = ZonaSensor[zona_sensor]
            new_sensor_planta: SensorPlanta = SensorPlantaSet.create(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, nombre_planta, 
                                                                           fecha_asociacion, fecha_anulacion)
            out= CommonSensorPlanta(new_sensor_planta.tipo_sensor, new_sensor_planta.zona_sensor,
                                      new_sensor_planta.numero_sensor, new_sensor_planta.nombre_planta, 
                                      new_sensor_planta.fecha_asociacion, new_sensor_planta.fecha_anulacion, 
                                      new_sensor_planta.id)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def create_sensor_planta_from_common(esquema: Esquema, sensor_planta: CommonSensorPlanta) -> CommonSensorPlanta:
        return SensorPlantaService.create_sensor_planta(esquema, sensor_planta.getTipoSensor(), sensor_planta.getZonaSensor(), 
                                                        sensor_planta.getNumeroSensor(), sensor_planta.getNombrePlanta())
    
    @staticmethod
    def create_sensor_planta_relation_from_common(esquema: Esquema, sensor: CommonSensor, planta: CommonRegistroPlanta) -> CommonSensorPlanta:
        return SensorPlantaService.create_sensor_planta(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), 
                                                        sensor.getNumeroSensor(), planta.getNombrePlanta())

    @staticmethod
    def exists_sensor_planta(esquema: Esquema, id:int):
        session: Session = esquema.new_session()
        sensor_planta_exists: bool = SensorPlantaSet.get(session, id)
        esquema.remove_session()
        return sensor_planta_exists

    @staticmethod
    def list_sensor_planta(esquema: Esquema) -> List[CommonSensorPlanta]:
        out: List[CommonSensorPlanta] = []
        session: Session = esquema.new_session()
        registros_sensor: List[SensorPlanta] = SensorPlantaSet.list_all(session)
        for sensor_planta in registros_sensor:
            out.append(CommonSensorPlanta(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                      sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                      sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                      sensor_planta.id))
        esquema.remove_session()
        return out

    @staticmethod
    def get_sensor_planta(esquema: Esquema, id : int) -> CommonSensorPlanta:
        session : Session = esquema.new_session()
        sensor_planta : SensorPlanta = SensorPlantaSet.get(session, id)
        out= CommonSensorPlanta(sensor_planta.tipo_sensor, sensor_planta.zona_sensor,
                                  sensor_planta.numero_sensor, sensor_planta.nombre_planta, 
                                  sensor_planta.fecha_asociacion, sensor_planta.fecha_anulacion,
                                  sensor_planta.id)
        esquema.remove_session()
        return out

'''
    @staticmethod
    def update_pregunta(id:int,schema: Schema):
        session: Session = schema.new_session()
        Preguntas.update(session,id)
        schema.remove_session()
'''

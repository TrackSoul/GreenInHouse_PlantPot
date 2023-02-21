from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import Sensor
from backend.data.db.resultsets import SensorSet
from common.data.util import Sensor as CommonSensor
from common.data.util import TipoSensor, ZonaSensor

class SensorService():
    
    @staticmethod
    def create(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                               modelo_sensor:str, direccion_lectura:str=None, patilla_1_lectura:int=None, patilla_2_lectura:int=None, 
                               patilla_3_lectura:int=None, patilla_4_lectura:int=None, 
                               fecha_creacion: datetime = datetime.now() ,fecha_eliminacion: datetime = None) -> CommonSensor:
        session: Session = esquema.new_session()
        out: CommonSensor = None
        try:
            nuevo_sensor: Sensor = SensorSet.create(session, tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                                  direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                                  patilla_3_lectura, patilla_4_lectura, 
                                                  fecha_creacion, fecha_eliminacion)
            out= CommonSensor(nuevo_sensor.tipo_sensor,nuevo_sensor.zona_sensor,nuevo_sensor.numero_sensor,nuevo_sensor.modelo_sensor, 
                              nuevo_sensor.direccion_lectura, nuevo_sensor.patilla_1_lectura, nuevo_sensor.patilla_2_lectura,
                              nuevo_sensor.patilla_3_lectura, nuevo_sensor.patilla_4_lectura, 
                              nuevo_sensor.fecha_creacion, nuevo_sensor.fecha_eliminacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, sensor: CommonSensor) -> CommonSensor:
        return SensorService.create(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(),sensor.getNumeroSensor(), 
                                           sensor.getModeloSensor(), sensor.getDireccionLectura(), sensor.getPatilla1Lectura(), 
                                           sensor.getPatilla2Lectura(), sensor.getPatilla3Lectura(), sensor.getPatilla4Lectura(),
                                           #sensor.getFechaCreacion(), sensor.getFechaEliminacion()
                                           )

    @staticmethod
    def exists(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> bool:
        session: Session = esquema.new_session()
        sensor_existe: bool = SensorSet.get(session, tipo_sensor, zona_sensor, numero_sensor)
        esquema.remove_session()
        return sensor_existe

    @staticmethod
    def listAll(esquema: Esquema) -> List[CommonSensor]:
        out: List[CommonSensor] = []
        session: Session = esquema.new_session()
        registros_sensor: List[Sensor] = SensorSet.listAll(session)
        for sensor in registros_sensor:
            out.append(CommonSensor(sensor.tipo_sensor,sensor.zona_sensor,sensor.numero_sensor,sensor.modelo_sensor, 
                              sensor.direccion_lectura, sensor.patilla_1_lectura, sensor.patilla_2_lectura,
                              sensor.patilla_3_lectura, sensor.patilla_4_lectura,
                              sensor.fecha_creacion, sensor.fecha_eliminacion))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> CommonSensor:
        session : Session = esquema.new_session()
        sensor : Sensor = SensorSet.get(session, tipo_sensor, zona_sensor, numero_sensor)
        out= CommonSensor(sensor.tipo_sensor,sensor.zona_sensor,sensor.numero_sensor,sensor.modelo_sensor, 
                          sensor.direccion_lectura, sensor.patilla_1_lectura, sensor.patilla_2_lectura,
                          sensor.patilla_3_lectura, sensor.patilla_4_lectura,
                          sensor.fecha_creacion, sensor.fecha_eliminacion)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                modelo_sensor:str, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int, 
                patilla_3_lectura:int, patilla_4_lectura:int, fecha_creacion: datetime ,fecha_eliminacion: datetime) -> CommonSensor:
        session: Session = esquema.new_session()
        out: CommonSensor = None
        try:
            sensor_modificado: Sensor = SensorSet.update(session, tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                                    direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                                    patilla_3_lectura, patilla_4_lectura, 
                                                    fecha_creacion, fecha_eliminacion)
            out= CommonSensor(sensor_modificado.tipo_sensor,sensor_modificado.zona_sensor,sensor_modificado.numero_sensor,
                              sensor_modificado.modelo_sensor, sensor_modificado.direccion_lectura, sensor_modificado.patilla_1_lectura, 
                              sensor_modificado.patilla_2_lectura, sensor_modificado.patilla_3_lectura, sensor_modificado.patilla_4_lectura, 
                              sensor_modificado.fecha_creacion, sensor_modificado.fecha_eliminacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, sensor: CommonSensor) -> CommonSensor:
        return SensorService.update(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(),sensor.getNumeroSensor(), 
                                    sensor.getModeloSensor(), sensor.getDireccionLectura(), sensor.getPatilla1Lectura(), 
                                    sensor.getPatilla2Lectura(), sensor.getPatilla3Lectura(), sensor.getPatilla4Lectura(),
                                    sensor.getFechaCreacion(), sensor.getFechaEliminacion())


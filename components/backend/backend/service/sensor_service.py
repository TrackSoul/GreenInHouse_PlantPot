from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import Sensor
from backend.data.db.resultsets import SensorSet
from backend.data.util import Sensor as SensorBackend
from common.data.util import Sensor as SensorCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor

class SensorService():
    
    @staticmethod
    def create(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                               modelo_sensor:ModeloSensor, direccion_lectura:str=None, patilla_1_lectura:int=None, patilla_2_lectura:int=None, 
                               patilla_3_lectura:int=None, patilla_4_lectura:int=None, unidad_medida_1:str = None,
                               unidad_medida_2:str = None, unidad_medida_3:str = None, unidad_medida_4:str = None,
                               fecha_creacion: datetime = datetime.now() ,fecha_eliminacion: datetime = None) -> SensorBackend:
        session: Session = esquema.new_session()
        out: SensorBackend = None
        try:
            nuevo_sensor: Sensor = SensorSet.create(session, tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                                  direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                                  patilla_3_lectura, patilla_4_lectura, unidad_medida_1, unidad_medida_2, 
                                                  unidad_medida_3, unidad_medida_4, fecha_creacion, fecha_eliminacion)
            out= SensorBackend(nuevo_sensor.tipo_sensor,nuevo_sensor.zona_sensor,nuevo_sensor.numero_sensor,nuevo_sensor.modelo_sensor, 
                              nuevo_sensor.direccion_lectura, nuevo_sensor.patilla_1_lectura, nuevo_sensor.patilla_2_lectura,
                              nuevo_sensor.patilla_3_lectura, nuevo_sensor.patilla_4_lectura, nuevo_sensor.unidad_medida_1,
                              nuevo_sensor.unidad_medida_2, nuevo_sensor.unidad_medida_3, nuevo_sensor.unidad_medida_4,
                              nuevo_sensor.fecha_creacion, nuevo_sensor.fecha_eliminacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, sensor: SensorCommon) -> SensorBackend:
        return SensorService.create(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(),sensor.getNumeroSensor(), 
                                           sensor.getModeloSensor(), sensor.getDireccionLectura(), sensor.getPatilla1Lectura(), 
                                           sensor.getPatilla2Lectura(), sensor.getPatilla3Lectura(), sensor.getPatilla4Lectura(), 
                                           sensor.getUnidadMedida1(), sensor.getUnidadMedida2(), 
                                           sensor.getUnidadMedida3(), sensor.getUnidadMedida4(),
                                           #sensor.getFechaCreacion(), sensor.getFechaEliminacion()
                                           )

    @staticmethod
    def exists(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> bool:
        session: Session = esquema.new_session()
        sensor_existe: bool = SensorSet.get(session, tipo_sensor, zona_sensor, numero_sensor)
        esquema.remove_session()
        return sensor_existe

    @staticmethod
    def listAll(esquema: Esquema) -> List[SensorBackend]:
        out: List[SensorBackend] = []
        session: Session = esquema.new_session()
        registros_sensor: List[Sensor] = SensorSet.listAll(session)
        for sensor in registros_sensor:
            out.append(SensorBackend(sensor.tipo_sensor,sensor.zona_sensor,sensor.numero_sensor,sensor.modelo_sensor, 
                              sensor.direccion_lectura, sensor.patilla_1_lectura, sensor.patilla_2_lectura,
                              sensor.patilla_3_lectura, sensor.patilla_4_lectura, sensor.unidad_medida_1,
                              sensor.unidad_medida_2, sensor.unidad_medida_3, sensor.unidad_medida_4,
                              sensor.fecha_creacion, sensor.fecha_eliminacion))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> SensorBackend:
        session : Session = esquema.new_session()
        sensor : Sensor = SensorSet.get(session, tipo_sensor, zona_sensor, numero_sensor)
        out= SensorBackend(sensor.tipo_sensor,sensor.zona_sensor,sensor.numero_sensor,sensor.modelo_sensor, 
                          sensor.direccion_lectura, sensor.patilla_1_lectura, sensor.patilla_2_lectura,
                          sensor.patilla_3_lectura, sensor.patilla_4_lectura, sensor.unidad_medida_1,
                          sensor.unidad_medida_2, sensor.unidad_medida_3, sensor.unidad_medida_4,
                          sensor.fecha_creacion, sensor.fecha_eliminacion)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                modelo_sensor:ModeloSensor, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int, 
                patilla_3_lectura:int, patilla_4_lectura:int, unidad_medida_1:str, unidad_medida_2:str,
                 unidad_medida_3:str, unidad_medida_4:str, fecha_creacion: datetime ,fecha_eliminacion: datetime) -> SensorBackend:
        session: Session = esquema.new_session()
        out: SensorBackend = None
        try:
            sensor_modificado: Sensor = SensorSet.update(session, tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                                    direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                                    patilla_3_lectura, patilla_4_lectura, unidad_medida_1, 
                                                    unidad_medida_2, unidad_medida_3, unidad_medida_4,
                                                    fecha_creacion, fecha_eliminacion)
            out= SensorBackend(sensor_modificado.tipo_sensor,sensor_modificado.zona_sensor,sensor_modificado.numero_sensor,
                              sensor_modificado.modelo_sensor, sensor_modificado.direccion_lectura, sensor_modificado.patilla_1_lectura, 
                              sensor_modificado.patilla_2_lectura, sensor_modificado.patilla_3_lectura, sensor_modificado.patilla_4_lectura, 
                              sensor_modificado.unidad_medida_1, sensor_modificado.unidad_medida_2, sensor_modificado.unidad_medida_3, 
                              sensor_modificado.unidad_medida_4, sensor_modificado.fecha_creacion, sensor_modificado.fecha_eliminacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, sensor: SensorCommon) -> SensorBackend:
        return SensorService.update(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(),sensor.getNumeroSensor(), 
                                    sensor.getModeloSensor(), sensor.getDireccionLectura(), sensor.getPatilla1Lectura(), 
                                    sensor.getPatilla2Lectura(), sensor.getPatilla3Lectura(), sensor.getPatilla4Lectura(),
                                    sensor.getUnidadMedida1(), sensor.getUnidadMedida2(), sensor.getUnidadMedida3(), 
                                    sensor.getUnidadMedida4(), sensor.getFechaCreacion(), sensor.getFechaEliminacion())


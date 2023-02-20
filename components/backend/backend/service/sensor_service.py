from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import Sensor
from backend.data.db.resultsets import SensorSet
from common.data import Sensor as CommonSensor
from common.data import TipoSensor, ZonaSensor

class SensorService():

    @staticmethod
    # def create_sensor(tipo_sensor: Union[TipoSensor,str], zona_sensor:Union[ZonaSensor,str] ,numero_sensor:int, valor:float, schema: Esquema) -> CommonSensor:
    def create(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                               modelo_sensor:str, direccion_lectura:str=None, patilla_1_lectura:int=None, patilla_2_lectura:int=None, 
                               patilla_3_lectura:int=None, patilla_4_lectura:int=None, 
                               fecha_creacion: datetime = datetime.now() ,fecha_eliminacion: datetime = None) -> CommonSensor:
        session: Session = esquema.new_session()
        out: CommonSensor = None
        try:
            # if isinstance(tipo_sensor, str):
            #     tipo_sensor = TipoSensor[tipo_sensor]
            # if isinstance(zona_sensor, str):
            #     zona_sensor = ZonaSensor[zona_sensor]
            new_sensor: Sensor = SensorSet.create(session, tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                                  direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                                  patilla_3_lectura, patilla_4_lectura, 
                                                  fecha_creacion, fecha_eliminacion)
            out= CommonSensor(new_sensor.tipo_sensor,new_sensor.zona_sensor,new_sensor.numero_sensor,new_sensor.modelo_sensor, 
                              new_sensor.direccion_lectura, new_sensor.patilla_1_lectura, new_sensor.patilla_2_lectura,
                              new_sensor.patilla_3_lectura, new_sensor.patilla_4_lectura, 
                              new_sensor.fecha_creacion, new_sensor.fecha_eliminacion)
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
        sensor_exists: bool = SensorSet.get(session, tipo_sensor, zona_sensor, numero_sensor)
        esquema.remove_session()
        return sensor_exists

    @staticmethod
    def list_all(esquema: Esquema) -> List[CommonSensor]:
        out: List[CommonSensor] = []
        session: Session = esquema.new_session()
        registros_sensor: List[Sensor] = SensorSet.list_all(session)
        for sensor in registros_sensor:
            out.append(CommonSensor(sensor.tipo_sensor,sensor.zona_sensor,sensor.numero_sensor,sensor.modelo_sensor, 
                              sensor.direccion_lectura, sensor.patilla_1_lectura, sensor.id, sensor.patilla_2_lectura,
                              sensor.patilla_3_lectura, sensor.id, sensor.patilla_4_lectura,
                              sensor.fecha_creacion, sensor.fecha_eliminacion))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> CommonSensor:
        session : Session = esquema.new_session()
        sensor : Sensor = SensorSet.get(session, tipo_sensor, zona_sensor, numero_sensor)
        out= CommonSensor(sensor.tipo_sensor,sensor.zona_sensor,sensor.numero_sensor,sensor.modelo_sensor, 
                          sensor.direccion_lectura, sensor.patilla_1_lectura, sensor.id, sensor.patilla_2_lectura,
                          sensor.patilla_3_lectura, sensor.id, sensor.patilla_4_lectura,
                          sensor.fecha_creacion, sensor.fecha_eliminacion)
        esquema.remove_session()
        return out

'''
    @staticmethod
    def update_pregunta(id:int,schema: Schema):
        session: Session = schema.new_session()
        Preguntas.update(session,id)
        schema.remove_session()
'''

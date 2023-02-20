from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroSensor
from backend.data.db.resultsets import RegistroSensorSet
from common.data import RegistroSensor as CommonRegistroSensor
from common.data import TipoSensor, ZonaSensor

class RegistroSensorService():

    @staticmethod
    # def create_registro_sensor(tipo_sensor: Union[TipoSensor,str], zona_sensor:Union[ZonaSensor,str] ,numero_sensor:int, valor:float, schema: Esquema) -> CommonRegistroSensor:
    def create(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, 
                               numero_sensor:int, valor:float, escala:str, fecha:datetime = datetime.now()) -> CommonRegistroSensor:
        session: Session = esquema.new_session()
        out: CommonRegistroSensor = None
        try:
            # if isinstance(tipo_sensor, str):
            #     tipo_sensor = TipoSensor[tipo_sensor]
            # if isinstance(zona_sensor, str):
            #     zona_sensor = ZonaSensor[zona_sensor]
            new_registro_sensor: RegistroSensor = RegistroSensorSet.create(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, valor, escala, fecha)
            out= CommonRegistroSensor(new_registro_sensor.tipo_sensor,new_registro_sensor.zona_sensor,
                                      new_registro_sensor.numero_sensor,new_registro_sensor.valor, 
                                      new_registro_sensor.escala, new_registro_sensor.fecha, 
                                      new_registro_sensor.id)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, registro_sensor: CommonRegistroSensor) -> CommonRegistroSensor:
        return RegistroSensorService.create(esquema, registro_sensor.getTipoSensor(), registro_sensor.getZonaSensor(), 
                                                            registro_sensor.getNumeroSensor(), registro_sensor.getValor(), 
                                                            registro_sensor.getEscala())

    @staticmethod
    def exists(esquema: Esquema, id:int) -> bool:
        session: Session = esquema.new_session()
        registro_sensor_exists: bool = RegistroSensorSet.get(session, id)
        esquema.remove_session()
        return registro_sensor_exists

    @staticmethod
    def listAll(esquema: Esquema) -> List[CommonRegistroSensor]:
        out: List[CommonRegistroSensor] = []
        session: Session = esquema.new_session()
        registros_sensor: List[RegistroSensor] = RegistroSensorSet.listAll(session)
        for registro_sensor in registros_sensor:
            out.append(CommonRegistroSensor(registro_sensor.tipo_sensor,registro_sensor.zona_sensor,
                                      registro_sensor.numero_sensor,registro_sensor.valor, 
                                      registro_sensor.escala, registro_sensor.fecha, 
                                      registro_sensor.id))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, id : int) -> CommonRegistroSensor:
        session : Session = esquema.new_session()
        registro_sensor : RegistroSensor = RegistroSensorSet.get(session, id)
        out= CommonRegistroSensor(registro_sensor.tipo_sensor,registro_sensor.zona_sensor, registro_sensor.numero_sensor,
                                  registro_sensor.valor, registro_sensor.escala, 
                                  registro_sensor.fecha, registro_sensor.id)
        esquema.remove_session()
        return out

'''
    @staticmethod
    def update_pregunta(id:int,schema: Schema):
        session: Session = schema.new_session()
        Preguntas.update(session,id)
        schema.remove_session()
'''

from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroSensor
from backend.data.db.resultsets import RegistroSensorSet
from common.data.util import RegistroSensor as CommonRegistroSensor
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida

class RegistroSensorService():

    @staticmethod
    def create(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, 
                        numero_sensor:int, valor:float, unidad_medida: UnidadMedida, fecha:datetime = datetime.now()) -> CommonRegistroSensor:
        session: Session = esquema.new_session()
        out: CommonRegistroSensor = None
        try:
            new_registro_sensor: RegistroSensor = RegistroSensorSet.create(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, valor, unidad_medida, fecha)
            out= CommonRegistroSensor(new_registro_sensor.tipo_sensor,new_registro_sensor.zona_sensor,
                                      new_registro_sensor.numero_sensor,new_registro_sensor.valor, 
                                      new_registro_sensor.unidad_medida, new_registro_sensor.fecha, 
                                      new_registro_sensor.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, registro_sensor: CommonRegistroSensor) -> CommonRegistroSensor:
        return RegistroSensorService.create(esquema, registro_sensor.getTipoSensor(), registro_sensor.getZonaSensor(), 
                                            registro_sensor.getNumeroSensor(), registro_sensor.getValor(), 
                                            registro_sensor.getUnidadMedida())

    @staticmethod
    def exists(esquema: Esquema, id_:int) -> bool:
        session: Session = esquema.new_session()
        registro_sensor_exists: bool = RegistroSensorSet.get(session, id_)
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
                                      registro_sensor.unidad_medida, registro_sensor.fecha, 
                                      registro_sensor.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllToJson(esquema: Esquema) -> List[Dict]:
        out: List[Dict] = []
        session: Session = esquema.new_session()
        registros_sensor: List[RegistroSensor] = RegistroSensorSet.listAll(session)
        
        for registro_sensor in registros_sensor:
            out.append(registros_sensor.toJson())
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, id_ : int) -> CommonRegistroSensor:
        session : Session = esquema.new_session()
        registro_sensor : RegistroSensor = RegistroSensorSet.get(session, id_)
        out= CommonRegistroSensor(registro_sensor.tipo_sensor,registro_sensor.zona_sensor, registro_sensor.numero_sensor,
                                  registro_sensor.valor, registro_sensor.unidad_medida, 
                                  registro_sensor.fecha, registro_sensor.id_)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, numero_sensor:int, valor:float, 
               unidad_medida: UnidadMedida, fecha: datetime, id_: int) -> CommonRegistroSensor:
        session: Session = esquema.new_session()
        out: CommonRegistroSensor = None
        try:
            registro_sensor_modificado: RegistroSensor = RegistroSensorSet.update(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, valor, unidad_medida, fecha,id_)
            out= CommonRegistroSensor(registro_sensor_modificado.tipo_sensor,registro_sensor_modificado.zona_sensor,
                                      registro_sensor_modificado.numero_sensor,registro_sensor_modificado.valor, 
                                      registro_sensor_modificado.unidad_medida, registro_sensor_modificado.fecha, 
                                      registro_sensor_modificado.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, registro_sensor: CommonRegistroSensor) -> CommonRegistroSensor:
        return RegistroSensorService.update(esquema, registro_sensor.getTipoSensor(), registro_sensor.getZonaSensor(), 
                                            registro_sensor.getNumeroSensor(), registro_sensor.getValor(), 
                                            registro_sensor.getUnidadMedida(), registro_sensor.getId())

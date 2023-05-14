import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroSensor
from backend.data.db.resultsets import RegistroSensorSet
from backend.service import RegistroSensorService, SensorService, GeneralService
from common.data.util import RegistroSensor as RegistroSensorCommon, Sensor as SensorCommon
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida


def getRegistroSensor(id: int) :
    with current_app.app_context() :
        if RegistroSensorService.exists(current_app.db,id):
            return RegistroSensorService.get(current_app.db, id).toJson(), HTTPStatus.OK.value
        else:
            return ("El registro no existe", HTTPStatus.NOT_FOUND.value)
        
def getAllRegistrosSensores() :
    with current_app.app_context() :
        return [item.toJson() for item in RegistroSensorService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllFromSensor(tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int):
    with current_app.app_context() :
        if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in RegistroSensorService.listAllFromSensor(current_app.db,tipo_sensor,zona_sensor,numero_sensor)], HTTPStatus.OK.value
        else:
            return ("El sensor no existe", HTTPStatus.NOT_FOUND.value)

def getAllFromSensorFromCommon(esquema: Esquema, sensor_dic: dict):
    sensor=SensorCommon().fromJson(sensor_dic)
    return getAllFromSensor(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor())


def getAllFromSensorBetweenDates(tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, fecha_inicio: str, fecha_fin: str = str(datetime.now())):
    with current_app.app_context() :
        try:
            fecha_inicio_dt=datetime.fromisoformat(fecha_inicio)
            fecha_fin_dt=datetime.fromisoformat(fecha_fin)
            if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
                return [item.toJson() for item in RegistroSensorService.listAllFromSensorBetweenDates(current_app.db,tipo_sensor,zona_sensor,numero_sensor,
                                                                                                      fecha_inicio_dt,fecha_fin_dt)], HTTPStatus.OK.value
            else:
                return ("El sensor no existe", HTTPStatus.NOT_FOUND.value)
        except(ValueError):
            return ("Error en las fechas especificadas", HTTPStatus.NOT_ACCEPTABLE.value)
    
def getAllFromSensorFromCommonBetweenDates(esquema: Esquema, sensor_dic: dict,  fecha_inicio: str, fecha_fin: str = str(datetime.now())):
    try:
        sensor=SensorCommon().fromJson(sensor_dic)
        return getAllFromSensorBetweenDates(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor(), 
                                                fecha_inicio, fecha_fin)
    except:
        return ("Los datos del sensor no son correctos", HTTPStatus.NOT_ACCEPTABLE.value)

# def post_comentario_respuesta(body: dict, aid: int):
#     with current_app.app_context() :
#         try:
#             comentario = Comentario.from_json(body,True)
#             return ComentarioService.create_comentario_from_common(comentario, aid, current_app.db).to_json(), HTTPStatus.CREATED.value
#         except Exception as e:
#             current_app.logger.error(traceback.format_exception(e))
#             return (str(e), HTTPStatus.NOT_FOUND.value)
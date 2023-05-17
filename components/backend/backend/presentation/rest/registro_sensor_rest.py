import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import RegistroSensorService, SensorService, PlantaService
from common.data.util import RegistroSensor as RegistroSensorCommon, Sensor as SensorCommon, Planta as PlantaCommon
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida


def get(rsid: int) :
    with current_app.app_context() :
        if RegistroSensorService.exists(current_app.db,rsid):
            return RegistroSensorService.get(current_app.db, rsid).toJson(), HTTPStatus.OK.value
        else:
            return ("El registro de sensor " + str(rsid) + "no existe", HTTPStatus.NOT_FOUND.value)
        
def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in RegistroSensorService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllFromSensor(st:str, sz: str ,sid:int):
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor especificado no es correcto.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor especificada no es correcta.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    with current_app.app_context() :
        if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in RegistroSensorService.listAllFromSensor(current_app.db,tipo_sensor,zona_sensor,numero_sensor)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)

# def getAllFromSensorFromCommon(sensor_dic: dict):
#     try:
#         sensor=SensorCommon().fromJson(sensor_dic)
#         return getAllFromSensor(sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor())
#     except:
#         return ("Los datos del sensor no son correctos", HTTPStatus.NOT_ACCEPTABLE.value)

def getAllFromSensorBetweenDates(st:str, sz: str ,sid:int, fi: str, ff: str = str(datetime.now())):
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor especificado no es correcto.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor especificada no es correcta.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    try:
        fecha_inicio=datetime.fromisoformat(fi)
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de las fechas especificadas.", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio no puede ser mayor que la fecha de fin.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in RegistroSensorService.listAllFromSensorBetweenDates(current_app.db,tipo_sensor,zona_sensor,numero_sensor,
                                                                                                    fecha_inicio,fecha_fin)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)
    
# def getAllFromSensorFromCommonBetweenDates(esquema: Esquema, sensor_dic: dict,  fecha_inicio: str, fecha_fin: str = str(datetime.now())):
#     try:
#         sensor=SensorCommon().fromJson(sensor_dic)
#         return getAllFromSensorBetweenDates(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor(), 
#                                                 fecha_inicio, fecha_fin)
#     except:
#         return ("Los datos del sensor no son correctos", HTTPStatus.NOT_ACCEPTABLE.value)

def getAllFromPlant(np:str):
    nombre_planta: str = np
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            return [item.toJson() for item in RegistroSensorService.listAllFromPlant(current_app.db, nombre_planta)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)

def getAllFromPlantBetweenDates(np:str, fi: str, ff: str = str(datetime.now())):
    nombre_planta: str = np
    try:
        fecha_inicio=datetime.fromisoformat(fi)
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de las fechas especificadas.", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio no puede ser mayor que la fecha de fin.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            return [item.toJson() for item in RegistroSensorService.listAllFromPlantBetweenDates(current_app.db, nombre_planta, fecha_inicio, fecha_fin)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)  
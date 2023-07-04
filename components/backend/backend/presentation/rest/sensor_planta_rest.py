import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import SensorService, PlantaService, SensorPlantaService
from common.data.util import Sensor as SensorCommon, Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.db.exc import ErrorSensorPlantaExiste, ErrorSensorPlantaNoExiste

def get(spid:int) :
    id_sensor_planta:int = spid
    with current_app.app_context() :
        if SensorPlantaService.exists(current_app.db,id_sensor_planta):
            return SensorPlantaService.get(current_app.db, id_sensor_planta).toJson(), HTTPStatus.OK.value
        else:
            return ("La asociación sensor-planta " + str(spid) + " no existe", HTTPStatus.NOT_FOUND.value)
        
def getActiveFromSensorAndPlant(st:str, sz: str ,sid:int, np:str) :
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            if SensorPlantaService.existsActiveFromSensorAndPlant(current_app.db,current_app.db, tipo_sensor,zona_sensor,numero_sensor,nombre_planta):
                return SensorPlantaService.getActiveFromSensorAndPlant(current_app.db, current_app.db, tipo_sensor,zona_sensor,numero_sensor,nombre_planta).toJson(), HTTPStatus.OK.value
            else:
                return ("La asociación entre el sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " y la planta " + str(nombre_planta) + " no existe", HTTPStatus.NOT_FOUND.value)
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value) 

def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in SensorPlantaService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllActive() :
    with current_app.app_context() :
        return [item.toJson() for item in SensorPlantaService.listAllActive(current_app.db)], HTTPStatus.OK.value


def getAllSensorsFromPlant(np:str) -> List[Dict]:
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            return [item.toJson() for item in SensorPlantaService.listAllSensorsFromPlant(current_app.db, nombre_planta)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)
        
def getAllActiveSensorsFromPlant(np:str) -> List[Dict]:
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            return [item.toJson() for item in SensorPlantaService.listAllSensorsFromPlant(current_app.db, nombre_planta)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)

def getAllSensorsFromPlantBetweenDates(np:str, fi: str, ff: str = str(datetime.now())) -> List[Dict]:
    try:
        fecha_inicio=datetime.fromisoformat(fi)
    except(ValueError):
        return ("Error en el formato de la fecha de inicio " + str(fi) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio " + str(fi) + " no puede ser mayor que la fecha de fin " + str(ff) + " .", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            return [item.toJson() for item in SensorPlantaService.listAllSensorsFromPlantBetweenDates(current_app.db, nombre_planta, fecha_inicio, fecha_fin)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)   

def getAllPlantsFromSensor(st:str, sz: str ,sid:int) -> List[Dict]:
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    with current_app.app_context() :
        if SensorPlantaService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in SensorPlantaService.listAllPlantsFromSensor(current_app.db,tipo_sensor,zona_sensor,numero_sensor)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)

def getAllActivePlantsFromSensor(st:str, sz: str ,sid:int) -> List[Dict]:
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    with current_app.app_context() :
        if SensorPlantaService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in SensorPlantaService.listAllActivePlantsFromSensor(current_app.db,tipo_sensor,zona_sensor,numero_sensor)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)

def getAllPlantsFromSensorBetweenDates(st:str, sz: str ,sid:int, fi: str, ff: str = str(datetime.now())) -> List[Dict]:
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    try:
        fecha_inicio=datetime.fromisoformat(fi)
    except(ValueError):
        return ("Error en el formato de la fecha de inicio " + str(fi) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio " + str(fi) + " no puede ser mayor que la fecha de fin " + str(ff) + " .", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in SensorPlantaService.listAllPlantsFromSensorBetweenDates(current_app.db,tipo_sensor,zona_sensor,numero_sensor,
                                                                                                    fecha_inicio,fecha_fin)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)

def post(body:dict):
    with current_app.app_context() :
        try:
            sensor_planta = SensorPlantaCommon.fromJson(body)
            return SensorPlantaService.createFromCommon(current_app.db,sensor_planta).toJson(), HTTPStatus.CREATED.value
        except ErrorSensorPlantaExiste:
            return ("Ya existe una asociacion activa entre el sensor " + str(body.get("numero_sensor")) + " de tipo " + str(body.get("tipo_sensor")) + " de la zona " + str(body.get("zona_sensor")) + " y la planta " + str(body.get("nombre_planta")), HTTPStatus.CONFLICT.value)
        
def update(body:dict):
    with current_app.app_context() :
        try:
            sensor = SensorCommon.fromJson(body)
            return SensorPlantaService.updateFromCommon(current_app.db,sensor).toJson(), HTTPStatus.OK.value
        except ErrorSensorPlantaNoExiste:
            return ("La asociación entre el sensor " + str(body.get("numero_sensor")) + " de tipo " + str(body.get("tipo_sensor")) + " de la zona " + str(body.get("zona_sensor")) + " y la planta " + str(body.get("nombre_planta") + " no existe"), HTTPStatus.NOT_FOUND.value)

def unsubscribe(st:str, sz: str ,sid:int, np:str) :
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            if SensorPlantaService.existsActiveFromSensorAndPlant(current_app.db, tipo_sensor,zona_sensor,numero_sensor,nombre_planta):
                return SensorPlantaService.unsubscribeFromSensorAndPlant(current_app.db, tipo_sensor,zona_sensor,numero_sensor,nombre_planta).toJson(), HTTPStatus.OK.value
            else:
                return ("La asociación entre el sensor " + str(sid) + " de tipo " + str(st) + " de la zona " + str(sz) + " y la planta " + str(np) + " no existe", HTTPStatus.NOT_FOUND.value)
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value) 

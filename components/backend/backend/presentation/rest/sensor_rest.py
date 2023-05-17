import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import SensorService, PlantaService, SensorPlantaService
from common.data.util import Sensor as SensorCommon, Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida


def get(st:str, sz: str ,sid:int) :
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
            return SensorService.get(current_app.db, tipo_sensor,zona_sensor,numero_sensor).toJson(), HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)
        
def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllActive() :
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllActive(current_app.db)], HTTPStatus.OK.value

def getAllFromType(st:str):
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("Los datos del tipo de sensor " + str(st) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllFromType(current_app.db,tipo_sensor)], HTTPStatus.OK.value
 
def getAllActiveFromType(st:str):
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("Los datos del tipo de sensor " + str(st) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllActiveFromType(current_app.db,tipo_sensor)], HTTPStatus.OK.value

def getAllFromZone(sz:str):
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("Los datos de la zona de sensor " + str(sz) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllFromZone(current_app.db,zona_sensor)], HTTPStatus.OK.value
 
def getAllActiveFromZone(sz:str):
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("Los datos de la zona de sensor " + str(sz) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllActiveFromZone(current_app.db,zona_sensor)], HTTPStatus.OK.value

def getAllFromTypeAndZone(st:str, sz:str):
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("Los datos del tipo de sensor " + str(st) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("Los datos de la zona de sensor " + str(sz) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllFromTypeAndZone(current_app.db,tipo_sensor,zona_sensor)], HTTPStatus.OK.value
 
def getAllActiveFromTypeAndZone(st:str, sz:str):
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("Los datos del tipo de sensor " + str(st) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("Los datos de la zona de sensor " + str(sz) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllActiveFromTypeAndZone(current_app.db,tipo_sensor,zona_sensor)], HTTPStatus.OK.value

def getAllFromModel(sm:str):
    try:
        modelo_sensor: ModeloSensor = ModeloSensor[sm]
    except(KeyError):
        return ("Los datos del modelo de sensor " + str(sm) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllFromModel(current_app.db,modelo_sensor)], HTTPStatus.OK.value
 
def getAllActiveFromModel(sm:str):
    try:
        modelo_sensor: ModeloSensor = ModeloSensor[sm]
    except(KeyError):
        return ("Los datos del modelo de sensor " + str(sm) + " no son correctos.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in SensorService.listAllFromModel(current_app.db,modelo_sensor)], HTTPStatus.OK.value


# TODO #
# metodos post para crear sensores
# metodos update para actualizar sensores
import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import SensorService, PlantaService, SensorPlantaService, TipoPlantaService
from common.data.util import Sensor as SensorCommon, Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon, TipoPlanta as TipoPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.db.exc import ErrorPlantaExiste, ErrorPlantaNoExiste, ErrorTipoPlantaNoExiste

def get(np:str) :
    nombre_planta:str = np
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,nombre_planta):
            return PlantaService.get(current_app.db, nombre_planta).toJson(), HTTPStatus.OK.value
        else:
            return ("La planta " + str(nombre_planta) + " no existe", HTTPStatus.NOT_FOUND.value)
        
def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in PlantaService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllActive() :
    with current_app.app_context() :
        return [item.toJson() for item in PlantaService.listAllActive(current_app.db)], HTTPStatus.OK.value

def getAllFromType(ntp:str):
    nombre_tipo_planta:str = ntp
    with current_app.app_context() :
        if TipoPlantaService.exists(current_app.db,nombre_tipo_planta):
            return [item.toJson() for item in PlantaService.listAllFromType(current_app.db,nombre_tipo_planta)], HTTPStatus.OK.value
        else:
            return ("El tipo de planta " + str(nombre_tipo_planta) + " no existe", HTTPStatus.NOT_FOUND.value)

def getAllActiveFromType(ntp:str):
    nombre_tipo_planta:str = ntp
    with current_app.app_context() :
        if TipoPlantaService.exists(current_app.db,nombre_tipo_planta):
            return [item.toJson() for item in PlantaService.listAllActiveFromType(current_app.db,nombre_tipo_planta)], HTTPStatus.OK.value
        else:
            return ("El tipo de planta " + str(nombre_tipo_planta) + " no existe", HTTPStatus.NOT_FOUND.value)

def post(body:dict):
    with current_app.app_context() :
        try:
            planta = PlantaCommon.fromJson(body)
            return PlantaService.createFromCommon(current_app.db,planta).toJson(), HTTPStatus.CREATED.value
        except ErrorPlantaExiste:
            return ("La planta " + str(body.get("nombre_planta")) + " ya existe.", HTTPStatus.CONFLICT.value)
        except ErrorTipoPlantaNoExiste:
            return ("El tipo de planta "  + str(body.get("tipo_planta")) + " no existe.", HTTPStatus.NOT_FOUND.value)  

def update(body:dict):
    with current_app.app_context() :
        try:
            planta = PlantaCommon.fromJson(body)
            return PlantaService.updateFromCommon(current_app.db,planta).toJson(), HTTPStatus.OK.value
        except ErrorPlantaNoExiste:
            return ("La planta " + str(body.get("nombre_planta")) + " no existe.", HTTPStatus.CONFLICT.value)
        except ErrorTipoPlantaNoExiste:
            return ("El tipo de planta "  + str(body.get("tipo_planta")) + " no existe.", HTTPStatus.NOT_FOUND.value)  

def unsubscribe(np:str) :
    nombre_planta:str = np
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,nombre_planta):
            return PlantaService.unsubscribe(current_app.db, nombre_planta).toJson(), HTTPStatus.OK.value
        else:
            return ("La planta " + str(nombre_planta) + " no existe", HTTPStatus.NOT_FOUND.value)

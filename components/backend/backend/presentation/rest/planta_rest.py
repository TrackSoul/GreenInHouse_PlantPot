import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import SensorService, PlantaService, SensorPlantaService, TipoPlantaService
from common.data.util import Sensor as SensorCommon, Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon, TipoPlanta as TipoPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida


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


# TODO #
# metodos post para crear plantas
# metodos update para actualizar plantas
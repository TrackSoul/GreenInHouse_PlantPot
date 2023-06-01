import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import SensorService, PlantaService, SensorPlantaService, TipoPlantaService
from common.data.util import Sensor as SensorCommon, Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon, TipoPlanta as TipoPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.db.exc import ErrorTipoPlantaExiste, ErrorTipoPlantaNoExiste

def get(ntp:str) :
    nombre_tipo_planta:str = ntp
    with current_app.app_context() :
        if TipoPlantaService.exists(current_app.db,nombre_tipo_planta):
            return TipoPlantaService.get(current_app.db, nombre_tipo_planta).toJson(), HTTPStatus.OK.value
        else:
            return ("El tipo de planta " + str(nombre_tipo_planta) + " no existe", HTTPStatus.NOT_FOUND.value)
        
def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in TipoPlantaService.listAll(current_app.db)], HTTPStatus.OK.value

# def post(tipo_planta:str, descripcion_planta:str):
#     with current_app.app_context() :
#         try:
#             return TipoPlantaService.create(current_app.db,tipo_planta,descripcion_planta).toJson(), HTTPStatus.CREATED.value
#         except ErrorTipoPlantaExiste:
#             return ('El Tipo de planta ya existe', HTTPStatus.CONFLICT.value)

# def update(tipo_planta:str, descripcion_planta:str):
#     with current_app.app_context() :
#         try:
#             return TipoPlantaService.update(current_app.db,tipo_planta,descripcion_planta).toJson(), HTTPStatus.CREATED.value
#         except ErrorTipoPlantaNoExiste:
#             return ('El tipo de planta no existe.', HTTPStatus.NOT_FOUND.value)

def post(body:dict):
    with current_app.app_context() :
        try:
            tipo_planta = TipoPlantaCommon.fromJson(body)
            return TipoPlantaService.createFromCommon(current_app.db,tipo_planta).toJson(), HTTPStatus.CREATED.value
        except ErrorTipoPlantaExiste:
            return ("El tipo de planta "  + str(body.get("tipo_planta")) + " ya existe.", HTTPStatus.CONFLICT.value)

def update(body:dict):
    with current_app.app_context() :
        try:
            tipo_planta = TipoPlantaCommon.fromJson(body)
            return TipoPlantaService.updateFromCommon(current_app.db,tipo_planta).toJson(), HTTPStatus.OK.value
        except ErrorTipoPlantaNoExiste:
            return ("El tipo de planta "  + str(body.get("tipo_planta")) + " no existe.", HTTPStatus.NOT_FOUND.value)  

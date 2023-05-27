import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import ConsejoPlantaService, PlantaService
from common.data.util import ConsejoPlanta as ConsejoPlantaCommon, Planta as PlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

def get(np: str, cz: str, mt: str) :
    try:
        zona_consejo: ZonaSensor = ZonaSensor[cz]
    except(KeyError):
        return ("La zona de consejo " + str(cz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value) 
    try:
        tipo_medida:TipoMedida = TipoMedida[mt]
    except(KeyError):
        return ("El tipo de medida " + str(mt) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db, np):
            nombre_planta: str = np
        else:
            return ("La planta " + str(np) + " no existe.", HTTPStatus.NOT_FOUND.value)
        if ConsejoPlantaService.exists(current_app.db, nombre_planta, zona_consejo, tipo_medida):
            return ConsejoPlantaService.get(current_app.db, nombre_planta, zona_consejo, tipo_medida).toJson(), HTTPStatus.OK.value
        else:
            return ("El consejo de la planta " + str(nombre_planta) + " para la medida " + str(tipo_medida) +
                " en la zona " + str(zona_consejo) + " no existe.", HTTPStatus.NOT_FOUND.value)
        
def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in ConsejoPlantaService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllFromPlant(np: str):
    with current_app.app_context() :
        if PlantaService.exists(current_app.db, np):
            nombre_planta: str = np
        else:
            return ("La planta " + str(np) + " no existe.", HTTPStatus.NOT_FOUND.value)
        return [item.toJson() for item in ConsejoPlantaService.listAllFromPlant(current_app.db, nombre_planta)], HTTPStatus.OK.value

def getAllFromZone(cz:str):
    try:
        zona_consejo: ZonaSensor = ZonaSensor[cz]
    except(KeyError):
        return ("La zona de consejo " + str(cz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in ConsejoPlantaService.listAllFromZone(current_app.db,zona_consejo)], HTTPStatus.OK.value

def getAllFromTypeMeasure(mt: str):
    try:
        tipo_medida:TipoMedida = TipoMedida[mt]
    except(KeyError):
        return ("El tipo de medida " + str(mt) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in ConsejoPlantaService.listAllFromTypeMeasure(current_app.db, tipo_medida)], HTTPStatus.OK.value

def getAllFromPlantAndZone(np:str, cz:str):
    try:
        zona_consejo: ZonaSensor = ZonaSensor[cz]
    except(KeyError):
        return ("La zona de consejo " + str(cz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db, np):
            nombre_planta: str = np
        else:
            return ("La planta " + str(np) + " no existe.", HTTPStatus.NOT_FOUND.value)
        return [item.toJson() for item in ConsejoPlantaService.listAllFromPlantAndZone(current_app.db, nombre_planta, zona_consejo)], HTTPStatus.OK.value

# TODO #
# metodos post para crear consejos
# metodos update para actualizar consejos
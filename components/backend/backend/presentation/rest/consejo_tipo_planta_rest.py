import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import ConsejoTipoPlantaService, TipoPlantaService
from common.data.util import ConsejoTipoPlanta as ConsejoTipoPlantaCommon, TipoPlanta as TipoPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

def get(ntp: str, cz: str, mt: str) :
    try:
        zona_consejo: ZonaSensor = ZonaSensor[cz]
    except(KeyError):
        return ("La zona de consejo " + str(cz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value) 
    try:
        tipo_medida:TipoMedida = TipoMedida[mt]
    except(KeyError):
        return ("El tipo de medida " + str(mt) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if TipoPlantaService.exists(current_app.db, ntp):
            nombre_tipo_planta: str = ntp
        else:
            return ("El tipo de planta " + str(ntp) + " no existe.", HTTPStatus.NOT_FOUND.value)
        if ConsejoTipoPlantaService.exists(current_app.db, nombre_tipo_planta, zona_consejo, tipo_medida):
            return ConsejoTipoPlantaService.get(current_app.db, nombre_tipo_planta, zona_consejo, tipo_medida).toJson(), HTTPStatus.OK.value
        else:
            return ("El consejo del tipo de planta " + str(nombre_tipo_planta) + " para la medida " + str(tipo_medida) +
                " en la zona " + str(zona_consejo) + " no existe.", HTTPStatus.NOT_FOUND.value)
        
def getAll() :
    with current_app.app_context() :
        return [item.toJson() for item in ConsejoTipoPlantaService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllFromTypePlant(ntp: str):
    with current_app.app_context() :
        if TipoPlantaService.exists(current_app.db, ntp):
            nombre_tipo_planta: str = ntp
        else:
            return ("El tipo de planta " + str(ntp) + " no existe.", HTTPStatus.NOT_FOUND.value)
        return [item.toJson() for item in ConsejoTipoPlantaService.listAllFromTypePlant(current_app.db, nombre_tipo_planta)], HTTPStatus.OK.value

def getAllFromZone(cz:str):
    try:
        zona_consejo: ZonaSensor = ZonaSensor[cz]
    except(KeyError):
        return ("La zona de consejo " + str(cz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in ConsejoTipoPlantaService.listAllFromZone(current_app.db,zona_consejo)], HTTPStatus.OK.value

def getAllFromTypeMeasure(mt: str):
    try:
        tipo_medida:TipoMedida = TipoMedida[mt]
    except(KeyError):
        return ("El tipo de medida " + str(mt) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        return [item.toJson() for item in ConsejoTipoPlantaService.listAllFromTypeMeasure(current_app.db, tipo_medida)], HTTPStatus.OK.value

def getAllFromTypePlantAndZone(ntp:str, cz:str):
    try:
        zona_consejo: ZonaSensor = ZonaSensor[cz]
    except(KeyError):
        return ("La zona de consejo " + str(cz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if TipoPlantaService.exists(current_app.db, ntp):
            nombre_tipo_planta: str = ntp
        else:
            return ("El tipo de planta " + str(ntp) + " no existe.", HTTPStatus.NOT_FOUND.value)
        return [item.toJson() for item in ConsejoTipoPlantaService.listAllFromTypePlantAndZone(current_app.db, nombre_tipo_planta, zona_consejo)], HTTPStatus.OK.value

# TODO #
# metodos post para crear consejos
# metodos update para actualizar consejos
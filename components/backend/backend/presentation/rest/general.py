import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import RegistroSensorService, PlantaService, GeneralService
from common.data.util import RegistroSensor as RegistroSensorCommon, Planta as PlantaCommon
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida

def getAllFromPlant(np:str):
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            return [item.toJson() for item in GeneralService.listRegistrosPlanta(current_app.db, np)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)

def getAllFromPlantBetweenDates(np:str, ff: str = str(datetime.now())):
    try:
        fecha_inicio=datetime.fromisoformat(fi)
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en las fechas especificadas.", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio no puede ser mayor que la fecha de fin.", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            return [item.toJson() for item in GeneralService.listRegistrosPlanta(current_app.db, np)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)  

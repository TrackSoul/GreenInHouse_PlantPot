import traceback
from datetime import datetime
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import SensorService, PlantaService, SensorPlantaService, TipoPlantaService
from common.data.util import Sensor as SensorCommon, Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon, TipoPlanta as TipoPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

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


# TODO #
# metodos post para crear plantas
# metodos update para actualizar plantas
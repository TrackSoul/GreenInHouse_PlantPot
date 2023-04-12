from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session
from backend.data.db.esquema import Esquema
from backend.data.db.results import Sensor, Planta, RegistroSensor, TipoPlanta, SensorPlanta
from backend.data.db.resultsets import SensorSet,PlantaSet, RegistroSensorSet, TipoPlantaSet, SensorPlantaSet
from backend.service import SensorService, PlantaService, RegistroSensorService, TipoPlantaService, SensorPlantaService
from common.data.util import Sensor as SensorCommon, RegistroSensor as RegistroSensorCommon, Planta as PlantaCommon
from common.data.util import TipoPlanta as TipoPlantaCommon, SensorPlanta as SensorPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class GeneralService():

    @staticmethod
    def readRegistrosPlanta(esquema: Esquema, planta: Planta) -> List[RegistroSensorCommon]:
        lista_registros: List[RegistroSensorCommon] = []
        for sensor in SensorPlantaService.listAllSensorsPlantFromCommon(esquema, planta):

            print(str(reg))   
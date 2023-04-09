from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session
from backend.data.db.esquema import Esquema
from backend.data.db.results import Sensor, Planta, RegistroSensor, TipoPlanta, SensorPlanta
from backend.data.db.resultsets import SensorSet,PlantaSet, RegistroSensorSet, TipoPlantaSet, SensorPlantaSet
from backend.service import SensorService, PlantaService, RegistroSensorService, TipoPlantaService, SensorPlantaService
from backend.data.util import SensorBackend
from common.data.util import Sensor as SensorCommon, RegistroSensor as RegistroSensorCommon, Planta as PlantaCommon
from common.data.util import TipoPlanta as TipoPlantaCommon, SensorPlanta as SensorPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class ElectronicSensorService():
    
    @staticmethod
    def readSensor(esquema: Esquema, sensor: SensorCommon) -> List[RegistroSensorCommon]:
        return SensorBackend(sensor).readSensorAndCreateRecords()    

    @staticmethod
    def readSensors(esquema: Esquema, sensores: List[SensorCommon]) -> List[RegistroSensorCommon]:
        registros: List[RegistroSensorCommon] = []
        for sensor in sensores:
            for registro in ElectronicSensorService.readSensor(esquema, sensor):
                registros.append(registro)
        return registros       

    @staticmethod
    def readActiveSensors(esquema: Esquema) -> List[RegistroSensorCommon]:
        return ElectronicSensorService.readSensors(esquema, SensorService.listAllActive(esquema))      

    @staticmethod
    def SaveRecord(esquema: Esquema, registro: RegistroSensorCommon) -> List[RegistroSensorCommon]:
        RegistroSensorService.createFromCommon(esquema,registro)

    @staticmethod
    def SaveRecords(esquema: Esquema, registros: List[RegistroSensorCommon]) -> List[RegistroSensorCommon]:
        for registro in registros:
            ElectronicSensorService.SaveRecord(esquema,registro)

    @staticmethod
    def readSensorAndSaveRecords(esquema: Esquema, sensor: SensorCommon) -> List[RegistroSensorCommon]:
        registros: List[RegistroSensorCommon] = ElectronicSensorService.readSensor(esquema, sensor)
        ElectronicSensorService.SaveRecords(esquema, registros)
        return registros      

    @staticmethod
    def readSensorsAndSaveRecords(esquema: Esquema, sensores: List[SensorCommon]) -> List[RegistroSensorCommon]:
        registros: List[RegistroSensorCommon] = ElectronicSensorService.readSensors(esquema, sensores)
        ElectronicSensorService.SaveRecords(esquema, registros)
        return registros 

    @staticmethod
    def readActiveSensorsAndSaveRecords(esquema: Esquema) -> List[RegistroSensorCommon]:
        registros: List[RegistroSensorCommon] = ElectronicSensorService.readActiveSensors(esquema)
        ElectronicSensorService.SaveRecords(esquema, registros)
        return registros 

from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import Sensor as SensorCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico, SensorElectronicoDHT11
class FactoriaSensor ():

    @staticmethod
    def getSensorElectronico(sensor_common: SensorCommon) -> SensorElectronico :
        
        sensor_electronico: SensorElectronico = SensorElectronico(sensor_common)
        if sensor_common.getModeloSensor() == ModeloSensor.DHT11:
            sensor_electronico = SensorElectronicoDHT11(sensor_common)
        elif sensor_common.getModeloSensor() == ModeloSensor.OTRO:
            sensor_electronico = SensorElectronico(sensor_common)
        '''
        match str(sensor_common.getModeloSensor()):
            case str(ModeloSensor.DHT11):
                sensor_electronico = SensorElectronicoDHT11(sensor_common)
            case str(ModeloSensor.OTRO):
                sensor_electronico = SensorElectronico(sensor_common)
            case _:
                sensor_electronico = SensorElectronico(sensor_common)
        '''
        return sensor_electronico
        

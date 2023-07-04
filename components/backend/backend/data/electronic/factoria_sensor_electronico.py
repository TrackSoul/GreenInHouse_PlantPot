#Author: Oscar Valverde Escobar

from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import Sensor as SensorCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico, SensorElectronicoDHT11, SensorElectronicoFC28
from backend.data.electronic import SensorElectronicoLDR, SensorElectronicoLM35, SensorElectronicoBH1750

class FactoriaSensorElectronico ():

    @staticmethod
    def getSensorElectronico(sensor_common: SensorCommon) -> SensorElectronico :
        
        sensor_electronico: SensorElectronico = SensorElectronico(sensor_common)
        if sensor_common.getModeloSensor() == ModeloSensor.DHT11:
            sensor_electronico = SensorElectronicoDHT11(sensor_common)
        elif sensor_common.getModeloSensor() == ModeloSensor.FC28:
            sensor_electronico = SensorElectronicoFC28(sensor_common)
        elif sensor_common.getModeloSensor() == ModeloSensor.LDR:
            sensor_electronico = SensorElectronicoLDR(sensor_common)
        elif sensor_common.getModeloSensor() == ModeloSensor.LM35:
            sensor_electronico = SensorElectronicoLM35(sensor_common)
        elif sensor_common.getModeloSensor() == ModeloSensor.BH1750:
            sensor_electronico = SensorElectronicoBH1750(sensor_common)
        elif sensor_common.getModeloSensor() == ModeloSensor.OTRO:
            sensor_electronico = SensorElectronico(sensor_common)
        return sensor_electronico
        

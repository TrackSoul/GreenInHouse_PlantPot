""" 
Enumeracion de modelos de sensores.
"""

from enum import Enum
from common.data.util import TipoSensor, ZonaSensor

class ModeloSensor(Enum):
    """ 
    Enumeracion con las zonas de los sensores
    """
    SIN_MODELO = 0, "Sin modelo", TipoSensor.SIN_TIPO, ZonaSensor.SIN_ZONA
    DHT11 = 1, "DHT11", TipoSensor.TEMPERATURA_Y_HUMEDAD, ZonaSensor.AMBIENTE
    LDR = 2, "LDR", TipoSensor.LUMINOSIDAD, ZonaSensor.AMBIENTE
    LM35 = 3, "LM35", TipoSensor.TEMPERATURA, ZonaSensor.AMBIENTE
    FC28 = 3, "FC28", TipoSensor.HUMEDAD, ZonaSensor.MACETA
    OTRO = 99, "Otro", TipoSensor.OTRO, ZonaSensor.OTRA

    def __new__(cls, value: int, nombre, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor):
        member = object.__new__(cls)
        member.__value:int = value
        member.__nombre:str = nombre
        member.__tipo_sensor:TipoSensor = tipo_sensor
        member.__zona_sensor:ZonaSensor = zona_sensor
        return member

    def __int__(self):
        return self.__value
    
    def __str__(self):
        return self.__nombre

    def getTipoSensor(self) -> TipoSensor:
        return self.__tipo_sensor

    def getZonaSensor(self) -> ZonaSensor:
        return self.__zona_sensor

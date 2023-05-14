""" 
Enumeracion de modelos de sensores.
"""

from enum import Enum
from common.data.util import TipoSensor, ZonaSensor

class ModeloSensor(Enum):

    SIN_MODELO = 0, "Sin modelo", "SIN_MODELO", TipoSensor.SIN_TIPO, ZonaSensor.SIN_ZONA
    DHT11 = 1, "DHT11", "DHT11", TipoSensor.TEMPERATURA_Y_HUMEDAD, ZonaSensor.AMBIENTE
    LDR = 2, "LDR", "LDR", TipoSensor.LUMINOSIDAD, ZonaSensor.AMBIENTE
    LM35 = 3, "LM35", "LM35", TipoSensor.TEMPERATURA, ZonaSensor.AMBIENTE
    FC28 = 3, "FC28", "FC28", TipoSensor.HUMEDAD, ZonaSensor.MACETA
    OTRO = 99, "Otro", "OTRO", TipoSensor.OTRO, ZonaSensor.OTRA

    def __new__(cls, value: int, nombre, tipo, 
                tipo_sensor: TipoSensor, zona_sensor: ZonaSensor):
        member = object.__new__(cls)
        member.__value: int = value
        member.__nombre: str = nombre
        member.__tipo: str = tipo
        member.__tipo_sensor: TipoSensor = tipo_sensor
        member.__zona_sensor: ZonaSensor = zona_sensor
        return member

    def __int__(self):
        return self.__value
    
    def __str__(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo

    def getTipoSensor(self) -> TipoSensor:
        return self.__tipo_sensor

    def getZonaSensor(self) -> ZonaSensor:
        return self.__zona_sensor
    
    def toJson(self) -> dict:
        dic={}
        dic["value"]=int(self)
        dic["nombre"]=str(self)
        dic["tipo"]=self.getTipo()
        dic["tipo sensor"]=self.getTipoSensor().toJson()
        dic["tipo medida"]=self.getZonaSensor().toJson()
        return dict

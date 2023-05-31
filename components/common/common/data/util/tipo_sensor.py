""" 
Enumeracion de tipos de sensores.
"""

from typing import List
from enum import Enum
from common.data.util.tipo_medida import TipoMedida

class TipoSensor(Enum):

    SIN_TIPO = 0, "Sin tipo", "SIN_TIPO", [TipoMedida.SIN_TIPO]
    HUMEDAD = 1, "Humedad", "HUMEDAD", [TipoMedida.HUMEDAD]
    TEMPERATURA = 2, "Temperatura", "TEMPERATURA", [TipoMedida.TEMPERATURA]
    TEMPERATURA_Y_HUMEDAD = 3, "Temperatura y Humedad", "TEMPERATURA_Y_HUMEDAD", [TipoMedida.TEMPERATURA,TipoMedida.HUMEDAD]
    LUMINOSIDAD = 4, "Luminosidad", "LUMINOSIDAD", [TipoMedida.LUMINOSIDAD]
    OTRO = 99, "Otro", "OTRO", [TipoMedida.OTRO]

    def __new__(cls, value, nombre, tipo,
                tipos_medida: List[TipoMedida]):
        member = object.__new__(cls)
        member.__value: int = value
        member.__nombre: str = nombre
        member.__tipo: str = tipo
        member.__tipos_medida: List[TipoMedida] = tipos_medida
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo

    def getTiposMedida(self) -> List[TipoMedida]:
        return self.__tipos_medida

    def getTipoMedida(self, val:int=0) -> TipoMedida:
        if val < len(self.__tipos_medida):
            return self.__tipos_medida[val]
        else:
            return TipoMedida.SIN_TIPO
            # return None
    
    def toJson(self) -> dict:
        dic={}
        dic["value"]=int(self)
        dic["nombre"]=str(self)
        dic["tipo"]=self.getTipo()
        dic["tipos_medida"]=[tipo_medida.toJson() for tipo_medida in self.getTiposMedida()]
        return dict

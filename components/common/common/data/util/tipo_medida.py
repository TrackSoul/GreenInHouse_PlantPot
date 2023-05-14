""" 
Enumeracion de tipos de sensores.
"""

from enum import Enum


class TipoMedida(Enum):

    SIN_TIPO = 0, "Sin tipo", "SIN_TIPO"
    HUMEDAD = 1, "Humedad", "HUMEDAD"
    TEMPERATURA = 2, "Temperatura", "TEMPERATURA"
    LUMINOSIDAD = 3, "Luminosidad", "LUMINOSIDAD"
    OTRO = 99, "Otro", "OTRO"

    def __new__(cls, value, nombre, tipo):
        member = object.__new__(cls)
        member.__value: int = value
        member.__nombre: str = nombre
        member.__tipo: str = tipo
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo

    def toJson(self) -> dict:
        dic={}
        dic["value"]=int(self)
        dic["nombre"]=str(self)
        dic["tipo"]=self.getTipo()
        return dict

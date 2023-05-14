""" 
Enumeracion de zonas de sensores.
"""

from enum import Enum

class ZonaSensor(Enum):

    SIN_ZONA = 0, "Sin zona", "SIN_ZONA"
    AMBIENTE = 1, "Ambiente", "AMBIENTE"
    MACETA = 2, "Maceta", "MACETA"
    SUELO = 3, "Suelo", "SUELO"
    OTRA = 99, "Otra", "OTRA"

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
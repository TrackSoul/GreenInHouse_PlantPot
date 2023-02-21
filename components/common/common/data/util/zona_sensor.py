""" 
Enumeracion de zonas de sensores.
"""

from enum import Enum

class ZonaSensor(Enum):
    """ 
    Enumeracion con las zonas de los sensores
    """
    AMBIENTE = 1, "Ambiente"
    MACETA = 2, "Maceta"
    SUELO = 3, "Suelo"
    OTRA = 99, "Otra"

    def __new__(cls, value, nombre):
        member = object.__new__(cls)
        member.__value = value
        member.__nombre = nombre
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre

    
""" 
Enumeracion de unidades de medida de sensores.
"""

from enum import Enum

class UnidadMedida(Enum):
    """ 
    Enumeracion con las unidades de medida de los sensores
    """
    GRADOS_CENTIGRADOS = 1, "ºC"
    GRADOS_FARENHEIT = 2, "ºF"
    PORCENTAJE = 3, "%"
    LUMENES = 4, "Lux"
    SIN_UNIDAD = 98, "Sin unidad"
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
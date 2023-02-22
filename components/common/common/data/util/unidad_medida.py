""" 
Enumeracion de unidades de medida de sensores.
"""
'''
from enum import Enum

class UnidadMedida(Enum):
    """ 
    Enumeracion con las unidades de medida de los sensores
    """
    SIN_UNIDAD = 0, "Sin unidad"
    PORCENTAJE = 1, "%"
    GRADOS_CENTIGRADOS = 2, "ºC"
    GRADOS_FARENHEIT = 3, "ºF"
    LUMENES = 4, "Lux"
    OTRO = 99, "Otra"

    def __new__(cls, value, nombre):
        member = object.__new__(cls)
        member.__value = value
        member.__nombre = nombre
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre

'''

from typing import List
from enum import Enum
from common.data.util.tipo_medida import TipoMedida

class UnidadMedida(Enum):
    """ 
    Enumeracion con las unidades de medida de los sensores
    """
    SIN_UNIDAD = 0, "Sin unidad", [TipoMedida.SIN_TIPO]
    PORCENTAJE = 1, "%", [TipoMedida.HUMEDAD]
    GRADOS_CENTIGRADOS = 2, "ºC", [TipoMedida.TEMPERATURA]
    GRADOS_FARENHEIT = 3, "ºF", [TipoMedida.TEMPERATURA]   
    LUMENES = 4, "Lux", [TipoMedida.LUMINOSIDAD]
    OTRO = 99, "Otra", [TipoMedida.OTRO]        

    def __new__(cls, value, nombre, 
                tipos_medida: List[TipoMedida]):
        member = object.__new__(cls)
        member.__value = value
        member.__nombre = nombre
        member.__tipos_medida: List[TipoMedida] = tipos_medida
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre

    def getTiposMedida(self) -> List[TipoMedida]:
        return self.__tipos_medida

    def getTipoMedida(self, val:int=0) -> TipoMedida:
        #try:
        if val < len(self.__tipos_medida):
            return self.__tipos_medida[val]
        #except IndexError as ex:
        else:
            return TipoMedida.SIN_TIPO

""" 
Enumeracion de tipos de sensores.
"""

from enum import Enum


class TipoMedida(Enum):
    """ 
    Enumeracion con los tipos de sensores
    """
    SIN_TIPO = 0, "Sin tipo"
    HUMEDAD = 1, "Humedad"
    TEMPERATURA = 2, "Temperatura"
    LUMINOSIDAD = 3, "Luminosidad"
    OTRO = 99, "Otro"

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
from common.data.util.unidad_medida import UnidadMedida

class TipoMedida(Enum):
    """ 
    Enumeracion con los tipos de sensores
    """
    SIN_TIPO = 0, "Sin tipo", [UnidadMedida.SIN_UNIDAD]
    HUMEDAD = 1, "Humedad", [UnidadMedida.PORCENTAJE]
    TEMPERATURA = 2, "Temperatura", [UnidadMedida.GRADOS_CENTIGRADOS, UnidadMedida.GRADOS_FARENHEIT]
    LUMINOSIDAD = 3, "Luminosidad", [UnidadMedida.LUMENES]
    OTRO = 99, "Otro", [UnidadMedida.OTRA]

    def __new__(cls, value, nombre, 
                unidades_medida: List[UnidadMedida]):
        member = object.__new__(cls)
        member.__value = value
        member.__nombre = nombre
        member.__unidades_medida: List[UnidadMedida] = unidades_medida
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre
    
    def getUnidadesMedida(self) -> List[UnidadMedida]:
        return self.__unidadess_medida

    def getUnidadMedida(self, val:int) -> UnidadMedida:
        #try:
        if val < len(self.__unidades_medida):
            return self.__unidades_medida[val]
        #except IndexError as ex:
        else:
            return UnidadMedida.SIN_UNIDAD
'''

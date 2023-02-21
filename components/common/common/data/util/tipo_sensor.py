""" 
Enumeracion de tipos de sensores.
"""

from enum import Enum
from common.data.util import UnidadMedida

class TipoSensor(Enum):
    """ 
    Enumeracion con los tipos de sensores
    """
    HUMEDAD = 1, "Humedad", UnidadMedida.PORCENTAJE
    TEMPERATURA = 2, "Temperatura", UnidadMedida.GRADOS_CENTIGRADOS, UnidadMedida.GRADOS_FARENHEIT
    TEMPERATURA_Y_HUMEDAD = 3, "Temperatura y Humedad", UnidadMedida.GRADOS_CENTIGRADOS, UnidadMedida.GRADOS_FARENHEIT , UnidadMedida.PORCENTAJE
    LUMINOSIDAD = 4, "Luminosidad", UnidadMedida.LUMENES
    OTRO = 99, "Otro", UnidadMedida.OTRA

    def __new__(cls, value, nombre, 
                unidad_medida_1:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                unidad_medida_2:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                unidad_medida_3:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                unidad_medida_4:UnidadMedida = UnidadMedida.SIN_UNIDAD):
        member = object.__new__(cls)
        member.__value = value
        member.__nombre = nombre
        member.__unidad_medida_1:str = unidad_medida_1
        member.__unidad_medida_2:str = unidad_medida_2
        member.__unidad_medida_3:str = unidad_medida_3
        member.__unidad_medida_4:str = unidad_medida_4
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre

    def getUnidadMedida1(self) -> UnidadMedida:
        return self.__unidad_medida_1
    
    def getUnidadMedida2(self) -> UnidadMedida:
        return self.__unidad_medida_2
    
    def getUnidadMedida3(self) -> UnidadMedida:
        return self.__unidad_medida_3

    def getUnidadMedida4(self) -> UnidadMedida:
        return self.__unidad_medida_4
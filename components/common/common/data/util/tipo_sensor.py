""" 
Enumeracion de tipos de sensores.
"""
from typing import List
from enum import Enum
from common.data.util.tipo_medida import TipoMedida

class TipoSensor(Enum):
    """ 
    Enumeracion con los tipos de sensores
    """
    SIN_TIPO = 0, "Sin tipo", [TipoMedida.SIN_TIPO]
    HUMEDAD = 1, "Humedad", [TipoMedida.HUMEDAD]
    TEMPERATURA = 2, "Temperatura", [TipoMedida.TEMPERATURA]
    TEMPERATURA_Y_HUMEDAD = 3, "Temperatura y Humedad", [TipoMedida.TEMPERATURA,TipoMedida.HUMEDAD]
    LUMINOSIDAD = 4, "Luminosidad", [TipoMedida.LUMINOSIDAD]
    OTRO = 99, "Otro", [TipoMedida.OTRO]

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

    def getTipoMedida(self, val:int) -> TipoMedida:
        #try:
        if val < len(self.__tipos_medida):
            return self.__tipos_medida[val]
        #except IndexError as ex:
        else:
            return TipoMedida.SIN_TIPO

'''
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
'''
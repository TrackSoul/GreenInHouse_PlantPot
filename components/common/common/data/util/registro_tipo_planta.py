from datetime import datetime
from typing import Optional,Dict,List

class RegistroTipoPlanta:

    def __init__(self, tipo_planta:str, descripcion_planta:str):
        self.__tipo_planta:str = tipo_planta
        self.__descripcion_planta:str = descripcion_planta

    def getTipoPlanta(self) -> str:
        return self.__tipo_planta

    def setTipoPlanta(self, tipo_planta: str):
        self.__tipo_planta = tipo_planta

    def getDescripcionPlanta(self) -> str:
        return self.__descripcion_planta

    def setDescripcionPlanta(self, descripcion_planta: str):
        self.__descripcion_planta = descripcion_planta

    def toString(self) -> str:
        texto: str = str("El tipo planta " + str(self.getTipoPlanta()) + " es: " +  
                          str(self.getDescripcionPlanta()))
        return texto

    def toJson(self) -> Dict:
        dict={}
        dict["tipo_planta"]=self.getTipoPlanta()
        dict["descripcion_planta"]=self.getDescripcionPlanta()
        return dict

    def fromJson(dict: dict):
        tipo_planta = RegistroTipoPlanta(dict["tipo_planta"],dict["descripcion_planta"])
        return tipo_planta
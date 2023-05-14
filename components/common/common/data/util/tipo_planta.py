from datetime import datetime
from typing import Optional,Dict,List

class TipoPlanta:

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

    def __str__(self) -> str:
        texto: str = str("El tipo planta " + str(self.getTipoPlanta()) + " es: " +  
                          str(self.getDescripcionPlanta()))
        return texto

    def toJson(self) -> Dict:
        dic={}
        dic["tipo_planta"]=self.getTipoPlanta()
        dic["descripcion_planta"]=self.getDescripcionPlanta()
        return dic

    @staticmethod
    def fromJson(dic: dict):
        tipo_planta = TipoPlanta(tipo_planta=dic.get("tipo_planta"),
                                 descripcion_planta=dic.get("descripcion_planta"))
        return tipo_planta
from datetime import datetime
from typing import Optional,Dict,List

class RegistroPlanta:

    def __init__(self, nombre_planta:str, tipo_planta:str, fecha_plantacion: datetime = None, fecha_marchitacion: datetime = None):
        self.__nombre_planta:str = nombre_planta
        self.__tipo_planta:str = tipo_planta
        self.__fecha_plantacion:datetime = fecha_plantacion
        self.__fecha_marchitacion:datetime = fecha_marchitacion

    def getNombrePlanta(self) -> str:
        return self.__nombre_planta

    def setNombrePlanta(self, nombre_planta: str):
        self.__nombre_planta = nombre_planta

    def getTipoPlanta(self) -> str:
        return self.__tipo_planta

    def setTipoPlanta(self, tipo_planta: str):
        self.__tipo_planta = tipo_planta

    def getFechaPlantacion(self) -> datetime:
        return self.__fecha_plantacion

    def setFechaPlantacion(self, fecha_plantacion: datetime):
        self.__fecha_plantacion = fecha_plantacion

    def getFechaMarchitacion(self) -> datetime:
        return self.__fecha_marchitacion

    def setFechaMarchitacion(self, fecha_marchitacion: datetime):
        self.__fecha_marchitacion = fecha_marchitacion
    
    def to_json(self) -> Dict:
        dict={}
        dict["nombre_planta"]=self.__nombre_planta()
        dict["tipo_planta"]=self.__tipo_planta()
        dict["fecha_plantacion"]=self.__fecha_plantacion()
        dict["fecha_marchitacion"]=self.__fecha_marchitacion()
        return dict

    def from_json(dict: dict):
        planta = RegistroPlanta(dict["nombre_planta"],dict["tipo_planta"],dict["fecha_plantacion"],dict["fecha_marchitacion"])
        return planta

from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data import TipoSensor, ZonaSensor

class SensorPlanta:

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor:ZonaSensor ,numero_sensor:str, nombre_planta:str,
                 fecha_asociacion: datetime = None, fecha_anulacion: datetime = None, id: int = 0):
        self.__id:int = id
        self.__tipo_sensor:TipoSensor = tipo_sensor
        self.__zona_sensor:ZonaSensor = zona_sensor
        self.__numero_sensor:int = numero_sensor
        self.__nombre_planta:str = nombre_planta
        self.__fecha_asociacion:datetime = fecha_asociacion
        self.__fecha_anulacion:datetime = fecha_anulacion
        
    def getId(self) -> Optional[int]:
        return self.__id

    def getTipoSensor(self) -> TipoSensor:
        return self.__tipo_sensor
    
    def setTipoSensor(self, tipo_sensor:TipoSensor):
        self.__tipo_sensor = tipo_sensor
    
    def getZonaSensor(self) -> ZonaSensor:
        return self.__zona_sensor
    
    def setZonaSensor(self, zona_sensor:ZonaSensor):
        self.__zona_sensor = zona_sensor

    def getNumeroSensor(self) -> int:
        return self.__numero_sensor
    
    def setNumeroSensor(self, numero_sensor:int):
        self.__numero_sensor = numero_sensor

    def getNombrePlanta(self) -> str:
         return self.__nombre_planta

    def getFechaAsociacion(self) -> Optional[datetime]:
        return self.__fecha_asociacion
    
    def setFechaAsociacion(self, fecha_asociacion:datetime):
        self.__fecha_asociacion = fecha_asociacion

    def getFechaAnulacion(self) -> Optional[datetime]:
        return self.__fecha_anulacion
    
    def setFechaAnulacion(self, fecha_anulacion:datetime):
        self.__fecha_anulacion = fecha_anulacion


    def to_json(self) -> Dict:
        dict={}
        dict["id"]=self.getId()
        dict["tipo_sensor"]=self.getTipoSensor()
        dict["zona_sensor"]=self.getZonaSensor()
        dict["numero_sensor"]=self.getNumeroSensor()
        dict["nombre_planta"]=self.getNombrePlanta()
        dict["fecha_asociacion"]=self.getFechaAsociacion()
        dict["fecha_anulacion"]=self.getFechaAnulacion()
        return dict

    def from_json(dict: dict):
        sensor = SensorPlanta(dict["id"],dict["tipo_sensor"],dict["zona_sensor"],dict["numero_sensor"],
                                dict["nombre_planta"],dict["fecha_asociacion"],dict["fecha_anulacion"])
        return sensor

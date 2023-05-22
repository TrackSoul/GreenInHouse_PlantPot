from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor

class SensorPlanta:

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor:ZonaSensor ,numero_sensor:str, nombre_planta:str,
                 fecha_asociacion: datetime = None, fecha_anulacion: datetime = None, id_: int = 0):
        self.__tipo_sensor:TipoSensor = tipo_sensor
        self.__zona_sensor:ZonaSensor = zona_sensor
        self.__numero_sensor:int = numero_sensor
        self.__nombre_planta:str = nombre_planta
        self.__fecha_asociacion:datetime = fecha_asociacion
        self.__fecha_anulacion:datetime = fecha_anulacion
        self.__id:int = id_

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
    
    def setNombrePlanta(self, nombre_planta:str):
        self.__nombre_planta = nombre_planta

    def getFechaAsociacion(self) -> Optional[datetime]:
        return self.__fecha_asociacion
    
    def setFechaAsociacion(self, fecha_asociacion:datetime):
        self.__fecha_asociacion = fecha_asociacion

    def getFechaAnulacion(self) -> Optional[datetime]:
        return self.__fecha_anulacion
    
    def setFechaAnulacion(self, fecha_anulacion:datetime):
        self.__fecha_anulacion = fecha_anulacion
    
    def getId(self) -> Optional[int]:
        return self.__id

    def __str__(self) -> str:
        texto: str = str("La planta " + str(self.getNombrePlanta()) + " esta asociada con el sensor " +  
                          str(self.getNumeroSensor()) + " de " + str(self.getTipoSensor()) + " de la zona " + 
                          str(self.getZonaSensor()) + " mediante el id " + str(self.getId()) + 
                          " desde la fecha " + str(self.getFechaAsociacion()))
        if self.getFechaAnulacion() is None:
            texto: str  = str(texto + " hasta la actualidad.")
        else:
            texto: str  = str(texto + " hasta la fecha " + str(self.getFechaAnulacion()) + " .")
        return texto

    def toJson(self) -> dict:
        dic={}
        dic["tipo_sensor"]={"nombre": str(self.getTipoSensor()),
                            "tipo": self.getTipoSensor().getTipo()}
        #dic["tipo_sensor"]=self.getTipoSensor().toJson()
        dic["zona_sensor"]={"nombre": str(self.getZonaSensor()),
                            "tipo": self.getZonaSensor().getTipo()}
        #dic["zona_sensor"]=self.getZonaSensor().toJson()
        dic["numero_sensor"]=self.getNumeroSensor()
        dic["nombre_planta"]=self.getNombrePlanta()
        dic["fecha_asociacion"]=self.getFechaAsociacion()
        dic["fecha_anulacion"]=self.getFechaAnulacion() if self.getFechaAnulacion() is not None else None
        dic["id"]=self.getId()
        return dic

    @staticmethod
    def fromJson(dic: dict):
        sensor = SensorPlanta(tipo_sensor=dic.get("tipo_sensor").get("tipo"),
                              zona_sensor=dic.get("zona_sensor").get("tipo"),
                              numero_sensor=dic.get("numero_sensor"), 
                              nombre_planta=dic.get("nombre_planta"),
                              fecha_asociacion=datetime.fromisoformat(dic.get("fecha_asociacion")),
                              fecha_anulacion=datetime.fromisoformat(dic.get("fecha_anulacion")) if dic.get("fecha_anulacion") is not None else None,
                              id_=dic.get("id"))
        return sensor

from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data import TipoSensor, ZonaSensor

class Sensor:

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, modelo_sensor:str, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int=None, patilla_3_lectura:int=None, patilla_4_lectura:int=None ):
        #self.__id:int = id
        self.__tipo_sensor: TipoSensor = tipo_sensor
        self.__zona_sensor: ZonaSensor = zona_sensor
        self.__numero_sensor: int = numero_sensor
        self.__modelo_sensor: str = modelo_sensor
        self.__direccion_lectura: str = direccion_lectura
        self.__patilla_1_lectura: int = patilla_1_lectura
        self.__patilla_2_lectura: int = patilla_2_lectura
        self.__patilla_3_lectura: int = patilla_3_lectura
        self.__patilla_4_lectura: int = patilla_4_lectura
        
    # def getId(self) -> Optional[int]:
    #     return self.__id

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

    def getModeloSensor(self) -> str:
        return self.__modelo_sensor
    
    def setModeloSensor(self, modelo_sensor:str):
        self.__modelo_sensor = modelo_sensor

    def getDireccionLectura(self) -> Optional[str]:
        return self.__direccion_lectura
    
    def setDireccionLectura(self, direccion_lectura:str):
        self.__direccion_lectura = direccion_lectura

    def getPatilla1Lectura(self) -> Optional[int]:
        return self.__patilla_1_lectura
    
    def setPatilla1Lectura(self, patilla_1_lectura:int):
        self.__patilla_1_lectura = patilla_1_lectura

    def getPatilla2Lectura(self) -> Optional[int]:
        return self.__patilla_2_lectura
    
    def setPatilla2Lectura(self, patilla_2_lectura:int):
        self.__patilla_2_lectura = patilla_2_lectura

    def getPatilla3Lectura(self) -> Optional[int]:
        return self.__patilla_3_lectura
    
    def setPatilla3Lectura(self, patilla_3_lectura:int):
        self.__patilla_3_lectura = patilla_3_lectura

    def getPatilla4Lectura(self) -> Optional[int]:
        return self.__patilla_4_lectura
    
    def setPatilla4Lectura(self, patilla_4_lectura:int):
        self.__patilla_4_lectura = patilla_4_lectura

    def to_json(self) -> Dict:
        dict={}
        #dict["id"]=self.getId()
        dict["tipo_sensor"]=self.getTipoSensor()
        dict["zona_sensor"]=self.getZonaSensor()
        dict["numero_sensor"]=self.getNumeroSensor()
        dict["modelo_sensor"]=self.getModeloSensor()
        dict["direccion_lectura"]=self.getDireccionLectura()
        dict["patilla_1_lectura"]=self.getPatilla1Lectura()
        dict["patilla_2_lectura"]=self.getPatilla2Lectura()
        dict["patilla_3_lectura"]=self.getPatilla3Lectura()
        dict["patilla_4_lectura"]=self.getPatilla4Lectura()
        return dict
    
    def from_json(dict: dict):
        sensor = RegistroSensor(dict["tipo_sensor"],dict["zona_sensor"],dict["numero_sensor"],dict["modelo_sensor"],
                                 dict["direccion_lectura"], dict["patilla_1_lectura"], dict["patilla_2_lectura"], 
                                 dict["patilla_3_lectura"], dict["patilla_4_lectura"])
        return sensor

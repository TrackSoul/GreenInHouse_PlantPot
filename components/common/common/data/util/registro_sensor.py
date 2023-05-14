from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida

class RegistroSensor:

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor:ZonaSensor ,numero_sensor:int, valor:float, 
                 unidad_medida: UnidadMedida,  fecha:datetime = datetime.now(), id_: int=0):
        self.__id:int = id_
        self.__tipo_sensor:TipoSensor = tipo_sensor
        self.__zona_sensor:ZonaSensor = zona_sensor
        self.__numero_sensor:int = numero_sensor
        self.__valor:float = valor
        self.__unidad_medida:UnidadMedida = unidad_medida
        self.__fecha:datetime = fecha
        
    def getId(self) -> Optional[int]:
        return self.__id

    def getTipoSensor(self) -> TipoSensor:
        return self.__tipo_sensor
    
    def getZonaSensor(self) -> ZonaSensor:
        return self.__zona_sensor

    def getNumeroSensor(self) -> int:
        return self.__numero_sensor

    def getValor(self) -> float:
        return self.__valor
      
    def getUnidadMedida(self) -> UnidadMedida:
        return self.__unidad_medida

    def getFecha(self) -> datetime:
        return self.__fecha

    def __str__(self) -> str:
        texto: str = str("El registro " + str(self.getId()) + " del sensor " +  str(self.getNumeroSensor()) + 
                          " de " + str(self.getTipoSensor()) + " de la zona " + str(self.getZonaSensor()) + 
                          " es " + str(self.getValor()) + str(self.getUnidadMedida()) +
                          " y fue creado en la fecha " + str(self.getFecha()) + " .")
        return texto

    def toJson(self) -> Dict:
        dic={}
        dic["id_"]=self.getId()
        dic["tipo_sensor"]={"str": str(self.getTipoSensor()),
                            "tipo": self.getTipoSensor().getTipo()}
        #dic["tipo_sensor"]=self.getTipoSensor().toJson()
        dic["zona_sensor"]={"str": str(self.getZonaSensor()),
                            "tipo": self.getZonaSensor().getTipo()}
        #dic["zona_sensor"]=self.getZonaSensor().toJson()
        dic["numero_sensor"]=self.getNumeroSensor()
        dic["valor"]=self.getValor()
        dic["unidad_medida"]={"str": str(self.getUnidadMedida()),
                            "tipo": self.getUnidadMedida().getTipo()}
        #dic["unidad_medida"]=self.getUnidadMedida().toJson()
        dic["fecha"]=self.getFecha()#.isoformat()
        return dic

    def fromJson(dic: dict):
        sensor = RegistroSensor(dic["id_"],dic["tipo_sensor"]["tipo"],dic["zona_sensor"]["tipo"],
                                dic["numero_sensor"],dic["valor"],dic["unidad_medida"]["tipo"],
                                dic["fecha"])
        return sensor

from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import RegistroSensor
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class Sensor:

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                 modelo_sensor:ModeloSensor, direccion_lectura:str=None, patilla_1_lectura:int=None, 
                 patilla_2_lectura:int=None, patilla_3_lectura:int=None, patilla_4_lectura:int=None,
                 unidad_medida_1:UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_2:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                 unidad_medida_3:UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_4:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                 fecha_creacion:datetime=None ,fecha_eliminacion:datetime=None,):
        self.__tipo_sensor: TipoSensor = tipo_sensor
        self.__zona_sensor: ZonaSensor = zona_sensor
        self.__numero_sensor: int = numero_sensor
        self.__modelo_sensor: ModeloSensor = modelo_sensor
        self.__direccion_lectura: str = direccion_lectura
        self.__patilla_1_lectura: int = patilla_1_lectura
        self.__patilla_2_lectura: int = patilla_2_lectura
        self.__patilla_3_lectura: int = patilla_3_lectura
        self.__patilla_4_lectura: int = patilla_4_lectura
        self.__unidad_medida_1:UnidadMedida = unidad_medida_1
        self.__unidad_medida_2:UnidadMedida = unidad_medida_2
        self.__unidad_medida_3:UnidadMedida = unidad_medida_3
        self.__unidad_medida_4:UnidadMedida = unidad_medida_4
        self.__fecha_creacion: datetime = fecha_creacion
        self.__fecha_eliminacion: datetime = fecha_eliminacion

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

    def getModeloSensor(self) -> ModeloSensor:
        return self.__modelo_sensor
    
    def setModeloSensor(self, modelo_sensor:ModeloSensor):
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

    def getUnidadMedida1(self) -> UnidadMedida:
        return self.__unidad_medida_1
    
    def setUnidadMedida1(self, unidad_medida_1:UnidadMedida):
        self.__unidad_medida_1 = unidad_medida_1

    def getUnidadMedida2(self) -> UnidadMedida:
        return self.__unidad_medida_2
    
    def setUnidadMedida2(self, unidad_medida_2:UnidadMedida):
        self.__unidad_medida_2 = unidad_medida_2

    def getUnidadMedida3(self) -> UnidadMedida:
        return self.__unidad_medida_3
    
    def setUnidadMedida3(self, unidad_medida_3:UnidadMedida):
        self.__unidad_medida_3 = unidad_medida_3    

    def getUnidadMedida4(self) -> UnidadMedida:
        return self.__unidad_medida_4
    
    def setUnidadMedida4(self, unidad_medida_4:UnidadMedida):
        self.__unidad_medida_4 = unidad_medida_4

    def getFechaCreacion(self) -> Optional[datetime]:
        return self.__fecha_creacion
    
    def setFechaCreacion(self, fecha_creacion:datetime):
        self.__fecha_creacion = fecha_creacion

    def getFechaEliminacion(self) -> Optional[datetime]:
        return self.__fecha_eliminacion
    
    def setFechaEliminacion(self, fecha_eliminacion:datetime):
        self.__fecha_eliminacion = fecha_eliminacion

    def __eq__(self, other)  -> bool:
      return (other and self.getTipoSensor() == other.getTipoSensor() and self.getZonaSensor() == other.getZonaSensor() and
          self.getNumeroSensor() == other.getNumeroSensor() and self.getModeloSensor() == other.getModeloSensor() and
          self.getDireccionLectura() == other.getDireccionLectura() and self.getPatilla1Lectura() == other.getPatilla1Lectura() and
          self.getPatilla2Lectura() == other.getPatilla2Lectura() and self.getPatilla3Lectura() == other.getPatilla3Lectura() and
          self.getPatilla4Lectura() == other.getPatilla4Lectura() and self.getUnidadMedida1() == other.getUnidadMedida1() and
          self.getUnidadMedida2() == other.getUnidadMedida2() and self.getUnidadMedida3() == other.getUnidadMedida3() and
          self.getUnidadMedida4() == other.getUnidadMedida4())

    def __ne__(self, other) -> bool:
      return not self.__eq__(other)

    def __str__(self) -> str:
        texto: str = str("El sensor " +  str(self.getNumeroSensor()) + " de " + str(self.getTipoSensor()) + 
                          " de la zona " + str(self.getZonaSensor()) + " es del modelo " + str(self.getModeloSensor()) +
                          " y tiene configurados los siguientes parametros de comunicacion.\n" + 
                          "\tDireccion de lectura: " + str(self.getDireccionLectura()) + " .\n" +
                          "\tPatilla 1 de lectura: " + str(self.getPatilla1Lectura()) + " .\n" +
                          "\tPatilla 2 de lectura: " + str(self.getPatilla2Lectura()) + " .\n" +
                          "\tPatilla 3 de lectura: " + str(self.getPatilla3Lectura()) + " .\n" +
                          "\tPatilla 4 de lectura: " + str(self.getPatilla4Lectura()) + " .\n" +
                          "\tUnidad de medida 1: " + str(self.getUnidadMedida1()) + " .\n" +
                          "\tUnidad de medida 2: " + str(self.getUnidadMedida2()) + " .\n" +
                          "\tUnidad de medida 3: " + str(self.getUnidadMedida3()) + " .\n" +
                          "\tUnidad de medida 4: " + str(self.getUnidadMedida4()) + " .\n" +
                          "Fue creado en la fecha " + str(self.getFechaCreacion()))
        if self.getFechaEliminacion() is None:
            texto: str  = str(texto + " y sigue activo.")
        else:
            texto: str  = str(texto + " y fue eliminado en la fecha " + str(self.getFechaEliminacion()) + " .")
        return texto

    def getCode(self) -> int:
        return (int(self.getModeloSensor())*100000000+int(self.getTipoSensor())*1000000+int(self.getZonaSensor())*10000+self.getNumeroSensor())


    def toJson(self) -> dict:
        dic={}
        dic["tipo_sensor"]=self.getTipoSensor()
        dic["zona_sensor"]=self.getZonaSensor()
        dic["numero_sensor"]=self.getNumeroSensor()
        dic["modelo_sensor"]=self.getModeloSensor()
        dic["direccion_lectura"]=self.getDireccionLectura()
        dic["patilla_1_lectura"]=self.getPatilla1Lectura()
        dic["patilla_2_lectura"]=self.getPatilla2Lectura()
        dic["patilla_3_lectura"]=self.getPatilla3Lectura()
        dic["patilla_4_lectura"]=self.getPatilla4Lectura()
        dic["unidad_medida_1"]=self.getUnidadMedida1()
        dic["unidad_medida_2"]=self.getUnidadMedida2()
        dic["unidad_medida_3"]=self.getUnidadMedida3()
        dic["unidad_medida_4"]=self.getUnidadMedida4()
        dic["fecha_creacion"]=self.getFechaCreacion()
        dic["fecha_eliminacion"]=self.getFechaEliminacion()
        return dic
    
    def fromJson(dic: dict):
        sensor = Sensor(tipo_sensor=dic["tipo_sensor"],zona_sensor=dic["zona_sensor"],numero_sensor=dic["numero_sensor"],
                        modelo_sensor=dic["modelo_sensor"], direccion_lectura=dic["direccion_lectura"], 
                        patilla_1_lectura=dic["patilla_1_lectura"], patilla_2_lectura=dic["patilla_2_lectura"], 
                        patilla_3_lectura=dic["patilla_3_lectura"], patilla_4_lectura=dic["patilla_4_lectura"],
                        unidad_medida_1=dic["unidad_medida_1"], unidad_medida_2=dic["unidad_medida_2"],
                        unidad_medida_3=dic["unidad_medida_3"],unidad_medida_4=dic["unidad_medida_4"],
                        fecha_creacion=dic["fecha_creacion"], fecha_eliminacion=dic["fecha_eliminacion"])
        return sensor

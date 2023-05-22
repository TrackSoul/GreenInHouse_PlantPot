from datetime import datetime
from typing import Optional, Dict, List, Tuple
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from common.data.util import RegistroSensor as RegistroSensorCommon


class Sensor:

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, modelo_sensor:ModeloSensor,
                 nombre_sensor:str, direccion_lectura:str=None, patilla_0_lectura:int=None, 
                 patilla_1_lectura:int=None, patilla_2_lectura:int=None, patilla_3_lectura:int=None,
                 unidad_medida_0:UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_1:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                 unidad_medida_2:UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_3:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                 fecha_creacion:datetime=None ,fecha_eliminacion:datetime=None,):
        self.__tipo_sensor: TipoSensor = tipo_sensor
        self.__zona_sensor: ZonaSensor = zona_sensor
        self.__numero_sensor: int = numero_sensor
        self.__modelo_sensor: ModeloSensor = modelo_sensor
        self.__nombre_sensor: str = nombre_sensor
        self.__direccion_lectura: str = direccion_lectura
        self.__patillas_lectura: List[int] = [patilla_0_lectura, patilla_1_lectura, patilla_2_lectura, patilla_3_lectura]
        self.__unidades_medida: List[UnidadMedida] = [unidad_medida_0, unidad_medida_1, unidad_medida_2, unidad_medida_3]
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

    def getNombreSensor(self) -> str:
        return self.__nombre_sensor
    
    def setNombreSensor(self, nombre_sensor:str):
        self.__nombre_sensor = nombre_sensor

    def getDireccionLectura(self) -> Optional[str]:
        return self.__direccion_lectura
    
    def setDireccionLectura(self, direccion_lectura:str):
        self.__direccion_lectura = direccion_lectura

    def getPatillaLectura(self, val: int = 0) -> Optional[int]:
        if val < len(self.__patillas_lectura):
            return self.__patillas_lectura[val]
        else:
            return None
    
    def setPatillaLectura(self, patilla_lectura: int, val: int = 0):
        if val < len(self.__patillas_lectura):
            self.__patillas_lectura[val] = patilla_lectura

    def getUnidadMedida(self, val: int = 0) -> Optional[UnidadMedida]:
        if val < len(self.__unidades_medida):
            return self.__unidades_medida[val]
        else:
            return None
    
    def setUnidadMedida(self, unidad_medida: UnidadMedida, val: int = 0):
        if val < len(self.__unidades_medida):
            self.__unidades_medida[val] = unidad_medida

    def getFechaCreacion(self) -> Optional[datetime]:
        return self.__fecha_creacion
    
    def setFechaCreacion(self, fecha_creacion:datetime):
        self.__fecha_creacion = fecha_creacion

    def getFechaEliminacion(self) -> Optional[datetime]:
        return self.__fecha_eliminacion
    
    def setFechaEliminacion(self, fecha_eliminacion:datetime):
        self.__fecha_eliminacion = fecha_eliminacion

    def getCode(self) -> int:
        return (int(self.getModeloSensor())*100000000+int(self.getTipoSensor())*1000000+int(self.getZonaSensor())*10000+self.getNumeroSensor())

    def __eq__(self, other)  -> bool:
      return (other and self.getTipoSensor() == other.getTipoSensor() and self.getZonaSensor() == other.getZonaSensor() and
          self.getNumeroSensor() == other.getNumeroSensor() and self.getModeloSensor() == other.getModeloSensor() and 
          self.getNombreSensor() == other.getNombreSensor() and
          self.getDireccionLectura() == other.getDireccionLectura() and self.getPatillaLectura(0) == other.getPatillaLectura(0) and
          self.getPatillaLectura(1) == other.getPatillaLectura(1) and self.getPatillaLectura(2) == other.getPatillaLectura(2) and
          self.getPatillaLectura(3) == other.getPatillaLectura(3) and self.getUnidadMedida(0) == other.getUnidadMedida(0) and
          self.getUnidadMedida(1) == other.getUnidadMedida(1) and self.getUnidadMedida(2) == other.getUnidadMedida(2) and
          self.getUnidadMedida(3) == other.getUnidadMedida(3))

    def __ne__(self, other) -> bool:
      return not self.__eq__(other)

    def __str__(self) -> str:
        texto: str = str("El sensor con nombre " +  str(self.getNombreSensor()) + " es el sensor " +
                         str(self.getNumeroSensor()) + " de " + str(self.getTipoSensor()) + 
                         " de la zona " + str(self.getZonaSensor()) + ". Es del modelo " + str(self.getModeloSensor()) +
                         " y tiene configurados los siguientes parametros de comunicacion.\n" + 
                         "\tDireccion de lectura: " + str(self.getDireccionLectura()) + " .\n" +
                         "\tPatilla 0 de lectura: " + str(self.getPatillaLectura(0)) + " .\n" +
                         "\tPatilla 1 de lectura: " + str(self.getPatillaLectura(1)) + " .\n" +
                         "\tPatilla 2 de lectura: " + str(self.getPatillaLectura(2)) + " .\n" +
                         "\tPatilla 3 de lectura: " + str(self.getPatillaLectura(3)) + " .\n" +
                         "\tUnidad de medida 0: " + str(self.getUnidadMedida(0)) + " .\n" +
                         "\tUnidad de medida 1: " + str(self.getUnidadMedida(1)) + " .\n" +
                         "\tUnidad de medida 2: " + str(self.getUnidadMedida(2)) + " .\n" +
                         "\tUnidad de medida 3: " + str(self.getUnidadMedida(3)) + " .\n" +
                         "Fue creado en la fecha " + str(self.getFechaCreacion()))
        if self.getFechaEliminacion() is None:
            texto: str  = str(texto + " y sigue activo.")
        else:
            texto: str  = str(texto + " y fue eliminado en la fecha " + str(self.getFechaEliminacion()) + " .")
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
        dic["modelo_sensor"]={"nombre": str(self.getModeloSensor()),
                            "tipo": self.getModeloSensor().getTipo()}
        #dic["modelo_sensor"]=self.getModeloSensor().toJson()
        dic["nombre_sensor"]=self.getNombreSensor()
        dic["direccion_lectura"]=self.getDireccionLectura()
        dic["patilla_0_lectura"]=self.getPatillaLectura(0)
        dic["patilla_1_lectura"]=self.getPatillaLectura(1) if self.getPatillaLectura(1) is not None else None
        dic["patilla_2_lectura"]=self.getPatillaLectura(2) if self.getPatillaLectura(2) is not None else None
        dic["patilla_3_lectura"]=self.getPatillaLectura(3) if self.getPatillaLectura(3) is not None else None
        dic["unidad_medida_0"]={"nombre": str(self.getUnidadMedida(0)),
                            "tipo": self.getUnidadMedida(0).getTipo()}
        #dic["unidad_medida_0"]=self.getUnidadMedida(0).toJson()
        dic["unidad_medida_1"]={"nombre": str(self.getUnidadMedida(1)),
                            "tipo": self.getUnidadMedida(1).getTipo()} if self.getUnidadMedida(1) is not None else None
        #dic["unidad_medida_1"]=self.getUnidadMedida(1).toJson()
        dic["unidad_medida_2"]={"nombre": str(self.getUnidadMedida(2)),
                            "tipo": self.getUnidadMedida(2).getTipo()} if self.getUnidadMedida(2) is not None else None
        #dic["unidad_medida_2"]=self.getUnidadMedida(2).toJson()
        dic["unidad_medida_3"]={"nombre": str(self.getUnidadMedida(3)),
                            "tipo": self.getUnidadMedida(3).getTipo()} if self.getUnidadMedida(3) is not None else None
        #dic["unidad_medida_3"]=self.getUnidadMedida(3).toJson()
        dic["fecha_creacion"]=str(self.getFechaCreacion())  if self.getFechaCreacion() is not None else None
        dic["fecha_eliminacion"]=str(self.getFechaEliminacion()) if self.getFechaEliminacion() is not None else None
        return dic
    
    @staticmethod
    def fromJson(dic: dict):
        #hacer conversion de tipos
        sensor = Sensor(tipo_sensor=dic.get("tipo_sensor"),
                        zona_sensor=dic.get("zona_sensor"),
                        numero_sensor=dic.get("numero_sensor"),
                        modelo_sensor=dic.get("modelo_sensor"), 
                        nombre_sensor=dic.get("nombre_sensor"), 
                        direccion_lectura=dic.get("direccion_lectura"), 
                        patilla_0_lectura=dic.get("patilla_0_lectura"), 
                        patilla_1_lectura=dic.get("patilla_1_lectura") if dic.get("patilla_1_lectura") is not None else None, 
                        patilla_2_lectura=dic.get("patilla_2_lectura") if dic.get("patilla_2_lectura") is not None else None, 
                        patilla_3_lectura=dic.get("patilla_3_lectura") if dic.get("patilla_3_lectura") is not None else None,
                        unidad_medida_0=dic.get("unidad_medida_0"), 
                        unidad_medida_1=dic.get("unidad_medida_1") if dic.get("unidad_medida_1") is not None else None,
                        unidad_medida_2=dic.get("unidad_medida_2") if dic.get("unidad_medida_2") is not None else None, 
                        unidad_medida_3=dic.get("unidad_medida_3") if dic.get("unidad_medida_3") is not None else None,
                        fecha_creacion=datetime.fromisoformat(dic.get("fecha_creacion")),
                        fecha_eliminacion=datetime.fromisoformat(dic.get("fecha_eliminacion")) if dic.get("fecha_eliminacion") is not None else None)
        return sensor
    

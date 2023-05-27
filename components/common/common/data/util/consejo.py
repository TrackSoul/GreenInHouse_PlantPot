from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida

class Consejo:

    def __init__(self, descripcion: str, nombre_elemento: str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, 
                 valor_minimo:float, valor_maximo:float, 
                 horas_minimas:float, horas_maximas:float):
        self.__descripcion: str = descripcion
        self.__nombre_elemento: str = nombre_elemento
        self.__zona_consejo: ZonaSensor = zona_consejo
        self.__tipo_medida: TipoMedida = tipo_medida       
        self.__unidad_medida: UnidadMedida = unidad_medida
        self.__valor_minimo: float = valor_minimo
        self.__valor_maximo: float  = valor_maximo
        self.__horas_minimas: float = horas_minimas
        self.__horas_maximas: float  = horas_maximas

    def getDescripcion(self) -> str:
        return self.__descripcion
    
    def setDescripcion(self, descripcion: str):
        self.__descripcion = descripcion

    def getZonaConsejo(self) -> ZonaSensor:
        return self.__zona_consejo

    def setZonaConsejo(self, zona_consejo:ZonaSensor):
        self.__zona_consejo = zona_consejo

    def getTipoMedida(self) -> TipoMedida:
        return self.__tipo_medida

    def setTipoMedida(self, tipo_medida:TipoMedida):
        self.__tipo_medida = tipo_medida
      
    def getUnidadMedida(self) -> UnidadMedida:
        return self.__unidad_medida
    
    def setUnidadMedida(self, unidad_medida:UnidadMedida):
        self.__unidad_medida = unidad_medida

    def getValorMinimo(self) -> float:
        return self.__valor_minimo

    def setValorMinimo(self, valor_minimo:float):
        self.__valor_minimo = valor_minimo
    
    def getValorMaximo(self) -> float:
        return self.__valor_maximo
    
    def setValorMaximo(self, valor_maximo:float):
        self.__valor_maximo = valor_maximo

    def getHorasMinimas(self) -> Optional[float]:
        return self.__horas_minimas

    def setHorasMinimas(self, horas_minimas:float):
        self.__horas_minimas = horas_minimas
    
    def getHorasMaximas(self) -> Optional[float]:
        return self.__horas_maximas
    
    def setHorasMaximas(self, horas_maximas:float):
        self.__horas_maximas = horas_maximas
    
    def getNombreElemento(self) -> str:
        return self.__nombre_elemento
    
    def setNombreElemento(self, nombre_elemento:str):
        self.__nombre_elemento = nombre_elemento
    
    def __str__(self) -> str:
        texto: str = str("El consejo del elemento " + str(self.getNombreElemento) + " de la zona " + str(self.getZonaConsejo()) + " del tipo de medida " +  str(self.getTipoMedida()) + 
                         " tiene la unidad de medida " +  str(self.getUnidadMedida()) + " con el valor minimo en " + str(self.getValorMinimo()) + 
                         " y el valor maximo en " + str(self.getValorMaximo()) +  " y la descripcion " + str(self.getDescripcion()) + " .")
        return texto

    def toJson(self) -> Dict:
        dic:Dict={}
        dic["descripcion"]=self.getDescripcion()
        dic["nombre_elemento"]=self.getNombreElemento()
        dic["zona_consejo"]={"nombre": str(self.getZonaConsejo()),
                            "tipo": self.getZonaConsejo().getTipo()}
        dic["tipo_medida"]={"nombre": str(self.getTipoMedida()),
                            "tipo": self.getTipoMedida().getTipo()}
        dic["unidad_medida"]={"nombre": str(self.getUnidadMedida()),
                            "tipo": self.getUnidadMedida().getTipo()}
        dic["valor_minimo"]=str(self.getValorMinimo())
        dic["valor_maximo"]=str(self.getValorMaximo())
        dic["horas_minimas"]=str(self.getHorasMinimas())
        dic["horas_maximas"]=str(self.getHorasMaximas())
        return dic

    @staticmethod
    def fromJson(dic: Dict):
        consejo = Consejo(descripcion=dic.get("descripcion"),
                          nombre_elemento=dic.get("nombre_elemento"),
                          zona_consejo=dic.get("zona_consejo").get("tipo"),
                          tipo_medida=dic.get("tipo_medida").get("tipo"),
                          unidad_medida=dic.get("unidad_medida").get("tipo"),
                          valor_minimo=dic.get("valor_minimo"),
                          valor_maximo=dic.get("valor_maximo"),
                          horas_minimas=dic.get("horas_minimas"),
                          horas_maximas=dic.get("horas_maximas"))
        return consejo

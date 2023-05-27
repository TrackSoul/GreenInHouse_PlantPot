from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida

class ConsejoPlanta:

    def __init__(self, descripcion: str, nombre_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float):
        self.__descripcion: str = descripcion
        self.__nombre_planta: str = nombre_planta
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
    
    def getNombrePlanta(self) -> str:
        return self.__nombre_planta
    
    def setNombrePlanta(self, nombre_planta:str):
        self.__nombre_planta = nombre_planta

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
    
    def __str__(self) -> str:
        texto: str = str("El consejo del tipo de planta " + str(self.getNombrePlanta()) + " de la zona " + str(self.getZonaConsejo()) +
                         " del tipo de medida " +  str(self.getTipoMedida()) + " tiene la unidad de medida " +  str(self.getUnidadMedida()) + 
                          " con el valor minimo en " + str(self.getValorMinimo()) + " y el valor maximo en " + str(self.getValorMaximo()) + 
                          " y la descripcion " + str(self.getDescripcion()) + " .")
        return texto

    def toJson(self) -> Dict:
        dic:Dict={}
        dic["descripcion"]=self.getDescripcion()
        dic["nombre_planta"]=self.getNombrePlanta()
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
        consejo = ConsejoPlanta(descripcion=dic.get("descripcion"),
                                nombre_planta=dic.get("nombre_planta"),
                                zona_consejo=dic.get("zona_consejo").get("tipo"),
                                tipo_medida=dic.get("tipo_medida").get("tipo"),
                                unidad_medida=dic.get("unidad_medida").get("tipo"),
                                valor_minimo=dic.get("valor_minimo"),
                                valor_maximo=dic.get("valor_maximo"),
                                horas_minimas=dic.get("horas_minimas"),
                                horas_maximas=dic.get("horas_maximas"))
        return consejo

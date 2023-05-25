from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida

class ConsejoTipoPlanta:

    def __init__(self, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float):
        self.__descripcion: str = descripcion
        self.__tipo_planta: str = tipo_planta
        self.__zona_consejo: ZonaSensor = zona_consejo
        self.__tipo_medida: TipoMedida = tipo_medida       
        self.__unidad_medida: UnidadMedida = unidad_medida
        self.__valor_minimo: float = valor_minimo
        self.__valor_maximo: float  = valor_maximo
        self.__horas_minimas: float = horas_minimas
        self.__horas_maximas: float  = horas_maximas

    def getDescripcion(self) -> str:
        return self.__descripcion
    
    def getTipoPlanta(self) -> str:
        return self.__tipo_planta

    def getZonaConsejo(self) -> ZonaSensor:
        return self.__zona_consejo

    def getTipoMedida(self) -> TipoMedida:
        return self.__tipo_medida
      
    def getUnidadMedida(self) -> UnidadMedida:
        return self.__unidad_medida

    def getValorMinimo(self) -> float:
        return self.__valor_minimo
    
    def getValorMaximo(self) -> float:
        return self.__valor_maximo

    def getHorasMinimas(self) -> Optional[float]:
        return self.__horas_minimas
    
    def getHorasMaximas(self) -> Optional[float]:
        return self.__horas_maximas
    
    def __str__(self) -> str:
        texto: str = str("El consejo del tipo de planta " + str(self.getTipoPlanta()) + " de la zona " + str(self.getZonaConsejo()) +
                         " del tipo de medida " +  str(self.getTipoMedida()) + " tiene la unidad de medida " +  str(self.getUnidadMedida()) + 
                          " con el valor minimo en " + str(self.getValorMinimo()) + " y el valor maximo en " + str(self.getValorMaximo()) + 
                          " y la descripcion " + str(self.getDescripcion()) + " .")
        return texto

    def toJson(self) -> Dict:
        dic:Dict={}
        dic["descripcion"]=self.getDescripcion()
        dic["tipo_planta"]=self.getTipoPlanta()
        dic["zona_consejo"]={"nombre": str(self.getZonaConsejo()),
                            "tipo": self.getZonaConsejo().getTipo()}
        #dic["zona_consejo"]=self.getZonaConsejo().toJson()
        dic["tipo_medida"]={"nombre": str(self.getTipoMedida()),
                            "tipo": self.getTipoMedida().getTipo()}
        #dic["tipo_medida"]=self.getTipoMedida().toJson()
        dic["unidad_medida"]={"nombre": str(self.getUnidadMedida()),
                            "tipo": self.getUnidadMedida().getTipo()}
        #dic["unidad_medida"]=self.getUnidadMedida().toJson()
        dic["valor_minimo"]=str(self.getValorMinimo())
        dic["valor_maximo"]=str(self.getValorMaximo())
        dic["horas_minimas"]=str(self.getHorasMinimas())
        dic["horas_maximas"]=str(self.getHorasMaximas())
        return dic

    @staticmethod
    def fromJson(dic: Dict):
        consejo = ConsejoTipoPlanta(descripcion=dic.get("descripcion"),
                                    tipo_planta=dic.get("tipo_planta"),
                                    zona_consejo=dic.get("zona_consejo").get("tipo"),
                                    tipo_medida=dic.get("tipo_medida").get("tipo"),
                                    unidad_medida=dic.get("unidad_medida").get("tipo"),
                                    valor_minimo=dic.get("valor_minimo"),
                                    valor_maximo=dic.get("valor_maximo"),
                                    horas_minimas=dic.get("horas_minimas"),
                                    horas_maximas=dic.get("horas_maximas"))
        return consejo

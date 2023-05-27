from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida, Consejo

class ConsejoTipoPlanta(Consejo):

    def __init__(self, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float):
        super().__init__(descripcion, zona_consejo, tipo_medida, unidad_medida,
                         valor_minimo, valor_maximo, horas_minimas, horas_maximas)
        self.__tipo_planta: str = tipo_planta
    
    def getTipoPlanta(self) -> str:
        return self.__tipo_planta
    
    def setTipoPlanta(self, tipo_planta:str):
        self.__tipo_planta = tipo_planta
    
    def __str__(self) -> str:
        texto: str = str("El consejo del tipo de planta " + str(self.getTipoPlanta()) + " de la zona " + str(self.getZonaConsejo()) +
                         " del tipo de medida " +  str(self.getTipoMedida()) + " tiene la unidad de medida " +  str(self.getUnidadMedida()) + 
                          " con el valor minimo en " + str(self.getValorMinimo()) + " y el valor maximo en " + str(self.getValorMaximo()) + 
                          " y la descripcion " + str(self.getDescripcion()) + " .")
        return texto

    def toJson(self) -> Dict:
        dic:Dict = super().toJson()
        dic["tipo_planta"]=self.getTipoPlanta()
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

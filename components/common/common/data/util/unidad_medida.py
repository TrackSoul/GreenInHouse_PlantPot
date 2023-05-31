""" 
Enumeracion con las unidades de medida de los sensores
"""

from typing import List
from enum import Enum
from common.data.util.tipo_medida import TipoMedida

class UnidadMedida(Enum):

    SIN_UNIDAD = 0, "Sin unidad", "SIN_UNIDAD", [TipoMedida.SIN_TIPO]
    PORCENTAJE = 1, "%", "PORCENTAJE", [TipoMedida.HUMEDAD]
    GRADOS_CENTIGRADOS = 2, "ºC", "GRADOS_CENTIGRADOS", [TipoMedida.TEMPERATURA]
    # GRADOS_FARENHEIT = 3, "ºF", "GRADOS_FARENHEIT", [TipoMedida.TEMPERATURA]   
    LUMENES = 4, "Lux", "LUMENES", [TipoMedida.LUMINOSIDAD]
    OTRO = 99, "Otro", "OTRO", [TipoMedida.OTRO]        

    def __new__(cls, value, nombre, tipo,
                tipos_medida: List[TipoMedida]):
        member = object.__new__(cls)
        member.__value: int = value
        member.__nombre: str = nombre
        member.__tipo: str = tipo
        member.__tipos_medida: List[TipoMedida] = tipos_medida
        return member

    def __int__(self):
        return self.__value

    def __str__(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo

    def getTiposMedida(self) -> List[TipoMedida]:
        return self.__tipos_medida

    def getTipoMedida(self, val:int=0) -> TipoMedida:
        if val < len(self.__tipos_medida):
            return self.__tipos_medida[val]
        else:
            return TipoMedida.SIN_TIPO
            # return None
    
    def toJson(self) -> dict:
        dic={}
        dic["value"]=int(self)
        dic["nombre"]=str(self)
        dic["tipo"]=self.getTipo()
        dic["tipos_medida"]=[tipo_medida.toJson() for tipo_medida in self.getTiposMedida()]
        return dict

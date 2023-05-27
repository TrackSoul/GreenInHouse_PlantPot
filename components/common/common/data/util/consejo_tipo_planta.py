from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida, Consejo

class ConsejoTipoPlanta(Consejo):
    
    def getTipoPlanta(self) -> str:
        return self.getNombreElemento()
    
    def setTipoPlanta(self, tipo_planta:str):
        self.setNombreElemento(tipo_planta)
    
    def __str__(self) -> str:
        texto: str = str("El consejo del tipo de planta " + str(self.getTipoPlanta()) + " de la zona " + str(self.getZonaConsejo()) +
                         " del tipo de medida " +  str(self.getTipoMedida()) + " tiene la unidad de medida " +  str(self.getUnidadMedida()) + 
                          " con el valor minimo en " + str(self.getValorMinimo()) + " y el valor maximo en " + str(self.getValorMaximo()) + 
                          " y la descripcion " + str(self.getDescripcion()) + " .")
        return texto


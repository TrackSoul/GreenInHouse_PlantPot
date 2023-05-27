from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida, Consejo

class ConsejoPlanta(Consejo):
    
    def getPlanta(self) -> str:
        return self.getNombreElemento()
    
    def setPlanta(self, planta:str):
        self.setNombreElemento(planta)
    
    def __str__(self) -> str:
        texto: str = str("El consejo de la planta " + str(self.getPlanta()) + " de la zona " + str(self.getZonaConsejo()) +
                         " del tipo de medida " +  str(self.getTipoMedida()) + " tiene la unidad de medida " +  str(self.getUnidadMedida()) + 
                          " con el valor minimo en " + str(self.getValorMinimo()) + " y el valor maximo en " + str(self.getValorMaximo()) + 
                          " y la descripcion " + str(self.getDescripcion()) + " .")
        return texto

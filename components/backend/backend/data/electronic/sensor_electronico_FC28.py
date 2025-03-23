#Author: Oscar Valverde Escobar

from typing import List, Tuple
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico, SensorElectronicoMCP3008
from common.data.util import Sensor as SensorCommon

class SensorElectronicoFC28 (SensorElectronicoMCP3008):

    def __init__(self, sensor_common: SensorCommon):
        super().__init__(sensor_common)


    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = super().leer_sensor()
        valor = lista_valor_unidad_medida[0][0]
        if (valor is not None):
            lista_valor_unidad_medida[0][0]=100.0-(valor*100.0/65535)
        else:
             lista_valor_unidad_medida[0][0]=-999
        return lista_valor_unidad_medida



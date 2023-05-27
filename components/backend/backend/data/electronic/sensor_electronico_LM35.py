from datetime import datetime
from typing import Optional,Dict,List, Tuple
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico, SensorElectronicoMCP3008
from common.data.util import Sensor as SensorCommon

class SensorElectronicoLM35 (SensorElectronicoMCP3008):

    def __init__(self, sensor_common: SensorCommon):
        super().__init__(sensor_common)
        # self.direccion_lectura:str = sensor_common.getDireccionLectura()
        # self.patilla_0_lectura:int = sensor_common.getPatillaLectura(0)
        # self.unidad_medida_0:UnidadMedida = sensor_common.getUnidadMedida(0)


    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = super().leer_sensor()
        valor = lista_valor_unidad_medida[0][0]
        if (valor is not None):
            lista_valor_unidad_medida[0][0]=(valor/10.0)
        return lista_valor_unidad_medida
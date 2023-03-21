from datetime import datetime
from typing import Optional,Dict,List, Tuple
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from common.data.util import Sensor as SensorCommon

class SensorElectronico ():

    def __init__(self, sensor_common: SensorCommon):
        self.direccion_lectura:str = sensor_common.getDireccionLectura()
        self.patilla_0_lectura:int = sensor_common.getPatillaLectura(0)
        self.patilla_1_lectura:int = sensor_common.getPatillaLectura(1)
        self.patilla_2_lectura:int = sensor_common.getPatillaLectura(2)
        self.patilla_3_lectura:int = sensor_common.getPatillaLectura(3)
        self.unidad_medida_0:UnidadMedida = sensor_common.getUnidadMedida(0)
        self.unidad_medida_1:UnidadMedida = sensor_common.getUnidadMedida(1)
        self.unidad_medida_2:UnidadMedida = sensor_common.getUnidadMedida(2)
        self.unidad_medida_3:UnidadMedida = sensor_common.getUnidadMedida(3)

    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = [[0.0,UnidadMedida.OTRO]]
        return lista_valor_unidad_medida
from datetime import datetime
from typing import Optional,Dict,List, Tuple
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico
from common.data.util import Sensor as SensorCommon

class SensorElectronicoDHT11 (SensorElectronico):

    def __init__(self, sensor_common: SensorCommon):
        self.direccion_lectura:str = sensor_common.getDireccionLectura()
        self.patilla_0_lectura:int = sensor_common.getPatillaLectura(0)


    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = [[10.0,UnidadMedida.GRADOS_CENTIGRADOS],[20.0,UnidadMedida.PORCENTAJE]]
        return lista_valor_unidad_medida
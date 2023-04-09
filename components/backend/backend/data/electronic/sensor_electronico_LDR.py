from typing import List, Tuple
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico, SensorElectronicoMCP3008
from common.data.util import Sensor as SensorCommon

class SensorElectronicoLDR (SensorElectronicoMCP3008):

    def __init__(self, sensor_common: SensorCommon, R_o = 10, R_l = 1, R_c = 10):
        super().__init__(sensor_common)
        self.R_o = R_o     #Resistencia en oscuridad en KΩ
        self.R_l = R_l     #Resistencia a la luz (10 Lux) en KΩ
        self.R_c = R_c     #Resistencia calibracion en KΩ


    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = super().leer_sensor()
        valor = lista_valor_unidad_medida[0][0]
        if (valor is not None):
            lista_valor_unidad_medida[0][0]= (valor*self.R_o*10)/(self.R_l*self.R_c*(65535-valor))
        return lista_valor_unidad_medida
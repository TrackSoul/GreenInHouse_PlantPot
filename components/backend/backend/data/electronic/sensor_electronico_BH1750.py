#Author: Oscar Valverde Escobar

from typing import List, Tuple
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico
from common.data.util import Sensor as SensorCommon
import busio
import digitalio
import board
from board import pin
import adafruit_bh1750 as BH1750
import time

class SensorElectronicoBH1750 (SensorElectronico):

    def __init__(self, sensor_common: SensorCommon):
        super().__init__(sensor_common)
        # i2c = board.I2C()
        # self.sensor = BH1750.BH1750(i2c,int(sensor_common.patilla_0_lectura))


    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        i2c = board.I2C()
        # self.sensor = BH1750.BH1750(i2c,self.patilla_0_lectura)
        valor_leido=None
        intentos_lectura = 0
        while (valor_leido is None and intentos_lectura < 10):
            try:
                valor_leido = BH1750.BH1750(i2c,self.patilla_0_lectura).lux
            except OSError:
                valor_leido=None
                time.sleep(1)
            intentos_lectura += 1
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = [[valor_leido, self.unidad_medida_0]]
        return lista_valor_unidad_medida



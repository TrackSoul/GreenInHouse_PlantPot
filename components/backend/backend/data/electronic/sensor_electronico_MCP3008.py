#Author: Oscar Valverde Escobar

from typing import List, Tuple
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico
from common.data.util import Sensor as SensorCommon
import busio
import digitalio
import board
from board import pin
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class SensorElectronicoMCP3008 (SensorElectronico):

    def __init__(self, sensor_common: SensorCommon):
        super().__init__(sensor_common)
        if ( 'MCP3008_0' == self.direccion_lectura ):
            self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        elif ('MCP3008_1' == self.direccion_lectura ):
            self.spi = busio.SPI(clock=board.SCK_1, MISO=board.MISO_1, MOSI=board.MOSI_1)
        self.cs = digitalio.DigitalInOut(pin.Pin(self.patilla_0_lectura))
        self.mcp = MCP.MCP3008(self.spi, self.cs)
        self.canal = AnalogIn(self.mcp, self.patilla_1_lectura)


    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        valor_leido=None
        intentos_lectura = 0
        while (valor_leido is None and intentos_lectura < 10):
            valor_leido = self.canal.value
            intentos_lectura += 1
        if (valor_leido is None):
            valor_leido = -999
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = [[valor_leido, self.unidad_medida_0]]
        return lista_valor_unidad_medida



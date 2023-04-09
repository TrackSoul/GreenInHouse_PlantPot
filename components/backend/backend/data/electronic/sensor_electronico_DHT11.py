from datetime import datetime
import time
from typing import Optional,Dict,List, Tuple
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico
from common.data.util import Sensor as SensorCommon
import board
from board import pin
import adafruit_dht

class SensorElectronicoDHT11 (SensorElectronico):

    def __init__(self, sensor_common: SensorCommon):
        self.direccion_lectura:str = sensor_common.getDireccionLectura()
        self.patilla_0_lectura:int = sensor_common.getPatillaLectura(0)
        self.unidad_medida_0:UnidadMedida = sensor_common.getUnidadMedida(0)
        self.unidad_medida_1:UnidadMedida = sensor_common.getUnidadMedida(1)
        self.dhtDevice = adafruit_dht.DHT11(pin.Pin(self.patilla_0_lectura), use_pulseio=False)
        self.dhtDevice._trig_wait = 1500

    def leer_sensor(self) -> List[Tuple[float, UnidadMedida]]:
        temperatura_c = None
        intentos_lectura = 0
        while (temperatura_c is None and intentos_lectura < 10):
            try:
                temperatura_c = self.dhtDevice.temperature
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                time.sleep(2.0)
                continue
            finally:
                intentos_lectura += 1
        registro_temperatura = None
        if (temperatura_c is None):
            temperatura_c = -100
        if (self.unidad_medida_0.getTipoMedida()==TipoMedida.TEMPERATURA):
            registro_temperatura: Tuple[float, UnidadMedida] = [temperatura_c, self.unidad_medida_0]
        else:
            registro_temperatura: Tuple[float, UnidadMedida] = [temperatura_c, self.unidad_medida_1]

        humedad = None
        intentos_lectura = 0
        while (humedad is None and intentos_lectura < 10):
            try:
                humedad = self.dhtDevice.humidity
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                time.sleep(2.0)
                continue
            finally:
                intentos_lectura += 1
        if (humedad is None):
            humedad = -100
        registro_humedad = None
        if (self.unidad_medida_0.getTipoMedida()==TipoMedida.HUMEDAD):
            registro_humedad: Tuple[float, UnidadMedida] = [humedad, self.unidad_medida_0]
        else:
            registro_humedad: Tuple[float, UnidadMedida] = [humedad, self.unidad_medida_1]

        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = [registro_temperatura,registro_humedad]
        return lista_valor_unidad_medida
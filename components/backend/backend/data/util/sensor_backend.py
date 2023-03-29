from datetime import datetime
from typing import Optional,Dict,List,Tuple
from enum import Enum
from common.data.util import Sensor as SensorCommon, RegistroSensor as RegistroSensorCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida
from backend.data.electronic import SensorElectronico
from backend.data.util import FactoriaSensor

class SensorBackend():

    def __init__(self, sensor_common: SensorCommon):
        self.sensor_common: SensorCommon = sensor_common
        self.sensor_electronico: SensorElectronico = FactoriaSensor.getSensorElectronico(sensor_common)

    def createRecordSensor(self, valor: float, unidad_medida: UnidadMedida) -> RegistroSensorCommon:
        return RegistroSensorCommon(self.sensor_common.getTipoSensor(),self.sensor_common.getZonaSensor(),
                                    self.sensor_common.getNumeroSensor(),valor,unidad_medida)

    def createRecordsSensor(self, lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]]) -> List[RegistroSensorCommon]:
        lista_registros_sensor  = []
        for registro_sensor in lista_valor_unidad_medida:
            lista_registros_sensor.append(self.createRecordSensor(registro_sensor[0],registro_sensor[1]))
        return lista_registros_sensor

    def readSensorAndCreateRecords(self) -> List[RegistroSensorCommon]:
        lista_registros_sensor  = []
        registro = self.sensor_electronico.leer_sensor()
        lista_registros_sensor = self.createRecordsSensor(registro)
        return lista_registros_sensor

from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session
from backend.data.db.esquema import Esquema
from backend.data.db.results import Sensor, Planta, RegistroSensor, TipoPlanta, SensorPlanta
from backend.data.db.resultsets import SensorSet,PlantaSet, RegistroSensorSet, TipoPlantaSet, SensorPlantaSet
from backend.service import SensorService, PlantaService, RegistroSensorService, TipoPlantaService, SensorPlantaService
from common.data.util import Sensor as SensorCommon, RegistroSensor as RegistroSensorCommon, Planta as PlantaCommon
from common.data.util import TipoPlanta as TipoPlantaCommon, SensorPlanta as SensorPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class GeneralService():

    @staticmethod
    def readRegistrosPlanta(esquema: Esquema, nombre_planta: str) -> List[RegistroSensorCommon]:
        planta: PlantaCommon = PlantaService.get(esquema,nombre_planta)
        lista_registros_sensores_planta: List[RegistroSensorCommon] = []
        sensores_planta_asociados: List[SensorPlantaCommon] =  SensorPlantaService.listAllSensorsPerPlantFromCommon(esquema,planta)
        for sensor_planta_asociado in sensores_planta_asociados:
            sensor: SensorCommon = SensorService.getSensorFromRelationFromCommon(esquema, sensor_planta_asociado)
            fecha_i = sensor_planta_asociado.getFechaAsociacion()
            fecha_f = sensor_planta_asociado.getFechaAnulacion()
            if (fecha_f is None):
                fecha_f = datetime.now()
            registros_sensor_planta = RegistroSensorService.listAllFromSensorFromCommonBetweenDates(esquema,sensor,fecha_i, fecha_f)
            for registro_sensor_planta in registros_sensor_planta:
                lista_registros_sensores_planta.append(registro_sensor_planta)

        return lista_registros_sensores_planta
    
    @staticmethod
    def readRegistrosPlantaFromCommon(esquema: Esquema, planta: PlantaCommon) -> List[RegistroSensorCommon]:
        return GeneralService.readRegistrosPlanta(esquema, planta.getNombrePlanta())
    

    @staticmethod
    def readRegistrosPlantaBetweenDates(esquema: Esquema, nombre_planta: str, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        planta: PlantaCommon = PlantaService.get(esquema,nombre_planta)
        lista_registros_sensores_planta: List[RegistroSensorCommon] = []
        sensores_planta_asociados: List[SensorPlantaCommon] =  SensorPlantaService.listAllSensorsPerPlantFromCommon(esquema,planta)
        for sensor_planta_asociado in sensores_planta_asociados:
            sensor: SensorCommon = SensorService.getSensorFromRelationFromCommon(esquema, sensor_planta_asociado)
            if (fecha_fin is None):
                fecha_fin = datetime.now()
            fecha_i = fecha_inicio
            fecha_f = fecha_fin
            if fecha_inicio < sensor_planta_asociado.getFechaAsociacion():
                fecha_i = sensor_planta_asociado.getFechaAsociacion()
            if sensor_planta_asociado.getFechaAnulacion() is not None:
                if fecha_fin > sensor_planta_asociado.getFechaAnulacion():
                    fecha_f = sensor_planta_asociado.getFechaAnulacion()
            registros_sensor_planta = RegistroSensorService.listAllFromSensorFromCommonBetweenDates(esquema,sensor,fecha_i, fecha_f)
            for registro_sensor_planta in registros_sensor_planta:
                lista_registros_sensores_planta.append(registro_sensor_planta)
        return lista_registros_sensores_planta
    
    @staticmethod
    def readRegistrosPlantaFromCommonBetweenDates(esquema: Esquema, planta: PlantaCommon, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        return GeneralService.readRegistrosPlantaBetweenDates(esquema, planta.getNombrePlanta(), fecha_inicio, fecha_fin)

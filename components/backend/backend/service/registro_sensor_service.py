#Author: Oscar Valverde Escobar

from datetime import datetime
from typing import List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroSensor
from backend.data.db.resultsets import RegistroSensorSet
from common.data.util import RegistroSensor as RegistroSensorCommon, Sensor as SensorCommon
from common.data.util import Planta as PlantaCommon, SensorPlanta as SensorPlantaCommon
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida
from backend.service import SensorService, PlantaService, SensorPlantaService

class RegistroSensorService():

    @staticmethod
    def create(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, 
                        numero_sensor:int, valor:float, unidad_medida: UnidadMedida, fecha:datetime = datetime.now()) -> RegistroSensorCommon:
        session: Session = esquema.new_session()
        out: RegistroSensorCommon = None
        try:
            new_registro_sensor: RegistroSensor = RegistroSensorSet.create(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, valor, unidad_medida, fecha)
            out= RegistroSensorCommon(new_registro_sensor.tipo_sensor,new_registro_sensor.zona_sensor,
                                      new_registro_sensor.numero_sensor,new_registro_sensor.valor, 
                                      new_registro_sensor.unidad_medida, new_registro_sensor.fecha, 
                                      new_registro_sensor.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, registro_sensor: RegistroSensorCommon) -> RegistroSensorCommon:
        return RegistroSensorService.create(esquema, registro_sensor.getTipoSensor(), registro_sensor.getZonaSensor(), 
                                            registro_sensor.getNumeroSensor(), registro_sensor.getValor(), 
                                            registro_sensor.getUnidadMedida())

    @staticmethod
    def exists(esquema: Esquema, id_:int) -> bool:
        session: Session = esquema.new_session()
        registro_sensor_exists: bool = RegistroSensorSet.get(session, id_)
        esquema.remove_session()
        return registro_sensor_exists

    @staticmethod
    def listToJson(esquema: Esquema, registros_sensor: List[RegistroSensorCommon]) -> List[Dict]:
        out: List[Dict] = []
        for registro_sensor in registros_sensor:
            out.append(registro_sensor.toJson())
        return out
    
    @staticmethod
    def listAll(esquema: Esquema) -> List[RegistroSensorCommon]:
        out: List[RegistroSensorCommon] = []
        session: Session = esquema.new_session()
        registros_sensor: List[RegistroSensor] = RegistroSensorSet.listAll(session)
        for registro_sensor in registros_sensor:
            out.append(RegistroSensorCommon(registro_sensor.tipo_sensor,registro_sensor.zona_sensor,
                                      registro_sensor.numero_sensor,registro_sensor.valor, 
                                      registro_sensor.unidad_medida, registro_sensor.fecha, 
                                      registro_sensor.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromSensor(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> List[RegistroSensorCommon]:
        out: List[RegistroSensorCommon] = []
        session: Session = esquema.new_session()
        registros_sensor: List[RegistroSensor] = RegistroSensorSet.listAllFromSensor(session, tipo_sensor, zona_sensor, numero_sensor)
        for registro_sensor in registros_sensor:
            out.append(RegistroSensorCommon(registro_sensor.tipo_sensor,registro_sensor.zona_sensor,
                                      registro_sensor.numero_sensor,registro_sensor.valor, 
                                      registro_sensor.unidad_medida, registro_sensor.fecha, 
                                      registro_sensor.id_))
        esquema.remove_session()
        return out
    
    
    @staticmethod
    def listAllFromSensorFromCommon(esquema: Esquema, sensor: SensorCommon) -> List[RegistroSensorCommon]:
        return RegistroSensorService.listAllFromSensor(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor())

    @staticmethod
    def listAllFromSensorBetweenDates(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        out: List[RegistroSensorCommon] = []
        session: Session = esquema.new_session()
        registros_sensor: List[RegistroSensor] = RegistroSensorSet.listAllFromSensorBetweenDates(session, tipo_sensor, zona_sensor, numero_sensor,fecha_inicio,fecha_fin)
        for registro_sensor in registros_sensor:
            out.append(RegistroSensorCommon(registro_sensor.tipo_sensor,registro_sensor.zona_sensor,
                                      registro_sensor.numero_sensor,registro_sensor.valor, 
                                      registro_sensor.unidad_medida, registro_sensor.fecha, 
                                      registro_sensor.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def listAllFromSensorFromCommonBetweenDates(esquema: Esquema, sensor: SensorCommon,  fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        return RegistroSensorService.listAllFromSensorBetweenDates(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor(), fecha_inicio, fecha_fin)

    @staticmethod
    def getAvgFromSensorBetweenDates(esquema: Esquema, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        out: List[RegistroSensorCommon] = []
        session: Session = esquema.new_session()
        registros_sensor: List[RegistroSensor] = RegistroSensorSet.getAvgFromSensorBetweenDates(session, tipo_sensor, zona_sensor, numero_sensor,fecha_inicio,fecha_fin)
        if len(registros_sensor)==0:
            registros_sensor: List[RegistroSensor] = []
            sensor: SensorCommon = SensorService.get(esquema,tipo_sensor,zona_sensor,numero_sensor)
            for unidad_medida in sensor.getUnidadesMedida():
                if unidad_medida == UnidadMedida.SIN_UNIDAD:
                    continue
                registro_sensor = RegistroSensor(tipo_sensor, zona_sensor, numero_sensor, 0, unidad_medida, fecha_inicio)
                registro_sensor.id_ = -1
                registros_sensor.append(registro_sensor)
        for registro_sensor in registros_sensor:
            out.append(RegistroSensorCommon(registro_sensor.tipo_sensor,registro_sensor.zona_sensor,
                                      registro_sensor.numero_sensor,registro_sensor.valor, 
                                      registro_sensor.unidad_medida, registro_sensor.fecha, 
                                      registro_sensor.id_))
        esquema.remove_session()
        return out

    @staticmethod
    def getAvgFromSensorFromCommonBetweenDates(esquema: Esquema, sensor: SensorCommon,  fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        return RegistroSensorService.getAvgFromSensorBetweenDates(esquema, sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor(), fecha_inicio, fecha_fin)


    @staticmethod
    def listAllFromPlant(esquema: Esquema, nombre_planta: str) -> List[RegistroSensorCommon]:
        planta: PlantaCommon = PlantaService.get(esquema,nombre_planta)
        lista_registros_sensores_planta: List[RegistroSensorCommon] = []
        sensores_planta_asociados: List[SensorPlantaCommon] =  SensorPlantaService.listAllSensorsFromPlantFromCommon(esquema,planta)
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
    def listAllFromPlantFromCommon(esquema: Esquema, planta: PlantaCommon) -> List[RegistroSensorCommon]:
        return RegistroSensorService.listAllFromPlant(esquema, planta.getNombrePlanta())
    
    @staticmethod
    def listAllFromPlantBetweenDates(esquema: Esquema, nombre_planta: str, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        planta: PlantaCommon = PlantaService.get(esquema,nombre_planta)
        lista_registros_sensores_planta: List[RegistroSensorCommon] = []
        sensores_planta_asociados: List[SensorPlantaCommon] =  SensorPlantaService.listAllSensorsFromPlantFromCommon(esquema,planta)
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
    def listAllFromPlantFromCommonBetweenDates(esquema: Esquema, planta: PlantaCommon, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        return RegistroSensorService.listAllFromPlantBetweenDates(esquema, planta.getNombrePlanta(), fecha_inicio, fecha_fin)

    @staticmethod
    def listAllAvgFromPlantBetweenDates(esquema: Esquema, nombre_planta: str, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        planta: PlantaCommon = PlantaService.get(esquema,nombre_planta)
        lista_registros_sensores_planta: List[RegistroSensorCommon] = []
        sensores_planta_asociados: List[SensorPlantaCommon] =  SensorPlantaService.listAllSensorsFromPlantFromCommon(esquema,planta)
        for sensor_planta_asociado in sensores_planta_asociados:
            sensor: SensorCommon = SensorService.getSensorFromRelationFromCommon(esquema, sensor_planta_asociado)
            if (fecha_fin is None):
                fecha_fin = datetime.now()
            fecha_i = fecha_inicio
            fecha_f = fecha_fin
            registros_sensor_planta = RegistroSensorService.getAvgFromSensorFromCommonBetweenDates(esquema,sensor,fecha_i, fecha_f)
            if len(registros_sensor_planta)==0:
                for unidad_medida in sensor.getUnidadesMedida():
                    registro = RegistroSensorCommon(sensor.getTipoSensor(), sensor.getZonaSensor(), sensor.getNumeroSensor(), 0, unidad_medida, fecha_i)
                    registros_sensor_planta.append(registro)
            for registro_sensor_planta in registros_sensor_planta:
                lista_registros_sensores_planta.append(registro_sensor_planta)
        return lista_registros_sensores_planta

    @staticmethod
    def listAllAvgFromPlantFromCommonBetweenDates(esquema: Esquema, planta: PlantaCommon, fecha_inicio: datetime, fecha_fin: datetime = datetime.now()) -> List[RegistroSensorCommon]:
        return RegistroSensorService.listAllAvgFromPlantBetweenDates(esquema, planta.getNombrePlanta(), fecha_inicio, fecha_fin)

    @staticmethod
    def get(esquema: Esquema, id_ : int) -> RegistroSensorCommon:
        session : Session = esquema.new_session()
        registro_sensor : RegistroSensor = RegistroSensorSet.get(session, id_)
        out= RegistroSensorCommon(registro_sensor.tipo_sensor,registro_sensor.zona_sensor, registro_sensor.numero_sensor,
                                  registro_sensor.valor, registro_sensor.unidad_medida, 
                                  registro_sensor.fecha, registro_sensor.id_)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, tipo_sensor: TipoSensor, zona_sensor: ZonaSensor, numero_sensor:int, valor:float, 
               unidad_medida: UnidadMedida, fecha: datetime, id_: int) -> RegistroSensorCommon:
        session: Session = esquema.new_session()
        out: RegistroSensorCommon = None
        try:
            registro_sensor_modificado: RegistroSensor = RegistroSensorSet.update(session, tipo_sensor, zona_sensor, 
                                                                           numero_sensor, valor, unidad_medida, fecha,id_)
            out= RegistroSensorCommon(registro_sensor_modificado.tipo_sensor,registro_sensor_modificado.zona_sensor,
                                      registro_sensor_modificado.numero_sensor,registro_sensor_modificado.valor, 
                                      registro_sensor_modificado.unidad_medida, registro_sensor_modificado.fecha, 
                                      registro_sensor_modificado.id_)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, registro_sensor: RegistroSensorCommon) -> RegistroSensorCommon:
        return RegistroSensorService.update(esquema, registro_sensor.getTipoSensor(), registro_sensor.getZonaSensor(), 
                                            registro_sensor.getNumeroSensor(), registro_sensor.getValor(), 
                                            registro_sensor.getUnidadMedida(), registro_sensor.getId())


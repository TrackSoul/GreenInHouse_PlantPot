#Author: Oscar Valverde Escobar

from datetime import datetime
from typing import List, Optional
from sqlalchemy import or_, and_
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import SensorPlanta
from backend.data.db.exc import ErrorSensorNoExiste, ErrorPlantaNoExiste, ErrorSensorPlantaExiste, ErrorSensorPlantaNoExiste
from common.data.util import TipoSensor, ZonaSensor

class SensorPlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones de asociacion entre sensores y plantas.
    """
    @staticmethod
    def create(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               nombre_planta:str, fecha_asociacion: datetime, fecha_anulacion: datetime) -> SensorPlanta:
        """
        Creacion de una nueva asociacion entre un sensor y una planta

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.
            - nombre_planta (str): Nombre de la planta asociada al sensor.
            - fecha_asociacion (datetime): Fecha de asociacion del sensor a la planta.
            - fecha_anulacion (datetime): Fecha de anulacion de la asociacion del sensor a la planta.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - SensorPlanta: Asociacion entre un sensor y una planta.
        """
        if tipo_sensor is None:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if zona_sensor is None:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if numero_sensor is None:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        if nombre_planta is None:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        nuevo_sensor_planta = None
        if SensorPlantaSet.getActiveFromSensorAndPlant(session, tipo_sensor, zona_sensor, numero_sensor, nombre_planta):
            SensorPlantaSet.getActiveFromSensorAndPlant(session, tipo_sensor, zona_sensor, numero_sensor, nombre_planta)
            session.rollback()
            raise ErrorSensorPlantaExiste(
                'Actualmente el sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 
                ' y la planta ' + nombre_planta + ' ya estan asociados.'
                )
        else:
            try:
                nuevo_sensor_planta = SensorPlanta(tipo_sensor, zona_sensor, numero_sensor, 
                                                nombre_planta, fecha_asociacion, fecha_anulacion)
                session.add(nuevo_sensor_planta)
                session.commit()
            except IntegrityError as ex:
                session.rollback()
                raise ErrorSensorPlantaExiste(
                    'Actualmente el sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 
                    ' y la planta ' + nombre_planta + ' ya estan asociados.'
                    ) from ex
            finally:
                return nuevo_sensor_planta

    @staticmethod
    def listAll(session: Session) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        sensores_planta = None
        query = session.query(SensorPlanta)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def listAllActive(session: Session) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        sensores_planta = None
        query = session.query(SensorPlanta).filter_by(fecha_anulacion=None)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def listAllSensorsFromPlant(session: Session, nombre_planta:str) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta en concreto.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de la planta asociada al sensor.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        if nombre_planta is None:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        sensores_planta = None
        query = session.query(SensorPlanta).filter_by(nombre_planta=nombre_planta)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def listAllActiveSensorsFromPlant(session: Session, nombre_planta:str) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta en concreto.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de la planta asociada al sensor.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        if nombre_planta is None:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        sensores_planta = None
        query = session.query(SensorPlanta).filter_by(nombre_planta=nombre_planta,fecha_anulacion=None)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta
    
    @staticmethod
    def listAllSensorsFromPlantBetweenDates(session: Session, nombre_planta:str, fecha_inicio: datetime, fecha_fin: datetime = None) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta en concreto.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de la planta asociada al sensor.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        if nombre_planta is None:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        if fecha_fin is None:
            fecha_fin = datetime.now()
        sensores_planta = None
        query = session.query(SensorPlanta).filter(SensorPlanta.nombre_planta == nombre_planta, SensorPlanta.fecha_asociacion < fecha_fin, 
                                                   or_(SensorPlanta.fecha_anulacion.is_(None), SensorPlanta.fecha_anulacion > fecha_inicio))
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def listAllPlantsFromSensor(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta en concreto.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        if tipo_sensor is None:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if zona_sensor is None:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if numero_sensor is None:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        sensores_planta = None
        query = session.query(SensorPlanta).filter_by(tipo_sensor=tipo_sensor, zona_sensor=zona_sensor ,numero_sensor=numero_sensor)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def listAllActivePlantsFromSensor(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta en concreto.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        if tipo_sensor is None:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if zona_sensor is None:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if numero_sensor is None:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        sensores_planta = None
        query = session.query(SensorPlanta).filter_by(tipo_sensor=tipo_sensor, zona_sensor=zona_sensor, numero_sensor=numero_sensor, fecha_anulacion=None)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta
    
    @staticmethod
    def listAllPlantsFromSensorBetweenDates(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, fecha_inicio: datetime, fecha_fin: datetime = None) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta en concreto.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de la planta asociada al sensor.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        if tipo_sensor is None:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if zona_sensor is None:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if numero_sensor is None:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        if fecha_fin is None:
            fecha_fin = datetime.now()
        sensores_planta = None
        query = session.query(SensorPlanta).filter(SensorPlanta.tipo_sensor == tipo_sensor, SensorPlanta.zona_sensor == zona_sensor, 
                                                   SensorPlanta.numero_sensor == numero_sensor, SensorPlanta.fecha_asociacion > fecha_inicio, 
                                                   or_(SensorPlanta.fecha_anulacion == None, SensorPlanta.fecha_anulacion < fecha_fin))
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def get(session: Session, id_: int) -> Optional[SensorPlanta]:
        """ 
        Obtencion de una asociacion entre un sensor y una planta

        Args:
            - session (Session): Objeto de sesion.
            - id_ (int): id_ de la asociacion de sensor planta
            
        Returns:
            - Optional[SensorPlanta]: Asociacion sensor planta 
        """
        if not id_:
            raise ValueError('Se requiere especificar un id.')
        sensor_planta: SensorPlanta = None
        try:
            query = session.query(SensorPlanta).filter_by(id_=id_)
            sensor_planta: SensorPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorSensorPlantaNoExiste(
                'La asociacion entre un sensor y una planta con el id ' + id_ + ' no existe.'
                ) from ex
        finally:
            return sensor_planta
        
    @staticmethod
    def getActiveFromSensorAndPlant(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               nombre_planta:str) -> Optional[SensorPlanta]:
        """ 
        Obtencion de una asociacion entre un sensor y una planta

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.
            - nombre_planta (str): Nombre de la planta asociada al sensor.
            
        Returns:
            - Optional[SensorPlanta]: Asociacion sensor planta 
        """
        if tipo_sensor is None:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if zona_sensor is None:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if numero_sensor is None:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        if nombre_planta is None:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        sensor_planta: SensorPlanta = None
        try:
            query = session.query(SensorPlanta).filter(SensorPlanta.tipo_sensor == tipo_sensor, SensorPlanta.zona_sensor == zona_sensor, 
                                                        SensorPlanta.numero_sensor == numero_sensor, SensorPlanta.nombre_planta == nombre_planta,
                                                        SensorPlanta.fecha_anulacion == None)
            sensor_planta: SensorPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorSensorPlantaNoExiste(
                'Actualmente el sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 
                 ' y la planta ' + nombre_planta + ' no estan asociados.'
                ) from ex
        finally:
            return sensor_planta

    @staticmethod
    def update(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               nombre_planta:str, fecha_asociacion: datetime, fecha_anulacion: datetime, id_:int) -> SensorPlanta:
        """
        Creacion de una nueva asociacion entre un sensor y una planta

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - id_ (int): id_ de la asociacion de sensor planta
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.
            - nombre_planta (str): Nombre de la planta asociada al sensor.
            - fecha_asociacion (datetime): Fecha de asociacion del sensor a la planta.
            - fecha_anulacion (datetime): Fecha de anulacion de la asociacion del sensor a la planta.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorSensorPlantaNoExiste: Si la asociacion entre el sensor y la planta no existe

        Returns:
            - SensorPlanta: Asociacion entre un sensor y una planta.
        """
        if not id_:
            raise ValueError('Se requiere especificar un id.')
        sensor_planta_modificado: SensorPlanta = None
        try:
            query = session.query(SensorPlanta).filter_by(id_=id_)
            sensor_planta: SensorPlanta = query.one()
            '''
            if sensor_planta.tipo_sensor != tipo_sensor:
                query.update({'tipo_sensor' : tipo_sensor})
            if sensor_planta.zona_sensor != zona_sensor:
                query.update({'zona_sensor' : zona_sensor})
            if sensor_planta.numero_sensor != numero_sensor:
                query.update({'numero_sensor' : numero_sensor})
            if sensor_planta.nombre_planta != nombre_planta:
                query.update({'nombre_planta' : nombre_planta})
            if sensor_planta.fecha_asociacion != fecha_asociacion:
                query.update({'fecha_asociacion' : fecha_asociacion})
            '''    
            if sensor_planta.fecha_anulacion != fecha_anulacion:
                query.update({'fecha_anulacion' : fecha_anulacion})
            session.commit()
            sensor_planta_modificado: SensorPlanta = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorSensorPlantaNoExiste(
                'La asociacion entre un sensor y una planta con el id ' + id_ + ' no existe.'
                ) from ex
        finally:
            return sensor_planta_modificado


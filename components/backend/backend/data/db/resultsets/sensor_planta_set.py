#import hashlib
#from flask import current_app

from datetime import datetime
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import SensorPlanta
from backend.data.db.exc import ErrorSensorNoExiste, ErrorRegistroPlantaNoExiste, ErrorSensorPlantaExiste, ErrorSensorPlantaNoExiste
from common.data import TipoSensor, ZonaSensor

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
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        if not nombre_planta:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        nuevo_sensor_planta = None
        try:
            nuevo_sensor_planta = SensorPlanta(tipo_sensor, zona_sensor, numero_sensor, 
                                            nombre_planta, fecha_asociacion, fecha_anulacion)
            session.add(nuevo_sensor_planta)
            session.commit()
        except IntegrityError as ex:
            session.rollback()
            raise ErrorSensorPlantaExiste(
                'El registro ' + str(nuevo_sensor_planta.id) + ' del sensor ' + str(nuevo_sensor_planta.numero_sensor) + ' de ' +  nuevo_sensor_planta.tipo_sensor + ' de ' +  nuevo_sensor_planta.zona_sensor + 'ya existe.'
                ) from ex
        return nuevo_sensor_planta

    @staticmethod
    def list_all(session: Session) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta.

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
    def listAllSensorsPlant(session: Session, nombre_planta:str) -> List[SensorPlanta]:
        """
        Lista de sensores asociados a una planta.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[SensorPlanta]: Sensores asociados a una planta.
        """
        sensores_planta = None
        query = session.query(SensorPlanta).filter_by(nombre_planta=nombre_planta)
        sensores_planta: List[SensorPlanta] = query.all()
        return sensores_planta

    @staticmethod
    def get(session: Session, id: int) -> Optional[SensorPlanta]:
        """ 
        Obtencion de una asociacion entre un sensor y una planta

        Args:
            - session (Session): Objeto de sesion.
            - id (int): Id de la asociacion de sensor planta
            
        Returns:
            - Optional[SensorPlanta]: Asociacion sensor planta 
        """
        if not id:
            raise ValueError('Se requiere especificar un Id.')
        try:
            query = session.query(SensorPlanta).filter_by(id=id)
            sensor: SensorPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorSensorPlantaNoExiste(
                'La asociacion entre un sensor y una planta con el id ' + id + ' no existe.'
                ) from ex
        return sensor

'''
    @staticmethod
    def update(session: Session,id:int):

        if not id:
            raise ValueError('An id is requiered.')
        try:
            session.query(Pregunta).filter(Pregunta.id == id).update({"visible": False})
            session.commit()
        except NoResultFound as ex:
            raise PreguntaNoExisteError(
                'The question with title ' + id + ' don\'t exists.'
                ) from ex

    @staticmethod
    def update(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               modelo_sensor:str, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int, 
               patilla_3_lectura:int, patilla_4_lectura:int,
               fecha_creacion:datetime ,fecha_eliminacion:datetime):

        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        try:
            query = session.query(Sensor).filter_by(tipo_sensor=tipo_sensor,zona_sensor=zona_sensor,numero_sensor=numero_sensor)
            query.update({'modelo_sensor' : modelo_sensor})
            query.update({'direccion_lectura' : direccion_lectura})
            query.update({'patilla_1_lectura' : patilla_1_lectura})
            query.update({'patilla_2_lectura' : patilla_2_lectura})
            query.update({'patilla_3_lectura' : patilla_3_lectura})
            query.update({'patilla_4_lectura' : patilla_4_lectura})
            #query.update({'fecha_creacion' : fecha_creacion})
            query.update({'fecha_eliminacion' : fecha_eliminacion})
            #setattr(query, 'modelo_sensor', modelo_sensor)
            session.commit()
            sensor_modificado: Sensor = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorSensorNoExiste(
                'El sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 'no existe.'
                ) from ex
        return sensor_modificado

'''
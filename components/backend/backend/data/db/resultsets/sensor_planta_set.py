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
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               nombre_planta:str, fecha_asociacion: datetime, fecha_anulacion: datetime) -> SensorPlanta:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (str): Tipo de sensor.
            - numero_sensor (str): Numero de sensor.
            - valor (float): Valor de lectura del sensor.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor asociado.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor asociado.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor asociado.')
        if not nombre_planta:
            raise ValueError('Necesario especificar el nombre de la planta asociada.')
        try:
            nuevo_sensor_planta = SensorPlanta(tipo_sensor, zona_sensor, numero_sensor, 
                                            nombre_planta, fecha_asociacion, fecha_anulacion)
            session.add(nuevo_sensor_planta)
            session.commit()
            return nuevo_sensor_planta
        except IntegrityError as ex:
            session.rollback()
            raise ErrorSensorPlantaExiste(
                'El registro ' + str(nuevo_sensor_planta.id) + ' del sensor ' + str(nuevo_sensor_planta.numero_sensor) + ' de ' +  nuevo_sensor_planta.tipo_sensor + ' de ' +  nuevo_sensor_planta.zona_sensor + 'ya existe.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[SensorPlanta]:
    #def list_all(session: Session, tipo_sensor:str ,numero_sensor:str) -> List[Sensor]:
        """Lists every user.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[User]: Lista de registros del sensor.
        """
        query = session.query(SensorPlanta)
        return query.all()

    @staticmethod
    def get(session: Session, id: str) -> Optional[SensorPlanta]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): Objeto de sesion.
            - id (str): The question id to find
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(SensorPlanta).filter_by(id=id)
            sensor: SensorPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorSensorPlantaNoExiste(
                'El registro de sensor con el id ' + id + ' no existe.'
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
'''
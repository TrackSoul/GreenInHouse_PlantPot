#import hashlib
#from flask import current_app

from datetime import datetime
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import Sensor
from backend.data.db.exc import ErrorSensorExiste, ErrorSensorNoExiste
from common.data import TipoSensor, ZonaSensor

class SensorSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               modelo_sensor:str, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int, 
               patilla_3_lectura:int, patilla_4_lectura:int,
               fecha_creacion:datetime ,fecha_eliminacion:datetime) -> Sensor:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (str): Tipo de sensor.
            - numero_sensor (str): Numero de sensor.
            - modelo_sensor (str): modelo_sensor del sensor.
            - direccion_lectura (str): Direccion de lectura del sensor.
            - patilla_1_lectura (int): Patilla 1 de lectura del sensor.
            - patilla_2_lectura (int): Patilla 2 de lectura del sensor.
            - patilla_3_lectura (int): Patilla 3 de lectura del sensor.
            - patilla_4_lectura (int): Patilla 4 de lectura del sensor.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorSensorExiste: Si el sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        if not modelo_sensor:
            raise ValueError('Necesario especificar el modelo del sensor.')
        if not direccion_lectura and not patilla_1_lectura:
            raise ValueError('Necesario especificar la direccion o patilla de lectura del sensor.')
        try:
            nuevo_sensor = Sensor(tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                  direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                  patilla_3_lectura, patilla_4_lectura, 
                                  fecha_creacion, fecha_eliminacion)
            session.add(nuevo_sensor)
            session.commit()
            return nuevo_sensor
        except IntegrityError as ex:
            session.rollback()
            raise ErrorSensorExiste(
                'El sensor ' + str(numero_sensor) + ' de ' +  str(tipo_sensor) + ' de ' +  str(zona_sensor) + ' ya existe.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Sensor]:
    #def list_all(session: Session, tipo_sensor:str ,numero_sensor:str) -> List[Sensor]:
        """Lists every user.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[User]: Lista de registros del sensor.
        """
        query = session.query(Sensor)
        return query.all()

    @staticmethod
    def get(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int,) -> Optional[Sensor]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): Objeto de sesion.
            - id (str): The question id to find
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        try:
            query = session.query(Sensor).filter_by(tipo_sensor=tipo_sensor,zona_sensor=zona_sensor,numero_sensor=numero_sensor)
            sensor: Sensor = query.one()
        except NoResultFound as ex:
            raise ErrorSensorNoExiste(
                'El sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 'no existe.'
                ) from ex
        return sensor

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

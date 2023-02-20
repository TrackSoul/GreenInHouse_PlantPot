#import hashlib
#from flask import current_app

from datetime import datetime
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import RegistroSensor
from backend.data.db.exc import ErrorSensorExiste, ErrorSensorNoExiste, ErrorRegistroSensorExiste, ErrorRegistroSensorNoExiste
from common.data import TipoSensor, ZonaSensor

class RegistroSensorSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               valor:float, escala:str, fecha: datetime ) -> RegistroSensor:
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
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        if not valor:
            raise ValueError('Necesario especificar el valor del sensor.')
        if not escala:
            raise ValueError('Necesario especificar la escala del sensor.')
        try:
            nuevo_registro = RegistroSensor(tipo_sensor, zona_sensor, numero_sensor, valor, escala, fecha)
            session.add(nuevo_registro)
            session.commit()
            return nuevo_registro
        except IntegrityError as ex:
            session.rollback()
            raise ErrorRegistroSensorExiste(
                'El registro ' + str(nuevo_registro.id) + ' del sensor ' + str(nuevo_registro.numero_sensor) +
                  ' de ' +  nuevo_registro.tipo_sensor + ' de ' +  nuevo_registro.zona_sensor + 'ya existe.'
                ) from ex

    @staticmethod
    def listAll(session: Session) -> List[RegistroSensor]:
    #def list_all(session: Session, tipo_sensor:str ,numero_sensor:str) -> List[Sensor]:
        """Lists every user.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[User]: Lista de registros del sensor.
        """
        query = session.query(RegistroSensor)
        return query.all()

    @staticmethod
    def get(session: Session, id: str) -> Optional[RegistroSensor]:
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
            query = session.query(RegistroSensor).filter_by(id=id)
            sensor: RegistroSensor = query.one()
        except NoResultFound as ex:
            raise ErrorRegistroSensorNoExiste(
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
#import hashlib
#from flask import current_app

from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results.registro_planta import RegistroPlanta
from backend.data.db.exc import ErrorRegistroPlantaExiste, ErrorRegistroPlantaNoExiste, ErrorRegistroTipoPlantaNoExiste

class RegistroPlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, nombre_planta:str, tipo_planta:str) -> RegistroPlanta:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de planta.
            - tipo_planta (str): Tipo de planta.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if not nombre_planta:
            raise ValueError('Necesario especificar el nombre de la planta.')
        if not tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        try:
            nuevo_registro = RegistroPlanta(nombre_planta, tipo_planta)
            session.add(nuevo_registro)
            session.commit()
            return nuevo_registro
        except IntegrityError as ex:
            session.rollback()
            raise ErrorRegistroPlantaExiste(
                'El nombre de planta ' + str(nombre_planta) + ' ya está registrado.'
                ) from ex
        except NoResultFound as ex:
            raise ErrorRegistroTipoPlantaNoExiste(
                'El tipo de planta ' + tipo_planta + 'no existe'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[RegistroPlanta]:
        """Lists every user.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[User]: Lista de registros del sensor.
        """
        query = session.query(RegistroPlanta)
        return query.all()

    @staticmethod
    def get(session: Session, nombre_planta: str) -> Optional[RegistroPlanta]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): The question id to find
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not nombre_planta:
            raise ValueError('Necesario especificar el nombre de la planta.')
        try:
            query = session.query(RegistroPlanta).filter_by(nombre_planta=nombre_planta)
            planta: RegistroPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorRegistroPlantaNoExiste(
                'La planta con el nombre' + nombre_planta + 'no existe'
                ) from ex
        return RegistroPlanta

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
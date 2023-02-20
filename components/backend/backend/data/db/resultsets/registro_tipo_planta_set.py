#import hashlib
#from flask import current_app

from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import RegistroTipoPlanta
from backend.data.db.exc import ErrorRegistroTipoPlantaExiste, ErrorRegistroTipoPlantaNoExiste

class RegistroTipoPlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, tipo_planta:str, descripcion_planta:str) -> RegistroTipoPlanta:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            - descripcion_planta (str): Descripcion de planta.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if not tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if not descripcion_planta:
            raise ValueError('Necesario especificar una descripcion de la planta.')
        try:
            nuevo_registro = RegistroTipoPlanta(tipo_planta, descripcion_planta)
            session.add(nuevo_registro)
            session.commit()
            return nuevo_registro
        except IntegrityError as ex:
            session.rollback()
            raise ErrorRegistroTipoPlantaExiste(
                'El nombre de planta ' + str(tipo_planta) + ' ya está registrado.'
                ) from ex

    @staticmethod
    def listAll(session: Session) -> List[RegistroTipoPlanta]:
        """Lists every user.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[RegistroTipoPlanta]: Lista de registros de tipos de plantas.
        """
        query = session.query(RegistroTipoPlanta)
        return query.all()

    @staticmethod
    def get(session: Session, tipo_planta: str) -> Optional[RegistroTipoPlanta]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): Objeto de sesion.
            - id (str): The question id to find
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        try:
            query = session.query(RegistroTipoPlanta).filter_by(tipo_planta=tipo_planta)
            planta: RegistroTipoPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorRegistroTipoPlantaNoExiste(
                'La planta con el nombre' + tipo_planta + 'no existe'
                ) from ex
        return RegistroTipoPlanta

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
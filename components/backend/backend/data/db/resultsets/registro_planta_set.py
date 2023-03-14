from datetime import datetime
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
    def create(session: Session, nombre_planta:str, tipo_planta:str, fecha_plantacion: datetime, fecha_marchitacion: datetime) -> RegistroPlanta:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de planta.
            - tipo_planta (str): Tipo de planta.
            - fecha_plantacion (datetime): Fecha en la que se planto la planta
            - fecha_marchitacion (datetime): Fecha en la que se marchito la planta

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
            nuevo_registro_planta = RegistroPlanta(nombre_planta, tipo_planta, fecha_plantacion, fecha_marchitacion)
            session.add(nuevo_registro_planta)
            session.commit()
            return nuevo_registro_planta
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
    def listAll(session: Session) -> List[RegistroPlanta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[RegistroPlanta]: Listado de registros de plantas.
        """
        plantas = None
        query = session.query(RegistroPlanta)
        plantas: List[RegistroPlanta] = query.all()
        return plantas

    @staticmethod
    def listAllActive(session: Session) -> List[RegistroPlanta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[RegistroPlanta]: Listado de registros de plantas.
        """
        plantas = None
        query = session.query(RegistroPlanta).filter_by(fecha_marchitacion=None)
        plantas: List[RegistroPlanta] = query.all()
        return plantas

    @staticmethod
    def listAllFromType(session: Session, tipo_planta: str) -> List[RegistroPlanta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[RegistroPlanta]: Listado de registros de plantas.
        """
        plantas_de_tipo = None
        query = session.query(RegistroPlanta).filter_by(tipo_planta=tipo_planta)
        plantas_de_tipo: List[RegistroPlanta] = query.all()
        return plantas_de_tipo

    @staticmethod
    def listAllActiveFromType(session: Session, tipo_planta: str) -> List[RegistroPlanta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[RegistroPlanta]: Listado de registros de plantas.
        """
        plantas_de_tipo = None
        query = session.query(RegistroPlanta).filter_by(fecha_marchitacion=None,tipo_planta=tipo_planta)
        plantas_de_tipo: List[RegistroPlanta] = query.all()
        return plantas_de_tipo

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
        registro_planta: RegistroPlanta = None
        try:
            query = session.query(RegistroPlanta).filter_by(nombre_planta=nombre_planta)
            registro_planta: RegistroPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorRegistroPlantaNoExiste(
                'La planta con el nombre' + nombre_planta + 'no existe'
                ) from ex
        finally:
            return registro_planta

    @staticmethod
    def update(session: Session, nombre_planta:str, tipo_planta:str, fecha_plantacion: datetime, fecha_marchitacion: datetime) -> RegistroPlanta:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): Nombre de planta.
            - tipo_planta (str): Tipo de planta.
            - fecha_plantacion (datetime): Fecha en la que se planto la planta
            - fecha_marchitacion (datetime): Fecha en la que se marchito la planta

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if not nombre_planta:
            raise ValueError('Necesario especificar el nombre de la planta.')
        registro_planta_modificado: RegistroPlanta = None
        try:
            query = session.query(RegistroPlanta).filter_by(nombre_planta=nombre_planta)
            registro_planta: RegistroPlanta = query.one()

            if registro_planta.tipo_planta != tipo_planta:
                query.update({'tipo_planta' : tipo_planta})
            if registro_planta.fecha_marchitacion != fecha_marchitacion:
                query.update({'fecha_marchitacion' : fecha_marchitacion})
            session.commit()
            registro_planta_modificado: RegistroPlanta = query.one() 

        except NoResultFound as ex:
            session.rollback()
            raise ErrorRegistroPlantaNoExiste(
                'La planta con el nombre' + nombre_planta + 'no existe'
                ) from ex
        finally:
            return registro_planta_modificado

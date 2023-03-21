from datetime import datetime
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results.planta import Planta
from backend.data.db.exc import ErrorPlantaExiste, ErrorPlantaNoExiste, ErrorTipoPlantaNoExiste

class PlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, nombre_planta:str, tipo_planta:str, fecha_plantacion: datetime, fecha_marchitacion: datetime) -> Planta:
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
        if nombre_planta is None:
            raise ValueError('Necesario especificar el nombre de la planta.')
        if tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta.')
        try:
            nuevo_planta = Planta(nombre_planta, tipo_planta, fecha_plantacion, fecha_marchitacion)
            session.add(nuevo_planta)
            session.commit()
            return nuevo_planta
        except IntegrityError as ex:
            session.rollback()
            raise ErrorPlantaExiste(
                'El nombre de planta ' + str(nombre_planta) + ' ya está registrado.'
                ) from ex
        except NoResultFound as ex:
            raise ErrorTipoPlantaNoExiste(
                'El tipo de planta ' + tipo_planta + 'no existe'
                ) from ex

    @staticmethod
    def listAll(session: Session) -> List[Planta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[Planta]: Listado de registros de plantas.
        """
        plantas = None
        query = session.query(Planta)
        plantas: List[Planta] = query.all()
        return plantas

    @staticmethod
    def listAllActive(session: Session) -> List[Planta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[Planta]: Listado de registros de plantas.
        """
        plantas = None
        query = session.query(Planta).filter_by(fecha_marchitacion=None)
        plantas: List[Planta] = query.all()
        return plantas

    @staticmethod
    def listAllFromType(session: Session, tipo_planta: str) -> List[Planta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[Planta]: Listado de registros de plantas.
        """
        plantas_de_tipo = None
        query = session.query(Planta).filter_by(tipo_planta=tipo_planta)
        plantas_de_tipo: List[Planta] = query.all()
        return plantas_de_tipo

    @staticmethod
    def listAllActiveFromType(session: Session, tipo_planta: str) -> List[Planta]:
        """
        Listado de plantas.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[Planta]: Listado de registros de plantas.
        """
        plantas_de_tipo = None
        query = session.query(Planta).filter_by(fecha_marchitacion=None,tipo_planta=tipo_planta)
        plantas_de_tipo: List[Planta] = query.all()
        return plantas_de_tipo

    @staticmethod
    def get(session: Session, nombre_planta: str) -> Optional[Planta]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): Objeto de sesion.
            - nombre_planta (str): The question id to find
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not nombre_planta:
            raise ValueError('Necesario especificar el nombre de la planta.')
        planta: Planta = None
        try:
            query = session.query(Planta).filter_by(nombre_planta=nombre_planta)
            planta: Planta = query.one()
        except NoResultFound as ex:
            raise ErrorPlantaNoExiste(
                'La planta con el nombre' + nombre_planta + 'no existe'
                ) from ex
        finally:
            return planta

    @staticmethod
    def update(session: Session, nombre_planta:str, tipo_planta:str, fecha_plantacion: datetime, fecha_marchitacion: datetime) -> Planta:
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
        planta_modificado: Planta = None
        try:
            query = session.query(Planta).filter_by(nombre_planta=nombre_planta)
            planta: Planta = query.one()

            if planta.tipo_planta != tipo_planta:
                query.update({'tipo_planta' : tipo_planta})
            if planta.fecha_marchitacion != fecha_marchitacion:
                query.update({'fecha_marchitacion' : fecha_marchitacion})
            session.commit()
            planta_modificado: Planta = query.one() 

        except NoResultFound as ex:
            session.rollback()
            raise ErrorPlantaNoExiste(
                'La planta con el nombre' + nombre_planta + 'no existe'
                ) from ex
        finally:
            return planta_modificado

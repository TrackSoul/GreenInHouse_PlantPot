from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import TipoPlanta
from backend.data.db.exc import ErrorTipoPlantaExiste, ErrorTipoPlantaNoExiste

class TipoPlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, nombre_tipo_planta:str, descripcion_tipo_planta:str) -> TipoPlanta:
        """
        Creacion de un nuevo registro de un tipo de planta.

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
        if nombre_tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if descripcion_tipo_planta is None:
            raise ValueError('Necesario especificar una descripcion de la planta.')
        nuevo_tipo_planta = None
        try:
            nuevo_tipo_planta = TipoPlanta(nombre_tipo_planta, descripcion_tipo_planta)
            session.add(nuevo_tipo_planta)
            session.commit()
        except IntegrityError as ex:
            session.rollback()
            raise ErrorTipoPlantaExiste(
                'El nombre de planta ' + str(nombre_tipo_planta) + ' ya está registrado.'
                ) from ex
        finally:
            return nuevo_tipo_planta

    @staticmethod
    def listAll(session: Session) -> List[TipoPlanta]:
        """
        istado de tipos de plantas

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[TipoPlanta]: Lista de registros de tipos de plantas.
        """
        query = session.query(TipoPlanta)
        return query.all()

    @staticmethod
    def get(session: Session, nombre_tipo_planta: str) -> Optional[TipoPlanta]:
        """ 
        Obtener un registro de tipo de planta.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not nombre_tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        tipo_planta: TipoPlanta = None
        try:
            query = session.query(TipoPlanta).filter_by(tipo_planta=nombre_tipo_planta)
            tipo_planta: TipoPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorTipoPlantaNoExiste(
                'El tipo de planta con el nombre' + nombre_tipo_planta + 'no existe'
                ) from ex
        finally:
            return tipo_planta

    @staticmethod
    def update(session: Session, nombre_tipo_planta:str, descripcion_tipo_planta:str) -> TipoPlanta:
        """
        Modificacion de un registro de un tipo de planta.

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
        if not nombre_tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if not descripcion_tipo_planta:
            raise ValueError('Necesario especificar una descripcion de la planta.')
        tipo_planta_modificado: TipoPlanta = None
        try:
            query = session.query(TipoPlanta).filter_by(tipo_planta=nombre_tipo_planta)
            tipo_planta: TipoPlanta = query.one()
            if tipo_planta.descripcion_planta != descripcion_tipo_planta:
                query.update({'descripcion_planta' : descripcion_tipo_planta})
            session.commit()
            tipo_planta_modificado: TipoPlanta = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorTipoPlantaNoExiste(
                'El tipo de planta con el nombre' + nombre_tipo_planta + 'no existe'
                ) from ex
        finally:
            return tipo_planta_modificado
        
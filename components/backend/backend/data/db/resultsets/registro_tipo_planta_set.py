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
        if not tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if not descripcion_planta:
            raise ValueError('Necesario especificar una descripcion de la planta.')
        nuevo_registro_tipo_planta = None
        try:
            nuevo_registro_tipo_planta = RegistroTipoPlanta(tipo_planta, descripcion_planta)
            session.add(nuevo_registro_tipo_planta)
            session.commit()
        except IntegrityError as ex:
            session.rollback()
            raise ErrorRegistroTipoPlantaExiste(
                'El nombre de planta ' + str(tipo_planta) + ' ya está registrado.'
                ) from ex
        finally:
            return nuevo_registro_tipo_planta

    @staticmethod
    def listAll(session: Session) -> List[RegistroTipoPlanta]:
        """
        istado de tipos de plantas

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[RegistroTipoPlanta]: Lista de registros de tipos de plantas.
        """
        query = session.query(RegistroTipoPlanta)
        return query.all()

    @staticmethod
    def get(session: Session, tipo_planta: str) -> Optional[RegistroTipoPlanta]:
        """ 
        Obtener un registro de tipo de planta.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        registro_tipo_planta: RegistroTipoPlanta = None
        try:
            query = session.query(RegistroTipoPlanta).filter_by(tipo_planta=tipo_planta)
            registro_tipo_planta: RegistroTipoPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorRegistroTipoPlantaNoExiste(
                'El tipo de planta con el nombre' + tipo_planta + 'no existe'
                ) from ex
        finally:
            return registro_tipo_planta

    @staticmethod
    def update(session: Session, tipo_planta:str, descripcion_planta:str) -> RegistroTipoPlanta:
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
        if not tipo_planta:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if not descripcion_planta:
            raise ValueError('Necesario especificar una descripcion de la planta.')
        registro_tipo_planta_modificado: RegistroTipoPlanta = None
        try:
            query = session.query(RegistroTipoPlanta).filter_by(tipo_planta=tipo_planta)
            registro_tipo_planta: RegistroTipoPlanta = query.one()
            if registro_tipo_planta.descripcion_planta != descripcion_planta:
                query.update({'descripcion_planta' : descripcion_planta})
            session.commit()
            registro_tipo_planta_modificado: RegistroTipoPlanta = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorRegistroTipoPlantaNoExiste(
                'El tipo de planta con el nombre' + tipo_planta + 'no existe'
                ) from ex
        finally:
            return registro_tipo_planta_modificado
        
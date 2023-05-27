from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import TipoPlanta, ConsejoTipoPlanta
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida
from backend.data.db.exc import ErrorConsejoTipoPlantaExiste, ErrorConsejoTipoPlantaNoExiste

class ConsejoTipoPlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float) -> ConsejoTipoPlanta:
        """
        Creacion de un nuevo consejo de un tipo de planta.

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - descripcion (str): Descripcion de los consejos del tipo de planta
            - tipo_planta (str): Tipo de planta.
            - zona_consejo (ZonaSensor): Zona asociada al consejo
            - tipo_medida (TipoMedida): Tipo medida asociada al consejo
            - unidad_medida (UnidadMedida): 
            - valor_minimo: (float): 
            - valor_maximo (float): 
            - horas_minimas (float): 
            - horas_maximas (float): 

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorConsejoTipoPlantaExiste: Si el consejo del tipo de planta de esa zona y tipo de medida especificados ya existe

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if descripcion is None:
            raise ValueError('Necesario especificar la descripcion de los consejos de la planta.')
        if tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta a la que se aplicaran los consejos.')
        if zona_consejo is None:
            raise ValueError('Necesario especificar la zona en la que se aplicaran los consejos de la planta.')
        if tipo_medida is None:
            raise ValueError('Necesario especificar el tipo de medida de los consejos del tipo de la planta.')
        if unidad_medida is None:
            raise ValueError('Necesario especificar la unidad de medida de los consejos del tipo de la planta.')
        if valor_minimo is None:
            raise ValueError('Necesario especificar el valor minimo del consejo del tipo de la planta.')
        if valor_maximo is None:
            raise ValueError('Necesario especificar el valor maximo del consejo del tipo de la planta.')

        nuevo_consejo_tipo_planta = None
        try:
            nuevo_consejo_tipo_planta = ConsejoTipoPlanta(descripcion, tipo_planta, zona_consejo,
                                                          tipo_medida, unidad_medida, valor_minimo,
                                                          valor_maximo, horas_minimas, horas_maximas)
            session.add(nuevo_consejo_tipo_planta)
            session.commit()
        except IntegrityError as ex:
            session.rollback()
            raise ErrorConsejoTipoPlantaExiste(
                'El consejo del tipo de planta ' + str(tipo_planta) + ' para la medida ' + str(tipo_medida) +
                ' en la zona ' + str(zona_consejo) + ' ya está registrado.'
                ) from ex
        finally:
            return nuevo_consejo_tipo_planta

    @staticmethod
    def listAll(session: Session) -> List[ConsejoTipoPlanta]:
        """
        istado de consejos de tipo de planta.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[ConsejoTipoPlanta]: Listado de consejos de tipo de planta.
        """
        query = session.query(ConsejoTipoPlanta)
        return query.all()

    @staticmethod
    def listAllFromTypePlant(session: Session, tipo_planta: str) -> List[ConsejoTipoPlanta]:
        """
        Listado de consejos de un tipo de planta especifico.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.

        Returns:
            - List[ConsejoTipoPlanta]: Listado de consejos de tipo de planta.
        """
        consejos = None
        query = session.query(ConsejoTipoPlanta).filter_by(nombre_elemento=tipo_planta)
        consejos: List[ConsejoTipoPlanta] = query.all()
        return consejos
    
    @staticmethod
    def listAllFromZone(session: Session, zona_consejo: ZonaSensor) -> List[ConsejoTipoPlanta]:
        """
        Listado de consejos de una zona especifica.

        Args:
            - session (Session): Objeto de sesion.
            - zona_consejo (ZonaSensor): Zona asociada al consejo.

        Returns:
            - List[ConsejoTipoPlanta]: Listado de consejos de tipo de planta.
        """
        consejos = None
        query = session.query(ConsejoTipoPlanta).filter_by(zona_consejo=zona_consejo)
        consejos: List[ConsejoTipoPlanta] = query.all()
        return consejos
    
    @staticmethod
    def listAllFromTypeMeasure(session: Session, tipo_medida: TipoMedida) -> List[ConsejoTipoPlanta]:
        """
        Listado de consejos de un tipo de media especifico.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_medida (TipoMedida): Tipo de medida.

        Returns:
            - List[ConsejoTipoPlanta]: Listado de consejos de tipo de planta.
        """
        consejos = None
        query = session.query(ConsejoTipoPlanta).filter_by(tipo_medida=tipo_medida)
        consejos: List[ConsejoTipoPlanta] = query.all()
        return consejos
    
    @staticmethod
    def listAllFromTypePlantAndZone(session: Session, tipo_planta: str, zona_consejo: ZonaSensor) -> List[ConsejoTipoPlanta]:
        """
        Listado de consejos de un tipo de planta y zona especificos.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            - zona_consejo (ZonaSensor): Zona asociada al consejo.

        Returns:
            - List[ConsejoTipoPlanta]: Listado de consejos de tipo de planta.
        """
        consejos = None
        query = session.query(ConsejoTipoPlanta).filter_by(nombre_elemento=tipo_planta, zona_consejo=zona_consejo)
        consejos: List[ConsejoTipoPlanta] = query.all()
        return consejos
    
    @staticmethod
    def listAllFromTypePlantAndTypeMeasure(session: Session, tipo_planta: str, tipo_medida: TipoMedida) -> List[ConsejoTipoPlanta]:
        """
        Listado de consejos de un tipo de planta y tipo de medida especifico.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            - tipo_medida (TipoMedida): Tipo de medida.

        Returns:
            - List[ConsejoTipoPlanta]: Listado de consejos de tipo de planta.
        """
        consejos = None
        query = session.query(ConsejoTipoPlanta).filter_by(nombre_elemento=tipo_planta, tipo_medida=tipo_medida)
        consejos: List[ConsejoTipoPlanta] = query.all()
        return consejos
    
    @staticmethod
    def get(session: Session, tipo_planta: str, zona_consejo:ZonaSensor, tipo_medida:TipoMedida) -> Optional[ConsejoTipoPlanta]:
        """ 
        Obtencvion de consejo de un tipo de planta, zona y tipo de medida especificos.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            - zona_consejo (ZonaSensor): Zona asociada al consejo.
            - tipo_medida (TipoMedida): Tipo de medida.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorConsejoTipoPlantaNoExiste: Si el consejo del tipo
                    de planta de esa zona y tipo de medida especificados no existe

        Returns:
            - Optional[ConsejoTipoPlanta]: The question 
        """
        if tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta a la que se aplicaran los consejos.')
        if zona_consejo is None:
            raise ValueError('Necesario especificar la zona en la que se aplicaran los consejos de la planta.')
        if tipo_medida is None:
            raise ValueError('Necesario especificar el tipo de medida de los consejos del tipo de la planta.')
        consejo: ConsejoTipoPlanta = None
        try:
            query = session.query(ConsejoTipoPlanta).filter_by(nombre_elemento=tipo_planta, zona_consejo=zona_consejo, tipo_medida=tipo_medida)
            consejo: ConsejoTipoPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorConsejoTipoPlantaNoExiste(
                'El consejo del tipo de planta ' + str(tipo_planta) + ' para la medida ' + str(tipo_medida) +
                ' en la zona ' + str(zona_consejo) + ' ya está registrado.'
                ) from ex
        finally:
            return consejo

    @staticmethod
    def update(session: Session, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                valor_maximo:float, horas_minimas:float, horas_maximas:float) -> ConsejoTipoPlanta:
        """
        Modificacion de un consejo de un tipo de planta.

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - descripcion (str): Descripcion de los consejos del tipo de planta
            - tipo_planta (str): Tipo de planta.
            - zona_consejo (ZonaSensor): Zona asociada al consejo
            - tipo_medida (TipoMedida): Tipo medida asociada al consejo
            - unidad_medida (UnidadMedida): 
            - valor_minimo: (float): 
            - valor_maximo (float): 
            - horas_minimas (float): 
            - horas_maximas (float):        

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorConsejoTipoPlantaNoExiste: Si el consejo del tipo de planta de esa zona y tipo de medida especificados no existe

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if descripcion is None:
            raise ValueError('Necesario especificar la descripcion de los consejos de la planta.')
        if tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta a la que se aplicaran los consejos.')
        if zona_consejo is None:
            raise ValueError('Necesario especificar la zona en la que se aplicaran los consejos de la planta.')
        if tipo_medida is None:
            raise ValueError('Necesario especificar el tipo de medida de los consejos del tipo de la planta.')
        if unidad_medida is None:
            raise ValueError('Necesario especificar la unidad de medida de los consejos del tipo de la planta.')
        if valor_minimo is None:
            raise ValueError('Necesario especificar el valor minimo del consejo del tipo de la planta.')
        if valor_maximo is None:
            raise ValueError('Necesario especificar el valor maximo del consejo del tipo de la planta.')

        consejo_modificado = None
        try:
            query = session.query(ConsejoTipoPlanta).filter_by(nombre_elemento=tipo_planta, zona_consejo=zona_consejo, tipo_medida=tipo_medida)
            consejo: ConsejoTipoPlanta = query.one()
            if consejo.descripcion != descripcion:
                query.update({'descripcion' : descripcion})
            if consejo.unidad_medida != unidad_medida:
                query.update({'unidad_medida' : unidad_medida})
            if consejo.valor_minimo != valor_minimo:
                query.update({'valor_minimo' : valor_minimo})
            if consejo.valor_maximo != valor_maximo:
                query.update({'valor_maximo' : valor_maximo})
            if consejo.horas_minimas != horas_minimas:
                query.update({'horas_minimas' : horas_minimas})
            if consejo.horas_maximas != horas_maximas:
                query.update({'horas_maximas' : horas_maximas})
            session.commit()
            consejo_modificado: ConsejoTipoPlanta = query.one() 
        except NoResultFound as ex:
            raise ErrorConsejoTipoPlantaNoExiste(
                'El consejo del tipo de planta ' + str(tipo_planta) + ' para la medida ' + str(tipo_medida) +
                ' en la zona ' + str(zona_consejo) + ' ya está registrado.'
                ) from ex
        finally:
            return consejo_modificado
        
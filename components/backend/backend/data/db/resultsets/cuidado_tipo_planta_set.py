from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import TipoPlanta, CuidadoTipoPlanta
from common.data.util import TipoMedida, UnidadMedida
from backend.data.db.exc import ErrorTipoPlantaExiste, ErrorTipoPlantaNoExiste

class CuidadoTipoPlantaSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los registros.
    """
    @staticmethod
    def create(session: Session, tipo_planta:str, temperatura_minima:float, temperatura_maxima:float, unidad_temperatura:UnidadMedida,
      humedad_ambiente_minima:float, humedad_ambiente_maxima:float, humedad_maceta_minima:float, humedad_maceta_maxima:float, 
      humedad_suelo_minima:float, humedad_suelo_maxima:float, unidad_humedad: UnidadMedida, luz_minima:float, luz_maxima:float, 
      unidad_luz:UnidadMedida, horas_luz_minimas:float, horas_luz_maximas:float, dias_germinacion:int, dias_maduracion:int,
      dias_marchitacion:int, descripcion: str) -> CuidadoTipoPlanta:
        """
        Creacion de un nuevo cuidado de un tipo de planta.

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            - temperatura_minima: (float): 
            - temperatura_maxima (float): 
            - unidad_temperatura (UnidadMedida): 
            - humedad_ambiente_minima (float):  
            - humedad_ambiente_maxima (float):  
            - humedad_maceta_minima (float):  
            - humedad_maceta_maxima (float): 
            - humedad_suelo_minima (float):  
            - humedad_suelo_maxima (float):  
            - unidad_humedad (UnidadMedida): 
            - luz_minima (float):  
            - luz_maxima (float): 
            - unidad_luz (UnidadMedida): 
            - horas_luz_minimas (float): 
            - horas_luz_maximas (float): 
            - dias_germinacion (int): Numero de dias que tarda en germinar la planta desde su plantacion
            - dias_maduracion (int): Numero de dias que tarda en madurar la planta desde su plantacion
            - dias_marchitacion (int):  Numero de dias que tarda en marchitar la planta desde su plantacion
            - descripcion (str): Descripcion de los cuidados del tipo de planta

            

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if temperatura_minima is None:
            raise ValueError('Necesario especificar la temperatura minima de la planta.')
        if temperatura_maxima is None:
            raise ValueError('Necesario especificar la temperatura maxima de la planta.')
        if unidad_temperatura is None:
            raise ValueError('Necesario especificar la unidad de temperatura de la planta.')
        if humedad_ambiente_minima is None:
            raise ValueError('Necesario especificar la humedad minima del ambiente de la planta.')
        if humedad_ambiente_maxima is None:
            raise ValueError('Necesario especificar la humedad maxima del ambiente de la planta.')
        if humedad_maceta_minima is None:
            raise ValueError('Necesario especificar la humedad minima de la maceta de la planta.')
        if humedad_maceta_maxima is None:
            raise ValueError('Necesario especificar la humedad maxima de la maceta de la planta.')
        if humedad_suelo_minima is None:
            raise ValueError('Necesario especificar la humedad minima del suelo de la planta.')
        if humedad_suelo_maxima is None:
            raise ValueError('Necesario especificar la humedad maxima del suelo de la planta.')
        if unidad_humedad is None:
            raise ValueError('Necesario especificar la unidad de humedad de la planta.')
        if luz_minima is None:
            raise ValueError('Necesario especificar la cantidad minima de luz de la planta.')
        if luz_maxima is None:
            raise ValueError('Necesario especificar la cantidad maxima de luz de la planta.')
        if unidad_luz is None:
            raise ValueError('Necesario especificar la unidad de luz de la planta.')
        if horas_luz_minimas is None:
            raise ValueError('Necesario especificar la cantidad minima de horas de luz que tiene ' +
                             'que estar de la planta entre el valor minimo y maximo de luz.')
        if horas_luz_maximas is None:
            raise ValueError('Necesario especificar la cantidad maxima de horas de luz que tiene ' +
                             'que estar de la planta entre el valor minimo y maximo de luz.')
        if dias_germinacion is None:
            raise ValueError('Necesario especificar los dias que tarda en germinar la planta.')
        if dias_maduracion is None:
            raise ValueError('Necesario especificar los dias que tarda en madurar la planta.')
        if dias_marchitacion is None:
            raise ValueError('Necesario especificar los dias que tarda en marchitar la planta.')
        if descripcion is None:
            raise ValueError('Necesario especificar la descripcion de los cuidados de la planta.')

        nuevo_cuidado_tipo_planta = None
        try:
            nuevo_cuidado_tipo_planta = CuidadoTipoPlanta( tipo_planta, temperatura_minima, temperatura_maxima, unidad_temperatura,
                                                            humedad_ambiente_minima, humedad_ambiente_maxima, humedad_maceta_minima, 
                                                            humedad_maceta_maxima, humedad_suelo_minima, humedad_suelo_maxima, 
                                                            unidad_humedad, luz_minima, luz_maxima, unidad_luz, horas_luz_minimas, 
                                                            horas_luz_maximas, dias_germinacion, dias_maduracion, dias_marchitacion,
                                                            descripcion)
            session.add(nuevo_cuidado_tipo_planta)
            session.commit()
        except IntegrityError as ex:
            session.rollback()
            raise ErrorTipoPlantaExiste(
                'El cuidado de tipo de planta ' + str(tipo_planta) + ' ya está registrado.'
                ) from ex
        finally:
            return nuevo_cuidado_tipo_planta

    @staticmethod
    def listAll(session: Session) -> List[CuidadoTipoPlanta]:
        """
        istado de tipos de plantas

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[TipoPlanta]: Lista de registros de tipos de plantas.
        """
        query = session.query(CuidadoTipoPlanta)
        return query.all()

    @staticmethod
    def get(session: Session, tipo_planta: str) -> Optional[CuidadoTipoPlanta]:
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
        cuidado_tipo_planta: CuidadoTipoPlanta = None
        try:
            query = session.query(CuidadoTipoPlanta).filter_by(tipo_planta=tipo_planta)
            cuidado_tipo_planta: CuidadoTipoPlanta = query.one()
        except NoResultFound as ex:
            raise ErrorTipoPlantaNoExiste(
                'El tipo de planta con el nombre' + tipo_planta + 'no existe'
                ) from ex
        finally:
            return cuidado_tipo_planta

    @staticmethod
    def update(session: Session, tipo_planta:str, temperatura_minima:float, temperatura_maxima:float, unidad_temperatura:UnidadMedida,
      humedad_ambiente_minima:float, humedad_ambiente_maxima:float, humedad_maceta_minima:float, humedad_maceta_maxima:float, 
      humedad_suelo_minima:float, humedad_suelo_maxima:float, unidad_humedad: UnidadMedida, luz_minima:float, luz_maxima:float, 
      unidad_luz:UnidadMedida, horas_luz_minimas:float, horas_luz_maximas:float, dias_germinacion:int, dias_maduracion:int,
      dias_marchitacion:int, descripcion: str) -> CuidadoTipoPlanta:
        """
        Modificacion de un cuidado de un tipo de planta.

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_planta (str): Tipo de planta.
            - temperatura_minima: (float): 
            - temperatura_maxima (float): 
            - unidad_temperatura (UnidadMedida): 
            - humedad_ambiente_minima (float):  
            - humedad_ambiente_maxima (float):  
            - humedad_maceta_minima (float):  
            - humedad_maceta_maxima (float): 
            - humedad_suelo_minima (float):  
            - humedad_suelo_maxima (float):  
            - unidad_humedad (UnidadMedida): 
            - luz_minima (float):  
            - luz_maxima (float): 
            - unidad_luz (UnidadMedida): 
            - horas_luz_minimas (float): 
            - horas_luz_maximas (float): 
            - dias_germinacion (int): Numero de dias que tarda en germinar la planta desde su plantacion
            - dias_maduracion (int): Numero de dias que tarda en madurar la planta desde su plantacion
            - dias_marchitacion (int):  Numero de dias que tarda en marchitar la planta desde su plantacion
            - descripcion (str): Descripcion de los cuidados del tipo de planta

            

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if tipo_planta is None:
            raise ValueError('Necesario especificar el tipo de la planta.')
        if temperatura_minima is None:
            raise ValueError('Necesario especificar la temperatura minima de la planta.')
        if temperatura_maxima is None:
            raise ValueError('Necesario especificar la temperatura maxima de la planta.')
        if unidad_temperatura is None:
            raise ValueError('Necesario especificar la unidad de temperatura de la planta.')
        if humedad_ambiente_minima is None:
            raise ValueError('Necesario especificar la humedad minima del ambiente de la planta.')
        if humedad_ambiente_maxima is None:
            raise ValueError('Necesario especificar la humedad maxima del ambiente de la planta.')
        if humedad_maceta_minima is None:
            raise ValueError('Necesario especificar la humedad minima de la maceta de la planta.')
        if humedad_maceta_maxima is None:
            raise ValueError('Necesario especificar la humedad maxima de la maceta de la planta.')
        if humedad_suelo_minima is None:
            raise ValueError('Necesario especificar la humedad minima del suelo de la planta.')
        if humedad_suelo_maxima is None:
            raise ValueError('Necesario especificar la humedad maxima del suelo de la planta.')
        if unidad_humedad is None:
            raise ValueError('Necesario especificar la unidad de humedad de la planta.')
        if luz_minima is None:
            raise ValueError('Necesario especificar la cantidad minima de luz de la planta.')
        if luz_maxima is None:
            raise ValueError('Necesario especificar la cantidad maxima de luz de la planta.')
        if unidad_luz is None:
            raise ValueError('Necesario especificar la unidad de luz de la planta.')
        if horas_luz_minimas is None:
            raise ValueError('Necesario especificar la cantidad minima de horas de luz que tiene ' +
                             'que estar de la planta entre el valor minimo y maximo de luz.')
        if horas_luz_maximas is None:
            raise ValueError('Necesario especificar la cantidad maxima de horas de luz que tiene ' +
                             'que estar de la planta entre el valor minimo y maximo de luz.')
        if dias_germinacion is None:
            raise ValueError('Necesario especificar los dias que tarda en germinar la planta.')
        if dias_maduracion is None:
            raise ValueError('Necesario especificar los dias que tarda en madurar la planta.')
        if dias_marchitacion is None:
            raise ValueError('Necesario especificar los dias que tarda en marchitar la planta.')
        if descripcion is None:
            raise ValueError('Necesario especificar la descripcion de los cuidados de la planta.')

        cuidado_tipo_planta_modificado = None
        try:
            query = session.query(CuidadoTipoPlanta).filter_by(tipo_planta=tipo_planta)
            cuidado_tipo_planta: CuidadoTipoPlanta = query.one()
            # if tipo_planta.descripcion_planta != descripcion_planta:
            #     query.update({'descripcion_planta' : descripcion_planta})
            session.commit()
            cuidado_tipo_planta_modificado: CuidadoTipoPlanta = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorTipoPlantaNoExiste(
                'El cuidado del tipo de planta con el nombre' + tipo_planta + 'no existe.'
                ) from ex
        finally:
            return cuidado_tipo_planta_modificado
        
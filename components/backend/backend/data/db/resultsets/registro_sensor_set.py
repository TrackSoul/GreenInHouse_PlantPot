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
            - escala (str): Esala/unidad de medida asociada al valor
            - fecha (datetime): Fecha de creacion del registro

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
        nuevo_registro_sensor: RegistroSensor = None
        try:
            nuevo_registro_sensor = RegistroSensor(tipo_sensor, zona_sensor, numero_sensor, valor, escala, fecha)
            session.add(nuevo_registro_sensor)
            session.commit()
        except IntegrityError as ex:
            session.rollback()
            raise ErrorRegistroSensorExiste(
                'El registro ' + str(nuevo_registro_sensor.id_) + ' del sensor ' + str(nuevo_registro_sensor.numero_sensor) +
                  ' de ' +  nuevo_registro_sensor.tipo_sensor + ' de ' +  nuevo_registro_sensor.zona_sensor + 'ya existe.'
                ) from ex
        finally:
            return nuevo_registro_sensor

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
    def get(session: Session, id_: str) -> Optional[RegistroSensor]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): Objeto de sesion.
            - id_ (str): The question id_ to find
            
        Returns:
            - Optional[Pregunta]: The question 
        """
        if not id_:
            raise ValueError('An id_ is requiered.')
        registro_sensor: RegistroSensor = None
        try:
            query = session.query(RegistroSensor).filter_by(id_=id_)
            registro_sensor: RegistroSensor = query.one()
        except NoResultFound as ex:
            raise ErrorRegistroSensorNoExiste(
                'El registro de sensor con el id ' + id_ + ' no existe.'
                ) from ex
        finally:
            return registro_sensor

    @staticmethod
    def update(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               valor:float, escala:str, fecha: datetime, id_: str) -> RegistroSensor:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (str): Tipo de sensor.
            - numero_sensor (str): Numero de sensor.
            - valor (float): Valor de lectura del sensor.
            - escala (str): Esala/unidad de medida asociada al valor
            - fecha (datetime): Fecha de creacion del registro
            - id_ (int): Id del registro

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorRegistroSensorExiste: Si el registro del sensor ya existe.

        Returns:
            - Sensor: Registro creado del sensor.
        """
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo del sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero del sensor.')
        if not valor:
            raise ValueError('Necesario especificar el valor del registro del sensor.')
        if not escala:
            raise ValueError('Necesario especificar la escala del registro del sensor.')
        if not fecha:
            raise ValueError('Necesario especificar la fecha de creacion del registro del sensor')
        if not id_:
            raise ValueError('Necesario especificar el id del registro del sensor.')
        registro_sensor_modificado: RegistroSensor = None
        try:
            query = session.query(RegistroSensor).filter_by(id_=id_)
            registro_sensor: RegistroSensor = query.one()
            if registro_sensor.tipo_sensor != tipo_sensor:
                query.update({'tipo_sensor' : tipo_sensor})
            if registro_sensor.zona_sensor != zona_sensor:
                query.update({'zona_sensor' : zona_sensor})
            if registro_sensor.numero_sensor != numero_sensor:
                query.update({'numero_sensor' : numero_sensor})
            if registro_sensor.valor != valor:
                query.update({'valor' : valor})
            if registro_sensor.escala != escala:
                query.update({'escala' : escala})
            if registro_sensor.fecha != fecha:
                query.update({'fecha' : fecha})
            session.commit()
            registro_sensor_modificado: RegistroSensor = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorRegistroSensorNoExiste(
                'El registro de sensor con el id ' + id_ + ' no existe.'
                ) from ex
        finally:
            return registro_sensor_modificado


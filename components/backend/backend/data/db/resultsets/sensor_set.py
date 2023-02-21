from datetime import datetime
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from backend.data.db.results import Sensor
from backend.data.db.exc import ErrorSensorExiste, ErrorSensorNoExiste
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor

class SensorSet():
    """ 
    Clase responsable a nivel de tabla de las operaciones con los sensores.
    """
    @staticmethod
    def create(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               modelo_sensor: ModeloSensor, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int, 
               patilla_3_lectura:int, patilla_4_lectura:int, unidad_medida_1:str, unidad_medida_2:str,
               unidad_medida_3:str, unidad_medida_4:str, fecha_creacion:datetime ,fecha_eliminacion:datetime) -> Optional[Sensor]:              
        """
        Creacion de un nuevo sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.
            - modelo_sensor (ModeloSensor): modelo_sensor del sensor.
            - direccion_lectura (str): Direccion de lectura del sensor.
            - patilla_1_lectura (int): Patilla 1 de lectura del sensor.
            - patilla_2_lectura (int): Patilla 2 de lectura del sensor.
            - patilla_3_lectura (int): Patilla 3 de lectura del sensor.
            - patilla_4_lectura (int): Patilla 4 de lectura del sensor.
            - unidad_medida_1 (int): Unidad de medida de lectura 1 del sensor.
            - unidad_medida_2 (int): Unidad de medida de lectura 2 del sensor.
            - unidad_medida_3 (int): Unidad de medida de lectura 3 del sensor.
            - unidad_medida_4 (int): Unidad de medida de lectura 4 del sensor.
            - fecha_creacion (datetime): Fecha de creacion del sensor.
            - fecha_eliminacion (datetime): Fecha de eliminacion del sensor.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorSensorExiste: Si el sensor ya existe.

        Returns:
            - Sensor: Sensor creado.
        """
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        if not modelo_sensor:
            raise ValueError('Necesario especificar el modelo del sensor.')
        if not direccion_lectura and not patilla_1_lectura:
            raise ValueError('Necesario especificar la direccion o patilla de lectura del sensor.')
        nuevo_sensor = None
        try:
            nuevo_sensor = Sensor(tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                                  direccion_lectura, patilla_1_lectura, patilla_2_lectura, 
                                  patilla_3_lectura, patilla_4_lectura, unidad_medida_1, 
                                  unidad_medida_2, unidad_medida_3, unidad_medida_4, 
                                  fecha_creacion, fecha_eliminacion)
            session.add(nuevo_sensor)
            session.commit()
            
        except IntegrityError as ex:
            session.rollback()
            raise ErrorSensorExiste(
                'El sensor ' + str(numero_sensor) + ' de ' +  str(tipo_sensor) + ' de ' +  str(zona_sensor) + ' ya existe.'
                ) from ex
        finally:    
            return nuevo_sensor

    @staticmethod
    def listAll(session: Session) -> List[Sensor]:
        """
        Lista con todos los sensores.

        Args:
            - session (Session): Objeto de sesion.

        Returns:
            - List[Sensor]: Lista de sensores.
        """
        sensores = None
        query = session.query(Sensor)
        sensores: List[Sensor] = query.all()
        return sensores

    @staticmethod
    def get(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int,) -> Optional[Sensor]:
        """
        Obtencion de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorSensorNoExiste: Si el sensor no existe.

        Returns:
            - Optional[Sensor]: Sensor obtenido.
        """
        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        sensor = None
        try:
            query = session.query(Sensor).filter_by(tipo_sensor=tipo_sensor,zona_sensor=zona_sensor,numero_sensor=numero_sensor)
            sensor: Sensor = query.one()
        except NoResultFound as ex:
            raise ErrorSensorNoExiste(
                'El sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 'no existe.'
                ) from ex
        finally:
            return sensor

    @staticmethod
    def update(session: Session, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
               modelo_sensor:ModeloSensor, direccion_lectura:str, patilla_1_lectura:int, patilla_2_lectura:int, 
               patilla_3_lectura:int, patilla_4_lectura:int, unidad_medida_1:str, unidad_medida_2:str,
               unidad_medida_3:str, unidad_medida_4:str, fecha_creacion:datetime ,fecha_eliminacion:datetime) -> Optional[Sensor]:
        """
        Creacion de un nuevo registro de un sensor

        Nota:
            Realiza commit de la transaccion.

        Args:
            - session (Session): Objeto de sesion.
            - tipo_sensor (TipoSensor): Tipo de sensor.
            - zona_sensor (ZonaSensor): Zona del sensor.
            - numero_sensor (int): Numero de sensor.
            - modelo_sensor (ModeloSensor): modelo_sensor del sensor.
            - direccion_lectura (str): Direccion de lectura del sensor.
            - patilla_1_lectura (int): Patilla 1 de lectura del sensor.
            - patilla_2_lectura (int): Patilla 2 de lectura del sensor.
            - patilla_3_lectura (int): Patilla 3 de lectura del sensor.
            - patilla_4_lectura (int): Patilla 4 de lectura del sensor.
            - unidad_medida_1 (int): Unidad de medida de lectura 1 del sensor.
            - unidad_medida_2 (int): Unidad de medida de lectura 2 del sensor.
            - unidad_medida_3 (int): Unidad de medida de lectura 3 del sensor.
            - unidad_medida_4 (int): Unidad de medida de lectura 4 del sensor.
            - fecha_creacion (datetime): Fecha de creacion del sensor.
            - fecha_eliminacion (datetime): Fecha de eliminacion del sensor.

        Raises:
            - ValueError: Si no es proporcionado alguno de los datos necesarios.
            - ErrorSensorNoExiste: Si el sensor no existe.

        Returns:
            - Optional[Sensor]: Sensor modificado.
        """

        if not tipo_sensor:
            raise ValueError('Necesario especificar el tipo de sensor.')
        if not zona_sensor:
            raise ValueError('Necesario especificar la zona del sensor.')
        if not numero_sensor:
            raise ValueError('Necesario especificar el numero de sensor.')
        sensor_modificado = None
        sensor_modificado: Sensor = None
        try:
            query = session.query(Sensor).filter_by(tipo_sensor=tipo_sensor,zona_sensor=zona_sensor,numero_sensor=numero_sensor)
            sensor: Sensor = query.one()
            if sensor.modelo_sensor != modelo_sensor:
                query.update({'modelo_sensor' : modelo_sensor})
            if sensor.direccion_lectura != direccion_lectura:
                query.update({'direccion_lectura' : direccion_lectura})
            if sensor.patilla_1_lectura != patilla_1_lectura:
                query.update({'patilla_1_lectura' : patilla_1_lectura})
            if sensor.patilla_2_lectura != patilla_2_lectura:
                query.update({'patilla_2_lectura' : patilla_2_lectura})
            if sensor.patilla_3_lectura != patilla_3_lectura:
                query.update({'patilla_3_lectura' : patilla_3_lectura})
            if sensor.patilla_4_lectura != patilla_4_lectura:
                query.update({'patilla_4_lectura' : patilla_4_lectura})
            if sensor.unidad_medida_1 != unidad_medida_1:
                query.update({'unidad_medida_1' : unidad_medida_1})
            if sensor.unidad_medida_2 != unidad_medida_2:
                query.update({'unidad_medida_2' : unidad_medida_2})
            if sensor.unidad_medida_3 != unidad_medida_3:
                query.update({'unidad_medida_3' : unidad_medida_3})
            if sensor.unidad_medida_4 != unidad_medida_4:
                query.update({'unidad_medida_4' : unidad_medida_4})
            # if sensor.fecha_creacion != fecha_creacion:
                # query.update({'fecha_creacion' : fecha_creacion})
            if sensor.fecha_eliminacion != fecha_eliminacion:
                query.update({'fecha_eliminacion' : fecha_eliminacion})
            session.commit()
            sensor_modificado: Sensor = query.one() 
        except NoResultFound as ex:
            session.rollback()
            raise ErrorSensorNoExiste(
                'El sensor ' + str(numero_sensor) + ' de ' +  tipo_sensor + ' de ' +  zona_sensor + 'no existe.'
                ) from ex
        finally:
            return sensor_modificado

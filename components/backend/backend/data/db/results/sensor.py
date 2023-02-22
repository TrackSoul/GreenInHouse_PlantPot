from datetime import datetime
from typing import Dict, List, Optional
from sqlalchemy import Table, MetaData, Column, String, Enum, Integer, Boolean, Float, TIMESTAMP # type: ignore
from sqlalchemy import ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class Sensor(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                 modelo_sensor:ModeloSensor, direccion_lectura:str, patilla_1_lectura:int, 
                 patilla_2_lectura:int, patilla_3_lectura:int, patilla_4_lectura:int,
                 unidad_medida_1:UnidadMedida, unidad_medida_2:UnidadMedida, 
                 unidad_medida_3:UnidadMedida, unidad_medida_4:UnidadMedida, 
                 fecha_creacion:datetime ,fecha_eliminacion:datetime):
        self.tipo_sensor: TipoSensor = tipo_sensor
        self.zona_sensor: ZonaSensor = zona_sensor
        self.numero_sensor: int = numero_sensor
        self.modelo_sensor: ModeloSensor = modelo_sensor
        self.direccion_lectura: str = direccion_lectura
        self.patilla_1_lectura: int = patilla_1_lectura
        self.patilla_2_lectura: int = patilla_2_lectura
        self.patilla_3_lectura: int = patilla_3_lectura
        self.patilla_4_lectura: int = patilla_4_lectura
        self.unidad_medida_1: UnidadMedida = unidad_medida_1
        self.unidad_medida_2: UnidadMedida = unidad_medida_2
        self.unidad_medida_3: UnidadMedida = unidad_medida_3
        self.unidad_medida_4: UnidadMedida = unidad_medida_4
        self.fecha_creacion: datetime = fecha_creacion
        self.fecha_eliminacion: datetime = fecha_eliminacion

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ 
        Definicion de la tabla.
        Args:
            - metadata (MetaData): Metadatos del esquema de la base de datos
                        (usado para la definicion y mapeo de entidades)
        
        Returns:
            - Table: Objeto tabla con al definicion de la tabla.
        """
        return Table(
            'sensores',
            metadata,
            Column('tipo_sensor', Enum(TipoSensor), primary_key=True ),
            Column('zona_sensor', Enum(ZonaSensor), primary_key=True),
            Column('numero_sensor', Integer, primary_key=True),
            Column('modelo_sensor', Enum(ModeloSensor), nullable=False),
            Column('direccion_lectura', String(100), nullable=True),
            Column('patilla_1_lectura', Integer, nullable=True),
            Column('patilla_2_lectura', Integer, nullable=True),
            Column('patilla_3_lectura', Integer, nullable=True),
            Column('patilla_4_lectura', Integer, nullable=True),
            Column('unidad_medida_1', Enum(UnidadMedida), nullable=True),
            Column('unidad_medida_2', Enum(UnidadMedida), nullable=True),
            Column('unidad_medida_3', Enum(UnidadMedida), nullable=True),
            Column('unidad_medida_4', Enum(UnidadMedida), nullable=True),
            Column('fecha_creacion', TIMESTAMP, nullable=False ),
            Column('fecha_eliminacion', TIMESTAMP, nullable=True ),
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ 
        Obtiene el diccionario con las propiedades de mapeado.
        Returns:
            - Dict: Diccionario con las propiedades de mapeado.
        """
        return {}

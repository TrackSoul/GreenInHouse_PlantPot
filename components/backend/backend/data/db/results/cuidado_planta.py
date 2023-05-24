from datetime import datetimeunidad_temperatura
from typing import Dict, Optional
from sqlalchemy import Table, MetaData, Column, String, Boolean, Integer, Float, Enum # type: ignore
from sqlalchemy import ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase
from common.data.util import TipoMedida, UnidadMedida

class CuidadoTipoPlanta(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, tipo_planta:str, temperatura_minima:float, temperatura_maxima:float, unidad_temperatura:UnidadMedida,
      humedad_ambiente_minima:float, humedad_ambiente_maxima:float, humedad_maceta_minima:float, humedad_maceta_maxima:float, 
      humedad_suelo_minima:float, humedad_suelo_maxima:float, unidad_humedad: UnidadMedida, luz_minima:float, luz_maxima:float, 
      unidad_luz:UnidadMedida, horas_luz_minimas:float, horas_luz_maximas:float, dias_germinacion:int, dias_maduracion:int, 
      dias_marchitacion:int, descripcion: str):
        self.tipo_planta: str = tipo_planta
        self.temperatura_minima: float = temperatura_minima
        self.temperatura_maxima: float  = temperatura_maxima
        self.unidad_temperatura: UnidadMedida = unidad_temperatura,
        self.humedad_ambiente_minima: float = humedad_ambiente_minima
        self.humedad_ambiente_maxima: float  = humedad_ambiente_maxima
        self.humedad_maceta_minima: float = humedad_maceta_minima
        self.humedad_maceta_maxima: float  = humedad_maceta_maxima
        self.humedad_suelo_minima: float = humedad_suelo_minima
        self.humedad_suelo_maxima: float  = humedad_suelo_maxima
        self.unidad_humedad: UnidadMedida = unidad_humedad,
        self.luz_minima: float = luz_minima
        self.luz_maxima: float  = luz_maxima
        self.unidad_luz: UnidadMedida = unidad_luz,
        self.horas_luz_minimas: float = horas_luz_minimas
        self.horas_luz_maximas: float  = horas_luz_maximas
        self.dias_germinacion: int = dias_germinacion
        self.dias_maduracion: int = dias_maduracion
        self.dias_marchitacion: int = dias_marchitacion
        self.descripcion: str = descripcion


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
            #str(self.tipo_sensor + str(self.numero_sensor)),
            'cuidados_tipos_plantas',
            metadata,
            Column('tipo_planta', String(100), ForeignKey('tipos_plantas.tipo_planta'), primary_key=True ),
            Column('temperatura_minima', Float, nullable=False ),
            Column('temperatura_maxima', Float, nullable=False ),
            Column('unidad_temperatura', Enum(UnidadMedida), nullable=False ),
            Column('humedad_ambiente_minima', Float, nullable=False ),
            Column('humedad_ambiente_maxima', Float, nullable=False ),
            Column('humedad_maceta_minima', Float, nullable=False ),
            Column('humedad_maceta_maxima', Float, nullable=False ),
            Column('humedad_suelo_minima', Float, nullable=False ),
            Column('humedad_suelo_maxima', Float, nullable=False ),
            Column('unidad_humedad', Enum(UnidadMedida), nullable=False ),
            Column('luz_minima', Float, nullable=False ),
            Column('luz_maxima', Float, nullable=False ),
            Column('unidad_luz', Enum(UnidadMedida), nullable=False ),
            Column('horas_luz_minimas', Float, nullable=False ),
            Column('horas_luz_maximas', Float, nullable=False ),
            Column('dias_germinacion', Integer, nullable=False ),
            Column('dias_maduracion', Integer, nullable=False ),
            Column('dias_marchitacion', Integer, nullable=False ),
            Column('descripcion', String(500), nullable=False ),
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ 
        Obtiene el diccionario con las propiedades de mapeado.
        Returns:
            - Dict: Diccionario con las propiedades de mapeado.
        """
        return {
        }
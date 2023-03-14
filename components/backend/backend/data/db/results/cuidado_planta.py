from datetime import datetime
from typing import Dict, Optional
from sqlalchemy import Table, MetaData, Column, String, Boolean, Integer, Float # type: ignore
from sqlalchemy import ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase

class CuidadoPlanta(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, tipo_planta:str, temperatura_minima:float, temperatura_maxima:float, escala_temperatura:str,
      humedad_ambiente_minima:float, humedad_ambiente_maxima:float, humedad_maceta_minima:float, humedad_maceta_maxima:float, 
      humedad_suelo_minima:float, humedad_suelo_maxima:float, escala_humedad:str, luz_minima:float, luz_maxima:float, 
      escala_luz:str, horas_luz_minimas:float, horas_luz_maximas:float, dia_inicio:int, dia_final:float):
        self.id: int
        self.tipo_planta: str = tipo_planta
        self.temperatura_minima: float = temperatura_minima
        self.temperatura_maxima: float  = temperatura_maxima
        self.escala_temperatura:str = escala_temperatura,
        self.humedad_ambiente_minima: float = humedad_ambiente_minima
        self.humedad_ambiente_maxima: float  = humedad_ambiente_maxima
        self.humedad_maceta_minima: float = humedad_maceta_minima
        self.humedad_maceta_maxima: float  = humedad_maceta_maxima
        self.humedad_suelo_minima: float = humedad_suelo_minima
        self.humedad_suelo_maxima: float  = humedad_suelo_maxima
        self.escala_humedad:str = escala_humedad,
        self.luz_minima: float = luz_minima
        self.luz_maxima: float  = luz_maxima
        self.escala_luz:str = escala_luz,
        self.horas_luz_minimas: float = horas_luz_minimas
        self.horas_luz_maximas: float  = horas_luz_maximas
        self.dia_inicio: int = dia_inicio
        self.dia_final: int = dia_final


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
            'cuidados_plantas',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('nombre_planta', String(100), primary_key=True),
            Column('tipo_planta', String(100), ForeignKey('tipos_plantas.tipo_planta'), nullable=False ),
            Column('temperatura_minima', Float, nullable=False ),
            Column('temperatura_maxima', Float, nullable=False ),
            Column('escala_temperatura', String, nullable=False ),
            Column('humedad_ambiente_minima', Float, nullable=False ),
            Column('humedad_ambiente_maxima', Float, nullable=False ),
            Column('humedad_maceta_minima', Float, nullable=False ),
            Column('humedad_maceta_maxima', Float, nullable=False ),
            Column('humedad_suelo_minima', Float, nullable=False ),
            Column('humedad_suelo_maxima', Float, nullable=False ),
            Column('escala_humedad', String, nullable=False ),
            Column('luz_minima', Float, nullable=False ),
            Column('luz_maxima', Float, nullable=False ),
            Column('escala_luz', String, nullable=False ),
            Column('horas_luz_minimas', Float, nullable=False ),
            Column('horas_luz_maximas', Float, nullable=False ),
            Column('dia_inicio', Integer, nullable=False ),
            Column('dia_final', Integer, nullable=False ),
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
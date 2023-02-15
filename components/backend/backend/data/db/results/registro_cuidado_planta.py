from datetime import datetime
from typing import Dict, Optional
from sqlalchemy import Table, MetaData, Column, String, Boolean # type: ignore
from sqlalchemy import ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase

class RegistroCuidadoPlanta(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, tipo_planta:str, ):
        self.id: int
        self.tipo_planta: str = tipo_planta
        self.temperatura_minima: float = temperatura_minima
        self.temperatura_maxima: float  = temperatura_maxima
        self.humedad_ambiente_minima: float = humedad_ambiente_minima
        self.humedad_ambiente_maxima: float  = humedad_ambiente_maxima
        self.humedad_maceta_minima: float = humedad_maceta_minima
        self.humedad_maceta_maxima: float  = humedad_maceta_maxima
        self.humedad_suelo_minima: float = humedad_suelo_minima
        self.humedad_suelo_maxima: float  = humedad_suelo_maxima
        self.luz_minima: float = luz_minima
        self.luz_maxima: float  = luz_maxima
        self.horas_luz_minima: float = horas_luz_minima
        self.horas_luz_maxima: float  = horas_luz_maxima
        self.dia_inicio: int = dia_inicio
        self.dia_final: int = dia_inicio


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
            'plantas',
            metadata,
            Column('nombre_planta', String(100), primary_key=True),
            Column('tipo_planta', String(100), ForeignKey('tipos_plantas.tipo_planta'), nullable=False ),
            Column('viva', Boolean, nullable=False ),
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ 
        Obtiene el diccionario con las propiedades de mapeado.
        Returns:
            - Dict: Diccionario con las propiedades de mapeado.
        """
        return {
            #'registro_sensores': relationship(RegistroSensor, backref='nombre_planta')
        }
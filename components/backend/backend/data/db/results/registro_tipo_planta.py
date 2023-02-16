from datetime import datetime
from typing import Dict, Optional
from sqlalchemy import Table, MetaData, Column, String, Boolean # type: ignore
from sqlalchemy import ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase

class RegistroTipoPlanta(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, tipo_planta:str, descripcion_planta:str,):
        self.tipo_planta: str = tipo_planta
        self.descripcion_planta: str = descripcion_planta

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
            'registros_tipos_plantas',
            metadata,
            Column('tipo_planta', String(100), primary_key=True),
            Column('descripcion_planta', String(500), nullable=False )
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

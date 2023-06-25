""" 
Modulo ResultBase.
"""
#Author: Oscar Valverde Escobar

from abc import ABC, abstractmethod
from typing import Dict
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import registry


class ModuloBase(ABC):
    """ 
    Clase base para todas las clase de registro de la base de datos
    """

    @classmethod
    def map(cls: type, esquema_db: registry) -> None:
        """
        Mapeado de los registros de las instancias en la base de datos

        Args:
            - cls (type): Esta clase
            - schema_registry (registry): Una generalizacion de registry para mapear las clases
        """
        esquema_db.map_imperatively(
            cls,
            cls._table_definition(esquema_db.metadata),
            properties=cls._mapping_properties()
        )

    @staticmethod
    @abstractmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ 
        Definicion de la tabla.
        Args:
            - metadata (MetaData): Metadatos del esquema de la base de datos
                        (usado para la definicion y mapeo de entidades)
        
        Returns:
            - Table: Objeto tabla con al definicion de la tabla.
        """

    @staticmethod
    def _mapping_properties() -> Dict:
        """ 
        Obtiene el diccionario con las propiedades de mapeado.
        Returns:
            - Dict: Diccionario con las propiedades de mapeado.
        """
        return {}

from datetime import datetimeunidad_temperatura
from typing import Dict, Optional
from sqlalchemy import Table, MetaData, Column, String, Boolean, Integer, Float, Enum # type: ignore
from sqlalchemy import ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase
from common.data.util import ZonaSensor, TipoMedida, UnidadMedida

class ConsejoTipoPlanta(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, descripcion: str, tipo_planta:str, zona_consejo:ZonaSensor,
                 tipo_medida:TipoMedida, unidad_medida:UnidadMedida, valor_minimo:float, 
                 valor_maximo:float, horas_minimas:float, horas_maximas:float):
        self.descripcion: str = descripcion
        self.tipo_planta: str = tipo_planta
        self.zona_consejo: ZonaSensor = zona_consejo
        self.tipo_medida: TipoMedida = tipo_medida       
        self.unidad_medida: UnidadMedida = unidad_medida,
        self.valor_minimo: float = valor_minimo
        self.valor_maximo: float  = valor_maximo
        self.horas_minimas: float = horas_minimas
        self.horas_maximas: float  = horas_maximas

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
            'consejos_tipos_plantas',
            metadata,
            Column('descripcion', String(500), nullable=False ),
            Column('tipo_planta', String(100), ForeignKey('tipos_plantas.tipo_planta'), primary_key=True ),
            Column('zona_consejo', Enum(ZonaSensor), primary_key=True),
            Column('tipo_medida', Enum(TipoMedida), primary_key=True ),
            Column('unidad_medida', Enum(UnidadMedida), nullable=False ),
            Column('valor_minimo', Float, nullable=False ),
            Column('valor_maximo', Float, nullable=False ),
            Column('horas_minimas', Float, nullable=True ),
            Column('horas_maximas', Float, nullable=True ),
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
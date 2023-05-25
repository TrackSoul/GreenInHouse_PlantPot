from datetime import datetime
from typing import Dict, Optional
from sqlalchemy import Table, MetaData, Column, String, Enum, Integer, Float, TIMESTAMP # type: ignore
from sqlalchemy import ForeignKey, ForeignKeyConstraint  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from backend.data.db.results import ModuloBase
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida

class RegistroSensor(ModuloBase):
    """ 
    Definicion y almacenamiento de los registros del sensor.
    """

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                 valor:float, unidad_medida: UnidadMedida, fecha: datetime):
        self.id_: int
        self.tipo_sensor: TipoSensor = tipo_sensor
        self.zona_sensor: ZonaSensor = zona_sensor
        self.numero_sensor: int = numero_sensor
        self.valor: float = valor   
        self.unidad_medida: UnidadMedida = unidad_medida     
        self.fecha: datetime = fecha

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
            'registros_sensores',
            metadata,
            Column('id_', Integer, autoincrement='auto', primary_key=True),
            Column('tipo_sensor', Enum(TipoSensor), nullable=False ),
            Column('zona_sensor', Enum(ZonaSensor), nullable=False ),
            Column('numero_sensor', Integer, nullable=False),
            Column('valor', Float, nullable=False),
            Column('unidad_medida', Enum(UnidadMedida), nullable=False),
            Column('fecha', TIMESTAMP, nullable=False),
            ForeignKeyConstraint(['tipo_sensor','zona_sensor','numero_sensor'],
                                 ['sensores.tipo_sensor','sensores.zona_sensor','sensores.numero_sensor']),
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ 
        Obtiene el diccionario con las propiedades de mapeado.
        Returns:
            - Dict: Diccionario con las propiedades de mapeado.
        """
        return {}

    # def toJson(self) -> Dict:
    #     dict={}
    #     dict["id_"]=self.id_
    #     dict["tipo_sensor"]=self.tipo_sensor
    #     dict["zona_sensor"]=self.zona_sensor
    #     dict["numero_sensor"]=self.numero_sensor
    #     dict["valor"]=self.valor
    #     dict["unidad_medida"]=self.unidad_medida
    #     dict["fecha"]=self.getFecha()#.isoformat()
    #     return dict

    # @staticmethod
    # def fromJson(dict: dict):
    #     sensor = RegistroSensor(dict["id_"],dict["tipo_sensor"],dict["zona_sensor"],dict["numero_sensor"],
    #                             dict["valor"],dict["unidad_medida"], dict["fecha"])
    #     return sensor
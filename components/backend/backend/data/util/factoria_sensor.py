from datetime import datetime
from typing import Optional,Dict,List
from enum import Enum
from backend.service import SensorService
from backend.data.util import Sensor as SensorBackend
from common.data.util import Sensor as SensorCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class FactoriaSensor ():

    __diccionario_sensores: Dict[SensorBackend]

    def __init(self):
        if  self.__diccionario_sensores == None:
            self.__diccionario_sensores = {}
        lista_sensores: List[SensorBackend] = SensorService.listAll()



    @staticmethod
    def getSensor():

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                 modelo_sensor:ModeloSensor, direccion_lectura:str=None, patilla_0_lectura:int=None, 
                 patilla_1_lectura:int=None, patilla_2_lectura:int=None, patilla_3_lectura:int=None,                 
                 unidad_medida_0: UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_1:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                 unidad_medida_2: UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_3:UnidadMedida = UnidadMedida.SIN_UNIDAD,
                 fecha_creacion:datetime=None ,fecha_eliminacion:datetime=None):
        pass()
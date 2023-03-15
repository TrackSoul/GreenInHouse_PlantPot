from datetime import datetime
from typing import Optional,Dict,List, Tuple
from enum import Enum
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class SensorElectronico ():

    #def __init__(self):
    #    pass

    @staticmethod
    def leer_sensor(self, direccion_lectura:str=None, patilla_0_lectura:int=None, patilla_1_lectura:int=None,
                    patilla_2_lectura:int=None, patilla_3_lectura:int=None,) -> List[Tuple[float, UnidadMedida]]:
        lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]] = [[0.0,UnidadMedida.OTRO]]
        return lista_valor_unidad_medida
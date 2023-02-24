from datetime import datetime
from typing import Optional,Dict,List,Tuple
from enum import Enum
from common.data.util import Sensor as SensorCommon, RegistroSensor as RegistroSensorCommon
from common.data.util import TipoSensor, ZonaSensor, ModeloSensor, TipoMedida, UnidadMedida

class Sensor (SensorCommon):

    def __init__(self, tipo_sensor:TipoSensor, zona_sensor: ZonaSensor ,numero_sensor:int, 
                 modelo_sensor:ModeloSensor, direccion_lectura:str=None, patilla_0_lectura:int=None, 
                 patilla_1_lectura:int=None, patilla_2_lectura:int=None, patilla_3_lectura:int=None,                 
                 unidad_medida_0: UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_1:UnidadMedida = UnidadMedida.SIN_UNIDAD, 
                 unidad_medida_2: UnidadMedida = UnidadMedida.SIN_UNIDAD, unidad_medida_3:UnidadMedida = UnidadMedida.SIN_UNIDAD,
                 fecha_creacion:datetime=None ,fecha_eliminacion:datetime=None):

        super().__init__(tipo_sensor, zona_sensor, numero_sensor, modelo_sensor, 
                 direccion_lectura, patilla_0_lectura, patilla_1_lectura, patilla_2_lectura, 
                 patilla_3_lectura, unidad_medida_0, unidad_medida_1, unidad_medida_2, unidad_medida_3,                
                 fecha_creacion, fecha_eliminacion)
        #print(self.getCode())
        #self.__electronica_sensor: 
        
    # TODO
    # Crear factoria de sensores que genere un objeto con el que leer el sensor especipfico
    # y que conozca ya su modelo, para saber como leer dicho sensor
    #

    #def leerSensor() -> List[List[float, str]]:

    def crearRegistroSensor(self, valor: float, unidad_medida: UnidadMedida) -> RegistroSensorCommon:
        return RegistroSensorCommon(self.getTipoSensor(),self.getZonaSensor(),self.getNumeroSensor(),valor,unidad_medida)

    def crearRegistrosSensor(self, lista_valor_unidad_medida: List[Tuple[float, UnidadMedida]]) -> List[RegistroSensorCommon]:
        lista_registros_sensor  = []
        for registro_sensor in lista_registros_sensor:
            lista_registros_sensor.append(self.crearRegistroSensor(registro_sensor[0],registro_sensor[1]))
        return lista_registros_sensor

    #def leerSesnorYCrearRegistroSensor()
     


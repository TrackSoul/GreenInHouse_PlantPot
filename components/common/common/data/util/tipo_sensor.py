""" 
Enumeracion de tipos de sensores.
"""

from enum import Enum

class TipoSensor(Enum):
    """ 
    Enumeracion con los tipos de sensores
    """
    HUMEDAD = 1
    TEMPERATURA = 2
    TEMPERATURA_Y_HUMEDAD = 3
    LUZ = 4
    OTRO = 99
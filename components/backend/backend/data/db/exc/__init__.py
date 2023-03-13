""" Questions  database-related exceptions.
"""

from .error_sensor_existe import ErrorSensorExiste
from .error_sensor_no_existe import ErrorSensorNoExiste
from .error_registro_sensor_existe import ErrorRegistroSensorExiste
from .error_registro_sensor_no_existe import ErrorRegistroSensorNoExiste
from backend.data.db.exc.error_planta_existe import ErrorPlantaExiste
from backend.data.db.exc.error_planta_no_existe import ErrorPlantaNoExiste
from backend.data.db.exc.error_tipo_planta_existe import ErrorTipoPlantaExiste
from backend.data.db.exc.error_tipo_planta_no_existe import ErrorTipoPlantaNoExiste
from backend.data.db.exc.error_sensor_planta_existe import ErrorSensorPlantaExiste
from backend.data.db.exc.error_sensor_planta_no_existe import ErrorSensorPlantaNoExiste
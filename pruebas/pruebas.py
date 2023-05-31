from datetime import datetime
import arrow
# from http import HTTPStatus
# from flask import current_app
# from typing import List, Dict
# from backend.service import RegistroSensorService, SensorService, PlantaService, ConsejoPlantaService, ConsejoTipoPlantaService
# from common.data.util import RegistroSensor as RegistroSensorCommon, Sensor as SensorCommon, Planta as PlantaCommon
# from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida
# from common.data.util import ConsejoPlanta as ConsejoPlantaCommon, ConsejoTipoPlanta as ConsejoTipoPlantaCommon, Consejo as ConsejoCommon



# def __agroupRecordsListOnIntervals(lista_registros_sensores: List[RegistroSensorCommon], dias: int, fecha: datetime = datetime.now() ) -> List[RegistroSensorCommon]:
#     fecha_fin = arrow.get(fecha)
#     fecha_inicio: arrow = None
#     if(dias==1):
#         fecha_inicio = fecha_fin.shift(days=-dias).ceil("hours")
#         intervalos_dia = 24
#     if(dias>1):
#         fecha_inicio = fecha_fin.shift(days=-dias).ceil("days")
#         intervalos_dia = 4
#         if dias > 7:
#             intervalos_dia = 2
#         if dias > 14:
#             intervalos_dia = 1
#     horas_intervalo = 24/intervalos_dia
#     arrow.Arrow.span_range('hour', fecha_inicio, fecha_fin)
#     intervalos = dias * intervalos_dia
#     # fecha = fecha_inicio   
#     # lista_fechas = []
#     # while fecha < fecha_fin:
#     #     lista_fechas.append(fecha)
#     #     fecha.shift(hours=+horas_intervalo)

if __name__ == '__main__':
    dias=1
    fecha: datetime = datetime.now()

    fecha_fin: arrow = arrow.get(fecha)
    fecha_inicio: arrow = None
    if(dias==1):
        fecha_inicio = fecha_fin.shift(days=-dias).ceil("hours")
        intervalos_dia = 24
    if(dias>1):
        fecha_inicio = fecha_fin.shift(days=-dias).ceil("days")
        intervalos_dia = 4
        if dias > 7:
            intervalos_dia = 2
        if dias > 14:
            intervalos_dia = 1
    horas_intervalo = 24/intervalos_dia
    # intervalos = dias * intervalos_dia
    f_int: arrow = fecha_inicio   
    lista_fechas = []
    while f_int < fecha_fin:
        lista_fechas.append((f_int.datetime,f_int.shift(hours=+horas_intervalo).datetime))
        # lista_fechas.append(f_int.datetime)
        f_int = f_int.shift(hours=+horas_intervalo)
    # lista_fechas.append(fecha_fin.datetime) 
    print(lista_fechas)
    print(lista_fechas[0])
    print(lista_fechas[-1])
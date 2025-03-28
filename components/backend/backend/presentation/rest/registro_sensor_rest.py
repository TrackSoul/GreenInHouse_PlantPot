#Author: Oscar Valverde Escobar

from datetime import datetime
import arrow
from http import HTTPStatus
from flask import current_app
from typing import List, Dict
from backend.service import RegistroSensorService, SensorService, PlantaService, ConsejoPlantaService, ConsejoTipoPlantaService
from common.data.util import RegistroSensor as RegistroSensorCommon, Sensor as SensorCommon, Planta as PlantaCommon
from common.data.util import TipoSensor, ZonaSensor, TipoMedida, UnidadMedida
from common.data.util import ConsejoPlanta as ConsejoPlantaCommon, ConsejoTipoPlanta as ConsejoTipoPlantaCommon, Consejo as ConsejoCommon

import traceback

def get(rsid: int) -> Dict:
    with current_app.app_context() :
        if RegistroSensorService.exists(current_app.db,rsid):
            return RegistroSensorService.get(current_app.db, rsid).toJson(), HTTPStatus.OK.value
        else:
            return ("El registro de sensor " + str(rsid) + "no existe", HTTPStatus.NOT_FOUND.value)
        
def getAll() -> List[Dict]:
    with current_app.app_context() :
        return [item.toJson() for item in RegistroSensorService.listAll(current_app.db)], HTTPStatus.OK.value

def getAllFromSensor(st:str, sz: str ,sid:int) -> List[Dict]:
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    with current_app.app_context() :
        if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in RegistroSensorService.listAllFromSensor(current_app.db,tipo_sensor,zona_sensor,numero_sensor)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)

def getAllFromSensorBetweenDates(st:str, sz: str ,sid:int, fi: str, ff: str = None) -> List[Dict]:
    try:
        tipo_sensor:TipoSensor = TipoSensor[st]
    except(KeyError):
        return ("El tipo de sensor " + str(st) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    try:
        zona_sensor: ZonaSensor = ZonaSensor[sz]
    except(KeyError):
        return ("La zona de sensor " + str(sz) + " no existe.", HTTPStatus.NOT_ACCEPTABLE.value)   
    numero_sensor:int = sid
    try:
        fecha_inicio=datetime.fromisoformat(fi)
    except(ValueError):
        return ("Error en el formato de la fecha de inicio " + str(fi) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        if ff is None:
            ff=str(datetime.now())
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio " + str(fi) + " no puede ser mayor que la fecha de fin " + str(ff) + " .", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if SensorService.exists(current_app.db,tipo_sensor,zona_sensor,numero_sensor):
            return [item.toJson() for item in RegistroSensorService.listAllFromSensorBetweenDates(current_app.db,tipo_sensor,zona_sensor,numero_sensor,
                                                                                                    fecha_inicio,fecha_fin)], HTTPStatus.OK.value
        else:
            return ("El sensor " + str(numero_sensor) + " de tipo " + str(tipo_sensor) + " de la zona " + str(zona_sensor) + " no existe", HTTPStatus.NOT_FOUND.value)

def getAllFromPlant(np:str) -> List[Dict]:
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            return [item.toJson() for item in RegistroSensorService.listAllFromPlant(current_app.db, nombre_planta)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)

def getAllFromPlantBetweenDates(np:str, fi: str, ff: str = None) -> List[Dict]:
    try:
        fecha_inicio=datetime.fromisoformat(fi)
    except(ValueError):
        return ("Error en el formato de la fecha de inicio " + str(fi) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        if ff is None:
            ff=str(datetime.now())
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio " + str(fi) + " no puede ser mayor que la fecha de fin " + str(ff) + " .", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            return [item.toJson() for item in RegistroSensorService.listAllFromPlantBetweenDates(current_app.db, nombre_planta, fecha_inicio, fecha_fin)], HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)   

def __createRecordsDcitToGraph() -> List[Dict]:
    dic_registros_graficar = {}
    for unidad_medida in list(UnidadMedida):
        tipo_medida: TipoMedida = unidad_medida.getTipoMedida()
        dic_tipo = {}
        for zona in list(ZonaSensor):
            dic_tipo_zona = {} 
            dic_tipo_zona["unidad_medida"] = {"nombre": str(unidad_medida),
                                            "tipo": unidad_medida.getTipo()}
            dic_tipo_zona["tipo_medida"] = {"nombre": str(tipo_medida),
                                            "tipo": tipo_medida.getTipo()}
            dic_tipo_zona["zona_sensor"] = {"nombre": str(zona),
                                    "tipo": zona.getTipo()}  
            dic_tipo_zona["lista_valores_medios"] = []
            dic_tipo_zona["lista_valores"] = []
            dic_tipo_zona["lista_fechas_largas"] = []
            dic_tipo_zona["lista_fechas_cortas"] = []
            dic_tipo[zona.getTipo()] = dic_tipo_zona 
        dic_registros_graficar[tipo_medida.getTipo()] = dic_tipo
    for zona in list(ZonaSensor):
        dic_zona = {}
        for unidad_medida in list(UnidadMedida):
            tipo_medida: TipoMedida = unidad_medida.getTipoMedida()           
            dic_zona_tipo = {}   
            dic_zona_tipo["unidad_medida"] = {"nombre": str(unidad_medida),
                                            "tipo": unidad_medida.getTipo()}
            dic_zona_tipo["tipo_medida"] = {"nombre": str(tipo_medida),
                                            "tipo": tipo_medida.getTipo()}
            dic_zona_tipo["zona_sensor"] = {"nombre": str(zona),
                                    "tipo": zona.getTipo()}  
            dic_zona_tipo["lista_valores_medios"] = []
            dic_zona_tipo["lista_valores"] = []
            dic_zona_tipo["lista_fechas_largas"] = []
            dic_zona_tipo["lista_fechas_cortas"] = []
            dic_zona[tipo_medida.getTipo()] = dic_zona_tipo
        dic_registros_graficar[zona.getTipo()] = dic_zona 
    return dic_registros_graficar

def __addAllRecordsListToGraph(lista_registros_sensores: List[RegistroSensorCommon], dic_registros_graficar, agrupar_multiples_sensores_con_misma_funcion=True) -> List[Dict]:
    for registro_sensor in lista_registros_sensores:
        unidad_medida: UnidadMedida = registro_sensor.getUnidadMedida()
        tipo_medida: TipoMedida = unidad_medida.getTipoMedida()
        zona: ZonaSensor = registro_sensor.getZonaSensor()
        # if registro_sensor.getValor() == -100:
        if zona == ZonaSensor.SIN_ZONA or tipo_medida == TipoMedida.SIN_TIPO:
            continue
        # Zona - Tipo unidad
        dic_tipo: Dict = dic_registros_graficar.get(tipo_medida.getTipo())
        dic_tipo_zona: Dict = dic_tipo.get(zona.getTipo())                  
        lista_valores_medios: List = dic_tipo_zona.get("lista_valores_medios")
        lista_valores: List = dic_tipo_zona.get("lista_valores")
        lista_fechas_largas: List = dic_tipo_zona.get("lista_fechas_largas")
        lista_fechas_cortas: List = dic_tipo_zona.get("lista_fechas_cortas")
        if agrupar_multiples_sensores_con_misma_funcion == True and len(lista_fechas_largas) > 0 and lista_fechas_largas[-1] == str(registro_sensor.getFecha()):
            if registro_sensor.getValor() != -999:
                if lista_valores_medios[-1] != -999:
                    lista_valores[-1].append(round(registro_sensor.getValor()))
                    lista_valores_medios[-1] = sum(lista_valores[-1])/len(lista_valores[-1])
                else:
                    lista_valores[-1]=[(round(registro_sensor.getValor()))]
                    lista_valores_medios[-1]=(round(registro_sensor.getValor()))
        else:
            lista_valores.append([round(registro_sensor.getValor())])
            lista_valores_medios.append(round(registro_sensor.getValor()))
            lista_fechas_largas.append(str(registro_sensor.getFecha()))
            #lista_fechas_cortas.append(str(registro_sensor.getFecha()))
            lista_fechas_cortas.append(str(registro_sensor.getFecha().strftime("%d/%m-%H:%M")))
        # Tipo unidad - Zona
        dic_zona: Dict = dic_registros_graficar.get(zona.getTipo())
        dic_zona_tipo: Dict = dic_zona.get(tipo_medida.getTipo())
        lista_valores_medios: List = dic_zona_tipo.get("lista_valores_medios")
        lista_valores: List = dic_zona_tipo.get("lista_valores")
        lista_fechas_largas: List = dic_zona_tipo.get("lista_fechas_largas")
        lista_fechas_cortas: List = dic_zona_tipo.get("lista_fechas_cortas")
        if agrupar_multiples_sensores_con_misma_funcion == True and len(lista_fechas_largas) > 0 and lista_fechas_largas[-1] == str(registro_sensor.getFecha()):
            if registro_sensor.getValor() != -999:
                if lista_valores_medios[-1] != -999:
                    lista_valores[-1].append(round(registro_sensor.getValor()))
                    lista_valores_medios[-1] = sum(lista_valores[-1])/len(lista_valores[-1])
                else:
                    lista_valores[-1]=[(round(registro_sensor.getValor()))]
                    lista_valores_medios[-1]=(round(registro_sensor.getValor()))
        else:
            lista_valores.append([round(registro_sensor.getValor())])
            lista_valores_medios.append(round(registro_sensor.getValor()))
            lista_fechas_largas.append(str(registro_sensor.getFecha()))
            #lista_fechas_cortas.append(str(registro_sensor.getFecha()))
            lista_fechas_cortas.append(str(registro_sensor.getFecha().strftime("%d/%m-%H:%M")))
    return dic_registros_graficar

def __addTipsListToGraph(lista_consejos: List[ConsejoCommon], dic_registros_graficar: Dict):
    for consejo in lista_consejos:
        dic_zona_medida: Dict = dic_registros_graficar.get(consejo.getZonaConsejo().getTipo()).get(consejo.getTipoMedida().getTipo())
        dic_medida_zona: Dict = dic_registros_graficar.get(consejo.getTipoMedida().getTipo()).get(consejo.getZonaConsejo().getTipo())
        lista_valores_minimos = []
        lista_valores_maximos = []
        for valor in dic_zona_medida.get("lista_valores"):
            lista_valores_minimos.append(consejo.getValorMinimo())
            lista_valores_maximos.append(consejo.getValorMaximo())
        dic_zona_medida["lista_valores_minimos"] = lista_valores_minimos
        dic_zona_medida["lista_valores_maximos"] = lista_valores_maximos
        dic_medida_zona["lista_valores_minimos"] = lista_valores_minimos
        dic_medida_zona["lista_valores_maximos"] = lista_valores_maximos
    return dic_registros_graficar


def getAllFromPlantToGraph(np:str) -> List[Dict]:
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            try:
                dic_registros_graficar = __createRecordsDcitToGraph()
                lista_registros = RegistroSensorService.listAllFromPlant(current_app.db, nombre_planta)
                dic_registros_graficar = __addAllRecordsListToGraph(lista_registros, dic_registros_graficar)
                lista_consejos: List[ConsejoPlantaCommon] = ConsejoPlantaService.listAllFromPlant(current_app.db, nombre_planta)
                dic_registros_graficar = __addTipsListToGraph(lista_consejos, dic_registros_graficar)
            except:
                return ("Error al procesar los datos de la planta " + np + " para graficar.", HTTPStatus.NOT_FOUND.value)
            return dic_registros_graficar, HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)

def getAllFromPlantBetweenDatesToGraph(np:str, fi: str, ff: str = None) -> List[Dict]:
    try:
        fecha_inicio=datetime.fromisoformat(fi)
    except(ValueError):
        return ("Error en el formato de la fecha de inicio " + str(fi) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    try:
        if ff is None:
            ff=str(datetime.now())
        fecha_fin=datetime.fromisoformat(ff)
    except(ValueError):
        return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
    if fecha_inicio > fecha_fin:
        return ("La fecha de inicio " + str(fi) + " no puede ser mayor que la fecha de fin " + str(ff) + " .", HTTPStatus.NOT_ACCEPTABLE.value)
    with current_app.app_context() :
        if PlantaService.exists(current_app.db,np):
            nombre_planta: str = np
            try:
                dic_registros_graficar = __createRecordsDcitToGraph()
                lista_registros = RegistroSensorService.listAllFromPlantBetweenDates(current_app.db, nombre_planta, fecha_inicio, fecha_fin)
                dic_registros_graficar = __addAllRecordsListToGraph(lista_registros, dic_registros_graficar)
                lista_consejos: List[ConsejoPlantaCommon] = ConsejoPlantaService.listAllFromPlant(current_app.db, nombre_planta)
                dic_registros_graficar = __addTipsListToGraph(lista_consejos, dic_registros_graficar)
            except:
                return ("Error al procesar los datos de la planta " + np + " para graficar.", HTTPStatus.NOT_FOUND.value)
            return dic_registros_graficar, HTTPStatus.OK.value
        else:
            return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value) 
        
def __dateListIntervals(dias: int, fecha: datetime = None) -> List[RegistroSensorCommon]:
    if fecha is None:
            fecha=datetime.now()
    fecha_fin: arrow = arrow.get(fecha)
    fecha_inicio: arrow = None
    if(dias==1):
        intervalos_dia = 24
        horas_intervalo = 24/intervalos_dia
        fecha_fin = fecha_fin.floor("hours")
        fecha_inicio = fecha_fin.shift(days=-dias,hours=+1)
    if(dias>1):
        intervalos_dia = 4
        if dias > 7:
            intervalos_dia = 2
        if dias > 14:
            intervalos_dia = 1
        horas_intervalo = 24/intervalos_dia
        fecha_actual: arrow = arrow.get(fecha)#
        fecha_fin = fecha_fin.floor("days").shift(days=+1,hours=-horas_intervalo)
        while fecha_actual <= fecha_fin:#
            fecha_fin = fecha_fin.shift(hours=-horas_intervalo)#
        fecha_inicio = fecha_fin.shift(days=-dias,hours=+horas_intervalo)
    f_int: arrow = fecha_inicio   
    lista_fechas = []
    while f_int <= fecha_fin:
        lista_fechas.append((f_int.datetime.replace(tzinfo=None),f_int.shift(hours=+horas_intervalo).datetime.replace(tzinfo=None)))
        f_int = f_int.shift(hours=+horas_intervalo)
    return lista_fechas

def getAvgFromPlantAgroupByIntervalsToGraph(np:str, d: int, ff:str = None) -> List[Dict]:
    with current_app.app_context() :
        if d > 0:
            if PlantaService.exists(current_app.db,np):
                nombre_planta: str = np
                try:
                    if ff is None:
                        ff=str(datetime.now())
                    fecha_fin = datetime.fromisoformat(ff)
                    lista_fechas = __dateListIntervals(d,fecha_fin)
                except:
                    return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
                try:
                    dic_registros_graficar = __createRecordsDcitToGraph()
                    for fecha in lista_fechas:
                        lista_registros = RegistroSensorService.listAllAvgFromPlantBetweenDates(current_app.db, nombre_planta, fecha[0], fecha[1])
                        dic_registros_graficar = __addAllRecordsListToGraph(lista_registros, dic_registros_graficar)
                    lista_consejos: List[ConsejoPlantaCommon] = ConsejoPlantaService.listAllFromPlant(current_app.db, nombre_planta)
                    dic_registros_graficar = __addTipsListToGraph(lista_consejos, dic_registros_graficar)
                except Exception as e:                  
                    return (traceback.print_exc(), HTTPStatus.NOT_FOUND.value)
                except: 
                    return ("Error al procesar los datos de la planta " + np + " para graficar.", HTTPStatus.NOT_FOUND.value)
                return dic_registros_graficar, HTTPStatus.OK.value
            else:
                return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)
        else:
            return ("El numero de dias seleccionados tiene que ser mayor que 0.", HTTPStatus.NOT_FOUND.value)

# def getAllAvgFromPlantToGraphAgroupByIntervals(db, np:str, d: int, ff=str(datetime.now())) -> List[Dict]:
#     if d > 0:
#         if PlantaService.exists(db,np):
#             nombre_planta: str = np
#             try:
#                 fecha_fin = datetime.fromisoformat(ff)
#                 lista_fechas = __dateListIntervals(d,fecha_fin)
#             except:
#                 return ("Error en el formato de la fecha de fin " + str(ff) +" .", HTTPStatus.NOT_ACCEPTABLE.value)
#             try:
#                 dic_registros_graficar = __createRecordsDcitToGraph()
#                 for fecha in lista_fechas:
#                     lista_registros = RegistroSensorService.listAllAvgFromPlantBetweenDates(db, nombre_planta, fecha[0], fecha[1])
#                     dic_registros_graficar = __addAllRecordsListToGraph(lista_registros, dic_registros_graficar)
#                 lista_consejos: List[ConsejoPlantaCommon] = ConsejoPlantaService.listAllFromPlant(db, nombre_planta)
#                 dic_registros_graficar = __addTipsListToGraph(lista_consejos, dic_registros_graficar)
#             except Exception as e:                  
#                 return (traceback.print_exc(), HTTPStatus.NOT_FOUND.value)
#             # except: 
#             #     return ("Error al procesar los datos de la planta " + np + " para graficar.", HTTPStatus.NOT_FOUND.value)
#             return dic_registros_graficar, HTTPStatus.OK.value
#         else:
#             return ("La planta " + np + " no existe.", HTTPStatus.NOT_FOUND.value)
#     else:
#         return ("El numero de dias seleccionados tiene que ser mayor que 0.", HTTPStatus.NOT_FOUND.value)

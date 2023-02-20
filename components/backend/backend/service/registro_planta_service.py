from datetime import datetime
from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroPlanta
from backend.data.db.resultsets import RegistroPlantaSet
from common.data import RegistroPlanta as CommonRegistroPlanta

class RegistroPlantaService():

    @staticmethod
    # def create_registro_planta(tipo_planta: Union[TipoPlanta,str], zona_planta:Union[ZonaPlanta,str] ,numero_planta:int, valor:float, schema: Esquema) -> CommonRegistroPlanta:
    def createRegistroPlanta(esquema: Esquema, nombre_planta: str, tipo_planta: str, 
                               fecha_plantacion: datetime = datetime.now(), fecha_marchitacion: datetime = None) -> CommonRegistroPlanta:
        session: Session = esquema.new_session()
        out: CommonRegistroPlanta = None
        try:
            # if isinstance(tipo_planta, str):
            #     tipo_planta = TipoPlanta[tipo_planta]
            new_registro_planta: RegistroPlanta = RegistroPlantaSet.create(session, nombre_planta, tipo_planta, 
                                                                           fecha_plantacion, fecha_marchitacion)
            out= CommonRegistroPlanta(new_registro_planta.nombre_planta,new_registro_planta.tipo_planta,
                                      new_registro_planta.fecha_plantacion,new_registro_planta.fecha_marchitacion)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createRegistroPlantaFromCommon(esquema: Esquema, registro_planta: CommonRegistroPlanta) -> CommonRegistroPlanta:
        return RegistroPlantaService.createRegistroPlanta(esquema, registro_planta.getNombrePlanta(), registro_planta.getTipoPlanta())

    @staticmethod
    def existsRegistroPlanta(esquema: Esquema, nombre_planta: str) -> bool:
        session: Session = esquema.new_session()
        registro_planta_exists: bool = RegistroPlantaSet.get(session, nombre_planta)
        esquema.remove_session()
        return registro_planta_exists

    @staticmethod
    def listRegistroPlanta(esquema: Esquema) -> List[CommonRegistroPlanta]:
        out: List[CommonRegistroPlanta] = []
        session: Session = esquema.new_session()
        registros_planta: List[RegistroPlanta] = RegistroPlantaSet.list_all(session)
        for registro_planta in registros_planta:
            out.append(CommonRegistroPlanta(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                            registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion))
        esquema.remove_session()
        return out

    @staticmethod
    def getRegistroPlanta(esquema: Esquema, nombre_planta: str) -> CommonRegistroPlanta:
        session: Session = esquema.new_session()
        registro_planta: CommonRegistroPlanta = RegistroPlantaSet.get(session, nombre_planta)
        out= CommonRegistroPlanta(registro_planta.nombre_planta,registro_planta.tipo_planta,
                                  registro_planta.fecha_plantacion,registro_planta.fecha_marchitacion)
        esquema.remove_session()
        return out

'''
    @staticmethod
    def update_pregunta(id:int,schema: Schema):
        session: Session = schema.new_session()
        Preguntas.update(session,id)
        schema.remove_session()
'''

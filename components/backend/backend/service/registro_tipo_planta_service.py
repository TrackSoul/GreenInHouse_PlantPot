from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import RegistroTipoPlanta
from backend.data.db.resultsets import RegistroTipoPlantaSet
from common.data import RegistroTipoPlanta as CommonRegistroTipoPlanta

class RegistroTipoPlantaService():

    @staticmethod
    # def create_registro_planta(tipo_planta: Union[TipoPlanta,str], zona_planta:Union[ZonaPlanta,str] ,numero_planta:int, valor:float, schema: Esquema) -> CommonRegistroPlanta:
    def create_registro_tipo_planta(esquema: Esquema, tipo_planta: str, descripcion_planta: str) -> CommonRegistroTipoPlanta:
        session: Session = esquema.new_session()
        out: CommonRegistroTipoPlanta = None
        try:
            # if isinstance(tipo_planta, str):
            #     tipo_planta = TipoPlanta[tipo_planta]
            new_registro_tipo_planta: RegistroTipoPlanta = RegistroTipoPlantaSet.create(session, tipo_planta, descripcion_planta)
            out= CommonRegistroTipoPlanta(new_registro_tipo_planta.tipo_planta,new_registro_tipo_planta.descripcion_planta)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def create_registro_tipo_planta_from_common(esquema: Esquema, registro_tipo_planta_common: CommonRegistroTipoPlanta) -> CommonRegistroTipoPlanta:
        return RegistroTipoPlantaService.create_registro_tipo_planta(esquema, registro_tipo_planta_common.getTipoPlanta(), registro_tipo_planta_common.getDescripcionPlanta())

    @staticmethod
    def exists_registro_tipo_planta(esquema: Esquema, tipo_planta: str):
        session: Session = esquema.new_session()
        registro_tipo_planta_exists: bool = RegistroTipoPlantaSet.get(session, tipo_planta)
        esquema.remove_session()
        return registro_tipo_planta_exists

    @staticmethod
    def list_registro_planta(esquema: Esquema) -> List[CommonRegistroTipoPlanta]:
        out: List[CommonRegistroTipoPlanta] = []
        session: Session = esquema.new_session()
        registros_tipo_planta: List[RegistroTipoPlanta] = RegistroTipoPlanta.list_all(session)
        for registro_tipo_planta in registros_tipo_planta:
            out.append(CommonRegistroTipoPlanta(registro_tipo_planta.tipo_planta,registro_tipo_planta.descripcion_planta))
        esquema.remove_session()
        return out

'''
    @staticmethod
    def get_pregunta(id : int, schema: Schema) -> common.Pregunta:
        session : Session = schema.new_session()
        pregunta : Pregunta = Preguntas.get_pregunta(session, id)
        out= common.Pregunta(pregunta.creador,pregunta.titulo,pregunta.descripcion,pregunta.id, datetime.fromisoformat(pregunta.fechaCreacion),pregunta.visible)
        schema.remove_session()
        return out

    @staticmethod
    def update_pregunta(id:int,schema: Schema):
        session: Session = schema.new_session()
        Preguntas.update(session,id)
        schema.remove_session()
'''

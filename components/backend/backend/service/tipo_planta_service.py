#Author: Oscar Valverde Escobar

from typing import Union, List, Dict
from sqlalchemy.orm.session import Session # type: ignore
from backend.data.db.esquema import Esquema
from backend.data.db.results import TipoPlanta
from backend.data.db.resultsets import TipoPlantaSet
from backend.service import ConsejoTipoPlantaService
from common.data.util import TipoPlanta as TipoPlantaCommon, ConsejoTipoPlanta as ConsejoTipoPlantaCommon

class TipoPlantaService():

    @staticmethod
    def create(esquema: Esquema, tipo_planta: str, descripcion_planta: str) -> TipoPlantaCommon:
        session: Session = esquema.new_session()
        out: TipoPlantaCommon = None
        try:
            new_tipo_planta: TipoPlanta = TipoPlantaSet.create(session, tipo_planta, descripcion_planta)
            out= TipoPlantaCommon(new_tipo_planta.tipo_planta,new_tipo_planta.descripcion_planta)
            #Creacion de consejos por defecto asociados al nuevo tipo de planta
            for consejo in ConsejoTipoPlantaService.listAllFromTypePlant(esquema,"Plantilla"):
                consejo.setNombreElemento(tipo_planta)
                ConsejoTipoPlantaService.createFromCommon(esquema, consejo)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def createFromCommon(esquema: Esquema, tipo_planta_common: TipoPlantaCommon) -> TipoPlantaCommon:
        return TipoPlantaService.create(esquema, tipo_planta_common.getTipoPlanta(), tipo_planta_common.getDescripcionPlanta())

    @staticmethod
    def exists(esquema: Esquema, tipo_planta: str) -> bool:
        session: Session = esquema.new_session()
        tipo_planta_exists: bool = TipoPlantaSet.get(session, tipo_planta)
        esquema.remove_session()
        return tipo_planta_exists

    @staticmethod
    def listAll(esquema: Esquema) -> List[TipoPlantaCommon]:
        out: List[TipoPlantaCommon] = []
        session: Session = esquema.new_session()
        registros_tipo_planta: List[TipoPlanta] = TipoPlantaSet.listAll(session)
        for tipo_planta in registros_tipo_planta:
            out.append(TipoPlantaCommon(tipo_planta.tipo_planta,tipo_planta.descripcion_planta))
        esquema.remove_session()
        return out

    @staticmethod
    def get(esquema: Esquema, tipo_planta: str) -> TipoPlantaCommon:
        session : Session = esquema.new_session()
        tipo_planta: TipoPlanta = TipoPlantaSet.get(session, tipo_planta)
        out= TipoPlantaCommon(tipo_planta.tipo_planta,tipo_planta.descripcion_planta)
        esquema.remove_session()
        return out

    @staticmethod
    def update(esquema: Esquema, tipo_planta: str, descripcion_planta: str) -> TipoPlantaCommon:
        session: Session = esquema.new_session()
        out: TipoPlantaCommon = None
        try:
            tipo_planta_modificado: TipoPlanta = TipoPlantaSet.update(session, tipo_planta, descripcion_planta)
            out= TipoPlantaCommon(tipo_planta_modificado.tipo_planta,tipo_planta_modificado.descripcion_planta)
        except Exception as ex:
            raise ex
        finally:
            esquema.remove_session()
        return out
    
    @staticmethod
    def updateFromCommon(esquema: Esquema, tipo_planta_common: TipoPlantaCommon) -> TipoPlantaCommon:
        return TipoPlantaService.update(esquema, tipo_planta_common.getTipoPlanta(), tipo_planta_common.getDescripcionPlanta())


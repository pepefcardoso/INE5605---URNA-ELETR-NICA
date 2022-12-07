from dao.DAO import DAO
from entidade.eleitor import Eleitor
import pickle


class EleitorDao(DAO):
    def __init__(self):
        super().__init__('eleitores.pkl')

    def add(self, eleitor: Eleitor):
        if (isinstance(eleitor, Eleitor) and 
            isinstance(eleitor.cpf, str) and
            eleitor is not None):
            super().add(eleitor.cpf, eleitor)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)

    def get_all(self):
        super().get_all()

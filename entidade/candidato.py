from entidade.eleitor import Eleitor
from entidade.cargo import Cargo
from entidade.categoria import Categoria
from entidade.chapa import Chapa


class Candidato(Eleitor):

    def __init__(self,
                 nome: str,
                 cpf: str,
                 categoria: Categoria,
                 numero: str,
                 chapa: Chapa,
                 cargo: Cargo):
        super().__init__(nome, cpf, categoria)
        self.__numero = numero
        self.__chapa = chapa
        self.__cargo = cargo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: str):
        if isinstance(numero, str):
            self.__numero = numero

    @property
    def chapa(self):
        return self.__chapa

    @chapa.setter
    def chapa(self, chapa: Chapa):
        if isinstance(chapa, Chapa):
            self.__chapa = chapa

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: Cargo):
        if isinstance(cargo, Cargo):
            self.__cargo = cargo

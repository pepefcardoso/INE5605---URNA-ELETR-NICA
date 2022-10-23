from entidade.eleitor import Eleitor
from entidade.cargo import Cargo
from entidade.categoria import Categoria


class Candidato(Eleitor):

    def __init__(self, nome: str, cpf: int, categoria: Categoria,
                 numero: int, chapa: str, cargo: Cargo):
        super().__init__(nome, cpf, categoria)
        self.__numero = numero
        self.__chapa = chapa
        self.__cargo = cargo

    @property
    def numero(self):
        return self.__numero

    @property
    def chapa(self):
        return self.__chapa

    @property
    def cargo(self):
        return self.__cargo

    @numero.setter
    def numero(self, numero: int):
        if isinstance(numero, int):
            self.__numero = numero

    @chapa.setter
    def chapa(self, chapa: str):
        if isinstance(chapa, str):
            self.__chapa = chapa

    @cargo.setter
    def cargo(self, cargo: Cargo):
        if isinstance(cargo, Cargo):
            self.__cargo = cargo

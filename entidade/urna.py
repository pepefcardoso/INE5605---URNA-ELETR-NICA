from entidade.categoria import Categoria
from entidade.cargo import Cargo


class Urna():
    def __init__(self,
                 codigo: str,
                 max_eleitores: int,
                 max_candidatos: int):
        self.__codigo = codigo
        self.__max_eleitores = max_eleitores
        self.__max_candidatos = max_candidatos
        self.__turno = 1
        self.__eleitores = []
        self.__candidatos = []
        self.__categorias = Categoria
        self.__cargos = Cargo
        self.__chapas = []
        self.__votos = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo

    @property
    def max_eleitores(self):
        return self.__max_eleitores

    @max_eleitores.setter
    def max_eleitores(self, max_eleitores):
        if isinstance(max_eleitores, int):
            self.__max_eleitores = max_eleitores

    @property
    def max_candidatos(self):
        return self.__max_candidatos

    @max_candidatos.setter
    def max_candidatos(self, max_candidatos):
        if isinstance(max_candidatos, int):
            self.__max_candidatos = max_candidatos

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        if isinstance(turno, int):
            self.__turno = turno

    @property
    def eleitores(self):
        return self.__eleitores

    @property
    def candidatos(self):
        return self.__candidatos

    @property
    def categorias(self):
        return self.__categorias

    @property
    def cargos(self):
        return self.__cargos

    @property
    def chapas(self):
        return self.__chapas

    @property
    def votos(self):
        return self.__votos

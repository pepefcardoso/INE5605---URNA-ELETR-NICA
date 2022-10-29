from entidade.voto import Voto

class Urna():
    def __init__(self,
                 codigo: int,
                 turno: int,
                 max_eleitores: int,
                 max_candidatos: int):
        self.__codigo = codigo
        self.__turno = turno
        self.__max_eleitores = max_eleitores
        self.__max_candidatos = max_candidatos
        self.__lista_votos = []
        self.__votantes_1_turno = []
        self.__votantes_2_turno = []

    @property
    def lista_votos(self):
        return self.__lista_votos

    @property
    def votantes_1_turno(self):
        return self.__votantes_1_turno

    @property
    def votantes_2_turno(self):
        return self.__votantes_2_turno

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno: int):
        self.__turno = turno

    @property
    def max_eleitores(self):
        return self.__max_eleitores

    @max_eleitores.setter
    def max_eleitores(self, max_eleitores: int):
        self.__max_eleitores = max_eleitores

    @property
    def max_candidatos(self):
        return self.__max_candidatos

    @max_candidatos.setter
    def max_candidatos(self, max_candidatos):
        self.__max_candidatos = max_candidatos

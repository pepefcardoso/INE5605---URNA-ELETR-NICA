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
        self.__lista_candidatos = []
        self.__lista_eleitor = []
        self.__lista_voto = []
        self.__lista_quem_ja_votou = []

    @property
    def lista_quem_ja_votou(self):
        return self.__lista_quem_ja_votou

    @property
    def lista_candidatos(self):
        return self.__lista_candidatos

    @lista_candidatos.setter
    def lista_candidatos(self, lista_candidatos: []):
        self.__lista_candidatos = lista_candidatos

    @property
    def lista_eleitor(self):
        return self.__lista_eleitor

    @lista_eleitor.setter
    def lista_eleitor(self, lista_eleitor: []):
        self.__lista_eleitor = lista_eleitor

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

    def add_voto(self, voto: Voto):
        self.__lista_voto.append(voto)

    def add_dono_do_voto(self, dono_do_voto):
        self.__lista_quem_ja_votou.append(dono_do_voto)

    def relatorio_dos_votos(self):
        pass
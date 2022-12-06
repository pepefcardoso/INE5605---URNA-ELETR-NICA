from entidade.categoria import Categoria
from entidade.pessoa import Pessoa


class Eleitor(Pessoa):

    def __init__(self, 
                 nome: str, 
                 cpf: str, 
                 categoria: Categoria):
        super().__init__(nome)
        self.__cpf = cpf
        self.__categoria = categoria
        self.__votou_1t = False
        self.__votou_2t = False

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        if isinstance(categoria, Categoria):
            self.__categoria = categoria

    @property
    def votou_1t(self):
        return self.__votou_1t

    @votou_1t.setter
    def votou_1t(self, votou_1t):
        if isinstance(votou_1t, bool):
            self.__votou_1t = votou_1t

    @property
    def votou_2t(self):
        return self.__votou_2t

    @votou_2t.setter
    def votou_2t(self, votou_2t):
        if isinstance(votou_2t, bool):
            self.__votou_2t = votou_2t

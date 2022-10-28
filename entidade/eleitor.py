from entidade.categoria import Categoria

class Eleitor:

    def __init__(self, nome: str, cpf: str, categoria: Categoria):
        self.__nome = nome
        self.__cpf = cpf
        self.__categoria = categoria

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def categoria(self):
        return self.__categoria

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @categoria.setter
    def categoria(self, categoria: Categoria):
        if isinstance(categoria, Categoria):
            self.__categoria = categoria

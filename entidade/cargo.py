from enum import Enum

class Cargo(Enum):
    REITOR = 1
    PRO_REITOR_GRADUACAO = 2
    PRO_REITOR_PESQUISA = 3
    PRO_REITOR_EXTENSAO = 4

'''
class Cargo():
    def __init__(self, cargo: str):
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo
'''

if __name__ == '__main__':
    for cargo in Cargo:
        print(cargo.name)

    nome = Cargo(3)
    print(nome.name)

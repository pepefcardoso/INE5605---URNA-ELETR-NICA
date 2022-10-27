class Voto:
    def __init__(self, voto_reitor: int, voto_grad: int, voto_pesquisa: int, voto_extensa: int):
        self.__voto_reitor = voto_reitor
        self.__voto_grad = voto_grad
        self.__voto_pesquisa = voto_pesquisa
        self.__voto_extensao = voto_extensa

    @property
    def voto_reitor(self):
        return self.__voto_reitor

    @property
    def voto_grad(self):
        return self.__voto_grad

    @property
    def voto_pesquisa(self):
        return self.__voto_pesquisa

    @property
    def voto_extensao(self):
        return self.__voto_extensao

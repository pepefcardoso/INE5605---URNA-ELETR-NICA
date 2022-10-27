from entidade.categoria import Categoria


class Voto:
    def __init__(self, voto_reitor: int, voto_grad: int, voto_pesq: int, voto_ext: int, categoria: Categoria):
        self.__voto_reitor = voto_reitor
        self.__voto_grad = voto_grad
        self.__voto_pesq = voto_pesq
        self.__voto_ext = voto_ext
        self.__categoria = categoria

    @property
    def voto_reitor(self):
        return self.__voto_reitor

    @property
    def voto_grad(self):
        return self.__voto_grad

    @property
    def voto_pesq(self):
        return self.__voto_pesq

    @property
    def voto_ext(self):
        return self.__voto_ext

    @property
    def categoria(self):
        return self.__categoria

    @voto_reitor.setter
    def voto_reitor(self, voto_reitor: int):
        if isinstance(voto_reitor, int):
            self.__voto_reitor = voto_reitor

    @voto_grad.setter
    def voto_grad(self, voto_grad: int):
        if isinstance(voto_grad, int):
            self.__voto_grad = voto_grad

    @voto_pesq.setter
    def voto_pesq(self, voto_pesq: int):
        if isinstance(voto_pesq, int):
            self.__voto_pesq = voto_pesq

    @voto_ext.setter
    def voto_ext(self, voto_ext: int):
        if isinstance(voto_ext, int):
            self.__voto_ext = voto_ext

    @categoria.setter
    def categoria(self, categoria: Categoria):
        if isinstance(categoria, Categoria):
            self.__categoria = categoria

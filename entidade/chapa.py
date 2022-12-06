from entidade.pessoa import Pessoa


class Chapa(Pessoa):
    def __init__(self, 
                 codigo: str, 
                 nome: str):
        self.__codigo = codigo
        super().__init__(codigo, nome)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo

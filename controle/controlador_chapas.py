from limite.tela_chapas import TelaChapa
from entidade.chapa import Chapa

class ControladorChapas():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_chapa = TelaChapa()
        self.__chapas = []

    def lista_chapas(self):
        pass

    def adiciona_chapa(self):
        pass

    def remove_chapa(self):
        pass

    def mostra_tela_opcoes(self):
        opcoes = {1: self.lista_chapas, 2: self.adiciona_chapa,
                3:self.remove_chapa}
        while True:
            opcao = self.__tela_chapa.mostra_tela_chapas()
            if opcao == 0:
                break
            opcoes[opcao]()

from limite.tela_chapa import TelaChapa
from entidade.chapa import Chapa

class ControladorChapa():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_chapa = TelaChapa()
        self.__lista_chapa = []

    def lista_chapa(self):
        pass

    def inclui_chapa(self):
        pass

    def exclui_chapa(self):
        pass

    def mostra_tela_opcoes(self):
        switcher = {1: self.lista_chapa,
                    2: self.inclui_chapa,
                    3: self.exclui_chapa}
        while True:
            opcao = self.__tela_chapa.mostra_tela()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

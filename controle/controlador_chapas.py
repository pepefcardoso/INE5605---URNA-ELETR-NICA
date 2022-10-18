from limite.tela_chapas import TelaChapa
from entidade.chapa import Chapa

class ControladorChapas():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_chapa = TelaChapa()
        self.__chapas = []

    def lista_chapas(self):
        for chapa in self.__chapas:
            nome = chapa.nome
            self.__tela_chapa.mostra_chapa(nome)
        if self.__chapas == []:
            self.__tela_chapa.mostra_mensagem("\nNão existem chapas cadastradas!\n")

    def adiciona_chapa(self):
        nova_chapa = Chapa(self.__tela_chapa.pega_nome_chapa())
        for chapa in self.__chapas:
            if chapa.nome == nova_chapa.nome:
                self.__tela_chapa.mostra_mensagem("\nJá existe uma chapa cadastrada com este nome!\n")
                return None
        self.__chapas.append(nova_chapa)

    def remove_chapa(self):
        pass

    def altera_chapa(self):
        pass

    def mostra_tela_opcoes(self):
        opcoes = {1: self.lista_chapas, 2: self.adiciona_chapa,
                3:self.remove_chapa, 4:self.altera_chapa}
        while True:
            opcao = self.__tela_chapa.mostra_tela_chapas()
            if opcao == 0:
                break
            opcoes[opcao]()

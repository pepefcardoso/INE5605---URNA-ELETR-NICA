from limite.tela_chapas import TelaChapa
from entidade.chapa import Chapa

class ControladorChapas():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_chapa = TelaChapa()
        self.__chapas = []

    def mostra_tela_inicial(self):
        opcoes = {1: self.lista_chapas, 2: self.adiciona_chapa,
                  3: self.remove_chapa, 4: self.altera_chapa}
        while True:
            self.__tela_chapa.mostra_menu_opcoes()
            opcao = self.__tela_chapa.pega_opcao()
            if opcao == 0:
                break
            opcoes[opcao]()

    def lista_chapas(self):
        if self.__chapas == []:
            self.__tela_chapa.mostra_mensagem('\nNÃO EXISTEM CHAPAS CADASTRADAS!\n')
        else:
            for chapa in self.__chapas:
                nome_chapa = {'Nome': chapa.nome}
                self.__tela_chapa.mostra_entidade(nome_chapa)

    def adiciona_chapa(self):
        nome_chapa = self.__tela_eleitores.pega_nome_chapa()
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                self.__tela_chapa.mostra_mensagem("\nJÁ EXISTE CHAPA CADASTRADA COM ESTE NOME!\n")
                return None
        self.__tela_chapa.mostra_mensagem("\nCHAPA CADASTRADA COM SUCESSO!\n")
        self.__eleitores.append(Chapa(nome_chapa))

    def remove_chapa(self):
        nome_chapa = self.__tela_eleitores.pega_nome_chapa()
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                self.__chapas.remove(chapa)
                return self.__tela_chapa.mostra_mensagem("\nCHAPA REMOVIDA COM SUCESSO!\n")
        self.__tela_chapa.mostra_mensagem("\nNÃO EXISTE CHAPA CADASTRADA COM ESTE NOME!\n")

    def altera_chapa(self):
        nome_chapa = self.__tela_eleitores.pega_nome_chapa()
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                nova_chapa = self.__tela_eleitores.pega_nome_chapa()
                chapa.nome = nova_chapa
                return self.__tela_eleitores.mostra_mensagem('\nCHAPA ALTERADA COM SUCESSO\n')
        self.__tela_eleitores.mostra_mensagem('\nNÃO EXISTE CHAPA CADASTRADA COM ESTE NOME!\n')

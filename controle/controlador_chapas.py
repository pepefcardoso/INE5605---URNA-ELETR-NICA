from limite.tela_chapas import TelaChapa
from entidade.chapa import Chapa

class ControladorChapas():
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_chapa = TelaChapa()
        self.__chapas = []

    def mostra_tela_inicial(self):
        opcoes = {1: self.lista_chapas, 2: self.adiciona_chapa,
                  3: self.remove_chapa, 4: self.altera_chapa}
        while True:
            self.__tela_chapa.abre_tela_inicial()
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
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                self.__tela_chapa.mostra_mensagem("\nJÁ EXISTE CHAPA CADASTRADA COM ESTE NOME!\n")
                return None
        self.__tela_chapa.mostra_mensagem("\nCHAPA CADASTRADA COM SUCESSO!\n")
        self.__chapas.append(Chapa(nome_chapa))

    def remove_chapa(self):
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                self.__chapas.remove(chapa)
                return self.__tela_chapa.mostra_mensagem("\nCHAPA REMOVIDA COM SUCESSO!\n")
        self.__tela_chapa.mostra_mensagem("\nNÃO EXISTE CHAPA CADASTRADA COM ESTE NOME!\n")

    def altera_chapa(self):
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                nova_chapa = self.__tela_chapa.pega_nome_chapa()
                chapa.nome = nova_chapa
                return self.__tela_chapa.mostra_mensagem('\nCHAPA ALTERADA COM SUCESSO\n')
        self.__tela_chapa.mostra_mensagem('\nNÃO EXISTE CHAPA CADASTRADA COM ESTE NOME!\n')

    def seleciona_chapa(self):
        opcoes = self.lista_chapas_enum()
        if self.__chapas == []:
            self.__tela_chapa.mostra_mensagem('\nNÃO EXISTEM CHAPAS CADASTRADAS!\n')
        while True:
            opcao = self.__tela_chapa.pega_chapa_num(opcoes, list(opcoes.keys()))
            if opcao == 0:
                break
            for chapa in self.__chapas:
                if opcoes[opcao] == chapa.nome:
                    return chapa

    def lista_chapas_enum(self):
        dict_chapas = {}
        i = 1
        for chapa in self.__chapas:
            dict_chapas[i] = chapa.nome
            i +=1
        return dict_chapas

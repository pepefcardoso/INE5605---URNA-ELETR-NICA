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
        for chapa in self.__eleitores:
            if eleitor.cpf == novo_eleitor.cpf:
                self.__tela_eleitores.mostra_mensagem("\nJÁ EXISTE ELEITOR CADASTRADO COM ESTE CPF!!\n")
                return None
        self.__tela_eleitores.mostra_mensagem("\nELEITOR CADSTRADO COM SUCESSO!\n")
        self.__eleitores.append(novo_eleitor)

    def remove_eleitor(self):
        cpf_eleitor = self.__tela_eleitores.pega_cpf_eleitor()
        for eleitor in self.__eleitores:
            if eleitor.cpf == cpf_eleitor:
                self.__eleitores.remove(eleitor)
                return self.__tela_eleitores.mostra_mensagem('\nELEITOR REMOVIDO COM SUCESSO\n')
        self.__tela_eleitores.mostra_mensagem('\nNÃO EXISTE ELEITOR CADASTRADO COM O CPF CONSULTADO!\n')

    def altera_eleitor(self):
        cpf_eleitor = self.__tela_eleitores.pega_cpf_eleitor()
        for eleitor in self.__eleitores:
            if eleitor.cpf == cpf_eleitor:
                dados_eleitor = self.__tela_eleitores.pega_dados_eleitor()
                eleitor.nome = dados_eleitor['nome']
                eleitor.cpf = dados_eleitor['cpf']
                eleitor.categoria = dados_eleitor['categoria']
                return self.__tela_eleitores.mostra_mensagem('\nELEITOR ALTERADO COM SUCESSO\n')
        self.__tela_eleitores.mostra_mensagem('\nNÃO EXISTE ELEITOR CADASTRADO COM O CPF CONSULTADO!\n')

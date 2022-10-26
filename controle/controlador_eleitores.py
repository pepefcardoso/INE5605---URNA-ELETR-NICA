from limite.tela_eleitores import TelaEleitores
from entidade.eleitor import Eleitor

class ControladorEleitores:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_eleitores = TelaEleitores()
        self.__eleitores = []

    def mostra_tela_inicial(self):
        opcoes = {1: self.lista_eleitores, 2: self.adiciona_eleitor,
                  3: self.remove_eleitor, 4: self.altera_eleitor}
        while True:
            self.__tela_eleitores.mostra_menu_opcoes()
            opcao = self.__tela_eleitores.pega_opcao()
            if opcao == 0:
                break
            opcoes[opcao]()

    def lista_eleitores(self):
        if self.__eleitores == []:
            self.__tela_eleitores.mostra_mensagem('\nNÃO EXISTEM ELEITORES CADASTRADOSs!\n')
        else:
            for eleitor in self.__eleitores:
                dados_eleitor = {'Nome': eleitor.nome,'CPF': eleitor.cpf,'Categoria': eleitor.categoria}
                self.__tela_eleitores.mostra_entidade(dados_eleitor)

    def adiciona_eleitor(self):
        dados_eleitor = self.__tela_eleitores.pega_dados_eleitor()
        novo_eleitor = Eleitor(dados_eleitor['nome'], dados_eleitor['cpf'], dados_eleitor['categoria'])
        for eleitor in self.__eleitores:
            if eleitor.cpf == novo_eleitor.cpf:
                self.__tela_eleitores.mostra_mensagem("\nJÁ EXISTE ELEITOR CADASTRADO COM ESTE CPF!!\n")
                return None
        self.__tela_eleitores.mostra_mensagem("\nELEITOR CADASTRADO COM SUCESSO!\n")
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

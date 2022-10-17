from limite.tela_eleitores import TelaEleitores
from entidade.eleitor import Eleitor

class ControladorEleitores:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_eleitores = TelaEleitores()
        self.__eleitores = []
        self.__max_eleitores = 0

    def mostra_tela_opcoes(self):
        opcoes = {1: self.lista_eleitores, 2: self.adiciona_eleitor,
                3:self.remove_eleitor, 4: self.maximo_eleitores}
        while True:
            opcao = self.__tela_eleitores.mostra_tela_eleitores()
            if opcao == 0:
                break
            opcoes[opcao]()

    def lista_eleitores(self):
        for eleitor in self.__eleitores:
            dados_eleitor = {'nome': eleitor.nome,'cpf': eleitor.cpf,'categoria': eleitor.categoria}
            self.__tela_eleitores.mostra_eleitor(dados_eleitor)

    def adiciona_eleitor(self):
        dados_eleitor = self.__tela_eleitores.pega_dados_eleitor()
        novo_eleitor = Eleitor(dados_eleitor['nome'], dados_eleitor['cpf'], dados_eleitor['categoria'])
        for eleitor in self.__eleitores:
            if eleitor.cpf == novo_eleitor.cpf:
                return False
        self.__eleitores.append(novo_eleitor)

    def remove_eleitor(self):
        pass

    def maximo_eleitores(self):
        pass

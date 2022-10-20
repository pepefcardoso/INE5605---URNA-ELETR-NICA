from limite.tela_candidatos import TelaCandidatos
from entidade.candidato import Candidato

class ControladorCandidatos:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_candidatos = TelaCandidatos()
        self.__candidatos = []
        self.__max_candidatos = 0

    def mostra_tela_opcoes(self):
        opcoes = {1: self.lista_candidatos, 2: self.adiciona_candidato,
                  3:self.remove_candidato, 4: self.maximo_candidatos}
        while True:
            opcao = self.__tela_candidatos.mostra_tela_candidatos()
            if opcao == 0:
                break
            opcoes[opcao]()

    def lista_candidatos(self):
        for candidato in self.__candidatos:
            dados_candidato = {'nome': candidato.__nome,'cpf': candidato.__nome,'categoria': candidato.__categoria, 'numero': candidato.__numero, 'chapa': candidato.__chapa, 'cargo': candidato.__cargo}
            self.__tela_candidatos.mostra_candidato(dados_candidato)

    def adiciona_candidato(self):
        pass

    def remove_candidato(self):
        pass

    def maximo_candidatos(self):
        pass

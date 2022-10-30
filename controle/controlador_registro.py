from limite.tela_registros import TelaRegistros
from entidade.eleitor import Eleitor
from entidade.candidato import Candidato
from entidade.voto import Voto


class ControladorRegistro:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_registros = TelaRegistros()

    def mostra_tela_inicial(self):
        opcoes = {1: self.abre_registros_1_turno,
                  2: self.abre_registros_2_turno}
        while True:
            self.__tela_registros.abre_tela_inicial()
            opcao = self.__tela_registros.pega_opcao()
            if opcao == 0:
                break
            opcoes[opcao]()

    def abre_registros_1_turno(self):
        while True:
            self.__tela_registros.abre_tela_registros(1)
            opcao = self.__tela_registros.pega_opcao_registro()
            if opcao == 0:
                break
            self.mostra_resultados_gerais(1)

    def abre_registros_2_turno(self):
        while True:
            self.__tela_registros.abre_tela_registros(2)
            opcao = self.__tela_registros.pega_opcao_registro()
            if opcao == 0:
                break
            self.mostra_resultados_gerais(2)

    def mostra_resultados_gerais(self, turno):
        self.__tela_registros.mostra_mensagem('cheguei aqui')

from limite.tela_registros import TelaRegistros
from entidade.eleitor import Eleitor
from entidade.candidato import Candidato
from entidade.voto import Voto


class ControladorRegistro:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_registros = TelaRegistros()

    def mostra_tela_inicial(self):
        opcoes = {1: self.abre_registros_geral, 
                  2: self.abre_registros_1_turno,
                  3: self.abre_registros_2_turno}
        while True:
            self.__tela_registros.abre_tela_inicial()
            opcao = self.__tela_registros.pega_opcao()
            if opcao == 0:
                break
            opcoes[opcao]()

    def mostra_tela_registros(self):
        pass

    def abre_registros_1_turno(self):
        pass

    def abre_registros_2_turno(self):
        pass

    def abre_registros_geral(self):
        pass

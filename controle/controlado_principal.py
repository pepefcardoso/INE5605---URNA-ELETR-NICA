from limite.tela_principal import TelaPrincipal
from controle.controlador_eleitores import ControladorEleitores
from controle.controlador_candidatos import ControladorCandidatos
import sys


class ControladorPrincipal:

    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__controlador_eleitores = ControladorEleitores(self)
        self.__controlador_candidatos = ControladorCandidatos(self)

    def inicia_eleitores(self):
        self.__controlador_eleitores.mostra_tela_opcoes()

    def inicia_candidatos(self):
        self.__controlador_candidatos.mostra_tela_opcoes()

    def inicia_config(self):
        pass

    def finaliza(self):
        sys.exit()

    def inicia(self):
        opcoes = {1: self.inicia_eleitores, 2: self.inicia_candidatos, 3: self.inicia_config, 0: self.finaliza}
        while True:
            opcao = self.__tela_principal.mostra_tela_inicial()
            opcoes[opcao]()
    

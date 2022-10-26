from limite.tela_urna import TelaUrna
from entidade.urna import Urna
from controle.controlador_eleitores import ControladorEleitores
from controle.controlador_candidatos import ControladorCandidatos
from controle.controlador_chapas import ControladorChapas
from controle.controlador_cargo import ControladorCargo
from controle.controlador_categoria_eleitor import ControladorCategoria
from controle.controlador_registro import ControladorRegistro
from controle.controlador_config import ControladorConfig

import sys


class ControladorUrna:
    def __init__(self):
        self.__tela_urna = TelaUrna()
        self.__controlador_eleitores = ControladorEleitores(self)
        self.__controlador_candidatos = ControladorCandidatos(self)
        self.__controlador_chapas = ControladorChapas(self)
        self.__controlador_cargo = ControladorCargo(self)
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_registro = ControladorRegistro(self)
        self.__controlador_config = ControladorConfig(self)

    @property
    def controlador_eleitores(self):
        return self.__controlador_eleitores

    @property
    def controlador_candidatos(self):
        return self.__controlador_candidatos

    @property
    def controlador_chapas(self):
        return self.__controlador_chapas

    @property
    def controlador_cargo(self):
        return self.__controlador_cargo

    @property
    def controlador_categoria(self):
        return self.__controlador_categoria

    @property
    def controlador_registro(self):
        return self.__controlador_registro

    @property
    def controlador_config(self):
        return self.__controlador_config

    def inicia_eleitores(self):
        self.__controlador_eleitores.mostra_tela_inicial()

    def inicia_candidatos(self):
        self.__controlador_candidatos.mostra_tela_inicial()

    def inicia_chapas(self):
        self.__controlador_chapas.mostra_tela_inicial()

    def inicia_cargos(self):
        self.__controlador_cargo.mostra_tela_inicial()

    def inicia_categoria(self):
        self.__controlador_categoria.mostra_tela_inicial()

    def inicia_registros(self):
        self.__controlador_registro.mostra_tela_inicial()

    def inicia_config(self):
        self.__controlador_config.mostra_tela_inicial()

    def finaliza(self):
        sys.exit()

    def inicializa_urna(self):
        dados_urna = self.__tela_urna.pega_config()
        self.__urna = Urna(dados_urna['codigo'], 
                           dados_urna['turno'], 
                           dados_urna['max_eleitores'], 
                           dados_urna['max_candidatos'])
        ControladorUrna().inicia_sistema()

    def inicia_sistema(self):
        opcoes = {1: self.inicia_eleitores,
                  2: self.inicia_candidatos,
                  3: self.inicia_chapas,
                  4: self.inicia_cargos,
                  5: self.inicia_categoria,
                  6: self.inicia_registros,
                  7: self.inicia_config,
                  0: self.finaliza}
        while True:
            self.__tela_urna.abre_tela_inicial()
            opcao = self.__tela_urna.pega_opcao()
            opcoes[opcao]()

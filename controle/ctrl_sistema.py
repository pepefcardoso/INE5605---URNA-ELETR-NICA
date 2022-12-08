from controle.ctrl_urna import ControladorUrna
from controle.ctrl_eleitor import ControladorEleitores
from controle.ctrl_candidatos import ControladorCandidatos
from controle.ctrl_chapas import ControladorChapas
from controle.ctrl_cargo import ControladorCargos
from controle.ctrl_categoria import ControladorCategoria
from controle.ctrl_relatorios import ControladorRelatorios
from controle.ctrl_configuracoes import ControladorConfiguracoes
from controle.ctrl_votacao import ControladorVotacao
from limite.tela_sistema import TelaSistema
import PySimpleGUI as psg
import sys


class ControladorSistema:
    def __init__(self):
        self.__ctrl_urna = ControladorUrna(self)
        self.__ctrl_eleitores = ControladorEleitores(self)
        self.__ctrl_candidatos = ControladorCandidatos(self)
        self.__ctrl_chapas = ControladorChapas(self)
        self.__ctrl_cargo = ControladorCargos(self)
        self.__ctrl_categoria = ControladorCategoria(self)
        self.__ctrl_relatorios = ControladorRelatorios(self)
        self.__ctrl_configuracoes = ControladorConfiguracoes(self)
        self.__ctrl_votacao = ControladorVotacao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def ctrl_urna(self):
        return self.__ctrl_urna

    @property
    def ctrl_eleitores(self):
        return self.__ctrl_eleitores

    @property
    def ctrl_candidatos(self):
        return self.__ctrl_candidatos

    @property
    def ctrl_chapas(self):
        return self.__ctrl_chapas

    @property
    def ctrl_cargo(self):
        return self.__ctrl_cargo

    @property
    def ctrl_categoria(self):
        return self.__ctrl_categoria

    @property
    def ctrl_relatorios(self):
        return self.__ctrl_relatorios

    @property
    def ctrl_configuracoes(self):
        return self.__ctrl_configuracoes

    @property
    def ctrl_votacao(self):
        return self.__ctrl_votacao

    def inicia_eleitores(self):
        self.__ctrl_eleitores.mostra_tela_inicial()

    def inicia_candidatos(self):
        self.__ctrl_candidatos.mostra_tela_inicial()

    def inicia_chapas(self):
        self.__ctrl_chapas.mostra_tela_inicial()

    def inicia_cargos(self):
        self.__ctrl_cargo.mostra_tela_inicial()

    def inicia_categoria(self):
        self.__ctrl_categoria.mostra_tela_inicial()

    def inicia_relatorios(self):
        self.__ctrl_relatorios.mostra_tela_inicial()

    def inicia_config(self):
        self.__ctrl_configuracoes.mostra_tela_inicial()

    def inicia_votacao(self):
        self.__ctrl_votacao.mostra_tela_inicial()

    def abre_sistema(self):
        if not self.__ctrl_urna.configura_urna():
            return
        self.abre_menu_inicial()

    def abre_menu_inicial(self):
        self.__tela_sistema.tela_opcoes()
        opcoes = {'ELEITORES': self.inicia_eleitores,
                  'CANDIDATOS': self.inicia_candidatos,
                  'CHAPAS': self.inicia_chapas,
                  'CARGOS': self.inicia_cargos,
                  'CATEGORIAS': self.inicia_categoria,
                  'RELATÓRIOS': self.inicia_relatorios,
                  'CONFIGURAÇÕES': self.inicia_config,
                  'VOTAÇÃO': self.inicia_votacao}
        while True:
            button, values = self.__tela_sistema.abre()
            if button in (psg.WIN_CLOSED, 'SAIR'):
                break
            self.__tela_sistema.fecha()
            return opcoes[button]()
        

from limite.tela_votacao import TelaVotacao
from entidade.voto import Voto
from entidade.eleitor import Eleitor
from entidade.cargo import Cargo
import PySimpleGUI as psg


class ControladorVotacao():
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_votacao = TelaVotacao()

    def mostra_tela_inicial(self):
        self.__tela_votacao.tela_opcoes_inicial(self.__ctrl_sistema.ctrl_urna.urna.turno)
        while True:
            event, values = self.__tela_votacao.abre()
            if event in (psg.WIN_CLOSED, 'VOLTAR'):
                self.__tela_votacao.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'INICIAR':
                pass





            '''if event == 'CORRIGIR':
                numero = ''
                self.__tela_votacao.atualiza_numero(numero)
            if len(numero) <= 1 and event.isnumeric():
                numero += event
                self.__tela_votacao.atualiza_numero(numero)'''

from entidade.cargo import Cargo
from limite.tela_cargos import TelaCargos
import PySimpleGUI as psg


class ControladorCargos():
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_cargos = TelaCargos()

    def mostra_tela_inicial(self):
        self.__tela_cargos.tela_cargos([x.name for x in self.__ctrl_sistema.ctrl_urna.urna.cargos])
        while True:
            event, values = self.__tela_cargos.abre()
            if event in ('SAIR', psg.WIN_CLOSED):
                self.__tela_cargos.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()

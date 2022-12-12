from limite.tela_relatorios import TelaRelatorios
from entidade.cargo import Cargo
import PySimpleGUI as psg


class ControladorRelatorios():

    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_relatorios = TelaRelatorios()

    def mostra_tela_inicial(self):
        self.__tela_relatorios.tela_opcoes()
        while True:
            event, values = self.__tela_relatorios.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_relatorios.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == '1º TURNO':
                self.__tela_relatorios.fecha()
                return self.mostra_relatorios(1, Cargo(1))
            if event == '2º TURNO':
                self.__tela_relatorios.fecha()
                return self.mostra_relatorios(1, Cargo(1))

    def mostra_relatorios(self, turno:int, cargo: Cargo):
        try:
            lista_resultados = self.__ctrl_sistema.ctrl_urna.calcula_lista_resultados_cargo(turno, cargo)
            while True:
                self.__tela_relatorios.tela_mostra_relatorios(lista_resultados)
                event, values = self.__tela_relatorios.abre()
                if event in ('VOLTAR', psg.WIN_CLOSED):
                    self.__tela_relatorios.fecha()
                    return self.mostra_tela_inicial()
        except Exception as e:
            self.__tela_relatorios.mostra_mensagem('ERRO', e)
            self.__tela_relatorios.fecha()
            return self.mostra_tela_inicial()

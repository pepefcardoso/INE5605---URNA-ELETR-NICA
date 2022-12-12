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
                return self.mostra_relatorios(1)
            if event == '2º TURNO':
                self.__tela_relatorios.fecha()
                return self.mostra_relatorios(1)

    def mostra_relatorios(self, turno:int):
        self.__tela_relatorios.tela_mostra_relatorios(self.calcula_lista_resultados(turno, Cargo(1)))
        while True:
            event, values = self.__tela_relatorios.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_relatorios.fecha()
                return self.mostra_tela_inicial()

    def calcula_lista_resultados(self, turno:int, cargo:Cargo):
        try:
            dicionario = self.__ctrl_sistema.ctrl_urna.conta_votos_cargo(turno, cargo)
            n_votos = 0
            for key in dicionario:
                n_votos += dicionario[key]
            lista = []
            for key in dicionario:
                lista.append([key, dicionario[key], float(dicionario[key]//n_votos)])
            return lista
        except Exception as e:
            self.__tela_relatorios.mostra_mensagem('ERRO', e)
            return False
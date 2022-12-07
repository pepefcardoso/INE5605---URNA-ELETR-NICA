from limite.tela_chapas import TelaChapas
from entidade.chapa import Chapa
import PySimpleGUI as psg


class ControladorChapas():

    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_chapas = TelaChapas()

    def mostra_tela_inicial(self):
        lista = self.__ctrl_sistema.ctrl_urna.lista_chapas()
        self.__tela_chapas.tela_opcoes(lista)
        opcoes = {'REMOVER': self.remove_chapa,
                  'ALTERAR': self.altera_chapa}
        while True:
            event, values = self.__tela_chapas.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_chapas.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'ADICIONAR':
                self.__tela_chapas.fecha()
                return self.adiciona_chapa()
            if event in ('REMOVER', 'ALTERAR'):
                if values['LISTA'] == []:
                    self.__tela_chapas.mostra_mensagem('ERRO', "NENHUMA CHAPA FOI SELECIONADO")
                else:
                    self.__tela_chapas.fecha()
                    return opcoes[event](lista[values['LISTA'][0]])

    def adiciona_chapa(self):
        self.__tela_chapas.tela_adiciona_chapa()
        while True:
            event, values = self.__tela_chapas.abre()
            if event in ('CANCELAR', psg.WIN_CLOSED):
                self.__tela_chapas.fecha()
                return self.mostra_tela_inicial()
            if event == 'SALVAR':
                codigo = values['1'].strip()
                nome = values['2'].strip().title()
                try:
                    if self.__ctrl_sistema.ctrl_urna.adiciona_chapa(codigo, nome):
                        self.__tela_chapas.mostra_mensagem('SUCESSO', 'CHAPA ADICIONADA!')
                        self.__tela_chapas.fecha()
                        return self.mostra_tela_inicial()
                except Exception as e:
                    self.__tela_chapas.mostra_mensagem('ERRO', e)

    def remove_chapa(self, chapa: list):
        if chapa is not None and chapa != []:
            self.__tela_chapas.tela_remove_chapa(chapa)
            while True:
                event, values = self.__tela_chapas.abre()
                if event in ('CANCELAR', psg.WIN_CLOSED):
                    self.__tela_chapas.fecha()
                    return self.mostra_tela_inicial()
                if event == 'CONFIRMAR':
                    try:
                        if self.__ctrl_sistema.ctrl_urna.remove_chapa(chapa[0]):
                            self.__tela_chapas.mostra_mensagem('SUCESSO', 'CHAPA REMOVIDA!')
                            self.__tela_chapas.fecha()
                            return self.mostra_tela_inicial()
                    except Exception as e:
                        self.__tela_chapas.mostra_mensagem('ERRO', e)
        return self.mostra_tela_inicial()

    def altera_chapa(self, chapa: list):
        if chapa is not None and chapa != []:
            self.__tela_chapas.tela_altera_chapa(chapa)
            while True:
                event, values = self.__tela_chapas.abre()
                if event in ('CANCELAR', psg.WIN_CLOSED):
                    self.__tela_chapas.fecha()
                    return self.mostra_tela_inicial()
                if event == 'SALVAR':
                    nome = values['1'].strip().title()
                    try:
                        if self.__ctrl_sistema.ctrl_urna.altera_chapa(chapa[0], nome):
                            self.__tela_chapas.mostra_mensagem('SUCESSO', 'CHAPA ALTERADO!')
                            self.__tela_chapas.fecha()
                            return self.mostra_tela_inicial()
                    except Exception as e:
                        self.__tela_chapas.mostra_mensagem('ERRO', e)
        return self.mostra_tela_inicial()

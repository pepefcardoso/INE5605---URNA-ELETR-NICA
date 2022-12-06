from limite.tela_eleitores import TelaEleitores
from entidade.eleitor import Eleitor
from entidade.categoria import Categoria
import PySimpleGUI as psg


class ControladorEleitores:

    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_eleitores = TelaEleitores()

    def mostra_tela_inicial(self):
        lista = self.__ctrl_sistema.ctrl_urna.lista_eleitores()
        self.__tela_eleitores.tela_opcoes(lista)
        opcoes = {'REMOVER': self.remove_eleitor,
                  'ALTERAR': self.altera_eleitor}
        while True:
            event, values = self.__tela_eleitores.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_eleitores.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'ADICIONAR':
                self.__tela_eleitores.fecha()
                return self.adiciona_eleitor()
            if event in ('REMOVER', 'ALTERAR'):
                if values['LISTA'] == []:
                    self.__tela_eleitores.mostra_mensagem('ERRO', "NENHUM ELEITOR FOI SELECIONADO")
                else:
                    self.__tela_eleitores.fecha()
                    return opcoes[event](lista[values['LISTA'][0]])

    def adiciona_eleitor(self):
        self.__tela_eleitores.tela_adiciona_eleitor([c.name for c in Categoria])
        while True:
            event, values = self.__tela_eleitores.abre()
            if event in ('CANCELAR', psg.WIN_CLOSED):
                self.__tela_eleitores.fecha()
                return self.mostra_tela_inicial()
            if event == 'SALVAR':
                nome = values['1'].strip().title()
                cpf = values['2'].strip()
                categoria = values['3'].strip()
                try:
                    if self.__ctrl_sistema.ctrl_urna.adiciona_eleitor(nome, cpf, categoria):
                        self.__tela_eleitores.mostra_mensagem('SUCESSO', 'ELEITOR ADICIONADO!')
                        self.__tela_eleitores.fecha()
                        return self.mostra_tela_inicial()
                except Exception as e:
                    self.__tela_eleitores.mostra_mensagem('ERRO', e)

    def remove_eleitor(self, cliente: list):
        if cliente is not None and cliente != []:
            self.__tela_eleitores.tela_remove_eleitor(cliente)
            while True:
                event, values = self.__tela_eleitores.abre()
                if event in ('CANCELAR', psg.WIN_CLOSED):
                    self.__tela_eleitores.fecha()
                    return self.mostra_tela_inicial()
                if event == 'CONFIRMAR':
                    try:
                        if self.__ctrl_sistema.ctrl_urna.remove_eleitor(cliente[1]):
                            self.__tela_eleitores.mostra_mensagem('SUCESSO', 'ELEITOR REMOVIDO!')
                            self.__tela_eleitores.fecha()
                            return self.mostra_tela_inicial()
                    except Exception as e:
                        self.__tela_eleitores.mostra_mensagem('ERRO', e)
        return self.mostra_tela_inicial()

    def altera_eleitor(self, cliente: list):
        if cliente is not None and cliente != []:
            self.__tela_eleitores.tela_altera_eleitor(cliente, [c.name for c in Categoria])
            while True:
                event, values = self.__tela_eleitores.abre()
                if event in ('CANCELAR', psg.WIN_CLOSED):
                    self.__tela_eleitores.fecha()
                    return self.mostra_tela_inicial()
                if event == 'SALVAR':
                    nome = values['1'].strip().title()
                    categoria = values['2'].strip()
                    try:
                        if self.__ctrl_sistema.ctrl_urna.altera_eleitor(nome, cliente[1], categoria):
                            self.__tela_eleitores.mostra_mensagem('SUCESSO', 'ELEITOR ALTERADO!')
                            self.__tela_eleitores.fecha()
                            return self.mostra_tela_inicial()
                    except Exception as e:
                        self.__tela_eleitores.mostra_mensagem('ERRO', e)
        return self.mostra_tela_inicial()

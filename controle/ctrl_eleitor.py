from limite.tela_eleitores import TelaEleitores
from entidade.eleitor import Eleitor
from entidade.categoria import Categoria
import PySimpleGUI as psg


class ControladorEleitores:

    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_eleitores = TelaEleitores()

    def mostra_tela_inicial(self):
        self.__tela_eleitores.tela_opcoes(self.__ctrl_sistema.ctrl_urna.lista_eleitores())
        opcoes = {'ADICIONAR': self.adiciona_eleitor,
                  'REMOVER': self.remove_eleitor,
                  'ALTERAR': self.altera_eleitor}
        while True:
            event, values = self.__tela_eleitores.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_eleitores.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            self.__tela_eleitores.fecha()
            return opcoes[event]()

    def adiciona_eleitor(self):
        self.__tela_eleitores.tela_adiciona_eleitor([c.name for c in Categoria])
        while True:
            event, values = self.__tela_eleitores.abre()
            if event in ('CANCELAR', psg.WIN_CLOSED):
                self.__tela_eleitores.fecha()
                return self.mostra_tela_inicial()
            if event == 'SALVAR':
                print(values)
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

    def remove_eleitor(self):
        cpf_eleitor = self.__tela_eleitores.pega_cpf_eleitor()
        for eleitor in self.__eleitores:
            if eleitor.cpf == cpf_eleitor:
                self.__eleitores.remove(eleitor)
                return self.__tela_eleitores.mostra_mensagem('\nELEITOR REMOVIDO COM SUCESSO')
        self.__tela_eleitores.mostra_mensagem('\nNÃO EXISTE ELEITOR CADASTRADO COM O CPF CONSULTADO!')

    def altera_eleitor(self):
        cpf_eleitor = self.__tela_eleitores.pega_cpf_eleitor()
        for eleitor in self.__eleitores:
            if eleitor.cpf == cpf_eleitor:
                dados_eleitor = self.__tela_eleitores.pega_dados_eleitor()
                dados_eleitor['categoria'] = self.__controlador_urna.controlador_categoria.selecionar_categoria()
                eleitor.nome = dados_eleitor['nome']
                eleitor.cpf = dados_eleitor['cpf']
                eleitor.categoria = dados_eleitor['categoria']
                return self.__tela_eleitores.mostra_mensagem('\nELEITOR ALTERADO COM SUCESSO')
        self.__tela_eleitores.mostra_mensagem('\nNÃO EXISTE ELEITOR CADASTRADO COM O CPF CONSULTADO!')

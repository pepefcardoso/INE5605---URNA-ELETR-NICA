import PySimpleGUI as psg


class TelaVotacao():
    def __init__(self):
        self.__window = None

    def tela_opcoes_inicial(self, turno: int):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Button(f'INICIAR VOTAÇÃO DO {turno}º TURNO', key='INICIAR')],
                  [psg.Button('VOLTAR', key='VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - VOTAÇÃO', size=(1080,720)).Layout(layout)

    def tela_opcoes_votacao(self, turno: int):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Button(f'INICIAR NOVO VOTO', key='INICIAR')],
                  [psg.Button(f'ENCERRAR VOTAÇÃO DO {turno}º TURNO', key='ENCERRAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - VOTAÇÃO', size=(1080,720)).Layout(layout)

    def tela_selecao_eleitor(self, nome: str = '', categoria: str = ''):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('DADOS DO ELEITOR')],
                  [psg.Text('CPF: '), psg.InputText(key='CPF')],
                  [psg.Submit('CONFIRMAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - VOTAÇÃO', size=(1080,720)).Layout(layout)

    def tela_votacao_encerrada(self, ):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('VOTAÇÕES ENCERRADAS!')],
                  [psg.Button('VOLTAR', key='VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - VOTAÇÃO', size=(1080,720)).Layout(layout)

    def tela_seleciona_voto(self):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('', key='NUMERO')],
                  [psg.Button('1', key='1'),psg.Button('2', key='2'),psg.Button('3', key='3')],
                  [psg.Button('4', key='4'),psg.Button('5', key='5'),psg.Button('6', key='6')],
                  [psg.Button('7', key='7'),psg.Button('8', key='8'),psg.Button('9', key='9')],
                  [psg.Button('0', key='0'),psg.Button('CORRIGIR'),psg.Button('CONFIRMAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - VOTAÇÃO', size=(1080,720)).Layout(layout)

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def atualiza_numero(self, numero:str):
        self.__window['NUMERO'].Update(numero)
        self.__window.Refresh()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

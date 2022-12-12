import PySimpleGUI as psg


class TelaSistema():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Button('ELEITORES', size=(15, 1))], [psg.Button('CANDIDATOS', size=(15, 1))],
                  [psg.Button('CATEGORIAS', size=(15, 1))], [psg.Button('CARGOS', size=(15, 1))],
                  [psg.Button('CHAPAS', size=(15, 1))], [psg.Button('CONFIGURAÇÕES', size=(15, 1))],
                  [psg.Button('VOTAÇÃO', size=(15, 1))], [psg.Button('RELATÓRIOS', size=(15, 1))],
                  [psg.Button('SAIR', size=(15, 1))]]
        layout = [[psg.Sizer(0, 350), psg.Column([[psg.Sizer(250, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC', layout, margins=(0, 0))

    def abre(self):
        button, values = self.__window.Read()
        return button, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

import PySimpleGUI as psg


class TelaCargos():
    def __init__(self):
        self.__window = None

    def tela_cargos(self, cargos: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CARGOS')],
                  [psg.Text(f"\n{x}") for x in cargos],
                  [psg.Button('SAIR')]]

        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CARGOS', layout, margins=(0,0))

    def abre(self):
        button, values = self.__window.Read()
        return button, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

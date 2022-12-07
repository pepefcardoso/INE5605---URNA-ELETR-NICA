import PySimpleGUI as psg


class TelaCargos():
    def __init__(self):
        self.__window = None

    def tela_cargos(self, cargos: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CARGOS')],
                  [psg.Text(f"\n{x}") for x in cargos],
                  [psg.Button('SAIR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CARGOS', size=(1080,720)).Layout(layout)

    def abre(self):
        button, values = self.__window.Read()
        return button, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

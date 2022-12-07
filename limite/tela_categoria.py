import PySimpleGUI as psg


class TelaCategoria():
    def __init__(self):
        self.__window = None

    def tela_categorias(self, categorias):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CATEGORIAS')],
                  [psg.Text(f"\n{x}") for x in categorias],
                  [psg.Button('SAIR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CATEGORIAS', size=(1080,720)).Layout(layout)

    def abre(self):
        button, values = self.__window.Read()
        return button, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

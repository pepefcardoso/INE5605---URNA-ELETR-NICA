import PySimpleGUI as psg


class TelaSistema():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Button('ELEITORES')], [psg.Button('CANDIDATOS')],
                  [psg.Button('CATEGORIAS')], [psg.Button('CARGOS')],
                  [psg.Button('CHAPAS')], [psg.Button('CONFIGURAÇÕES')],
                  [psg.Button('VOTAÇÃO')], [psg.Button('RELATÓRIOS')],
                  [psg.Button('SAIR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC', size=(1080,720)).Layout(layout)

    def abre_tela(self):
        button, values = self.__window.Read()
        return button, values

    def fecha_tela(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

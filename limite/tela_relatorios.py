import PySimpleGUI as psg


class TelaRelatorios():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'CPF', 'CATEGORIA']
        layout = [[psg.Button('1º TURNO')],
                  [psg.Button('2º TURNO')],
                  [psg.Cancel('VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - RELATÓRIOS', size=(1080,720)).Layout(layout)

    def tela_mostra_relatorios(self, lista_resultados: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'NÚMERO DE VOTOS', '%']
        layout = [[psg.Table(values=lista_resultados,
                             headings=headings,
                             key='LISTA',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(60,27,27),
                             num_rows=38,
                             enable_events=True)],
                   [psg.Button('VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - RELATÓRIOS', size=(1080,720)).Layout(layout)

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

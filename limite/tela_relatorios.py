import PySimpleGUI as psg


class TelaRelatorios():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'CPF', 'CATEGORIA']
        layout = [[psg.Button('1º TURNO', size=(15, 1))],
                  [psg.Button('2º TURNO', size=(15, 1))],
                  [psg.Cancel('VOLTAR', size=(15, 1))]]
        layout = [[psg.Sizer(0, 250), psg.Column([[psg.Sizer(250, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - RELATÓRIOS', layout, margins=(0, 0))

    def tela_mostra_relatorios(self, lista_resultados: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'NÚMERO DE VOTOS', '%']
        layout = [[psg.Table(values=lista_resultados,
                             headings=headings,
                             key='LISTA',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(30,16,16),
                             num_rows=30,
                             enable_events=True)],
                   [psg.Button('VOLTAR')]]
        layout = [[psg.Sizer(0, 350), psg.Column([[psg.Sizer(250, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - RELATÓRIOS', layout, margins=(0, 0))

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

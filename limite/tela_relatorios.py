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

    def tela_mostra_relatorios(self, resultados_1: list, resultados_2: list, resultados_3: list, resultados_4: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'NÚMERO DE VOTOS', '%']
        lista_1 = [psg.Table(values=resultados_1,
                             headings=headings,
                             key='LISTA_1',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(30,16,16),
                             enable_events=True)]
        lista_2 =[psg.Table(values=resultados_2,
                             headings=headings,
                             key='LISTA_2',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(30,16,16),
                             enable_events=True)]
        lista_3 =[psg.Table(values=resultados_3,
                             headings=headings,
                             key='LISTA_3',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(30,16,16),
                             enable_events=True)]
        lista_4 =[psg.Table(values=resultados_4,
                             headings=headings,
                             key='LISTA_4',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(30,16,16),
                             enable_events=True)]
        layout = [lista_1,
                  lista_2,
                  lista_3,
                  lista_4,
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

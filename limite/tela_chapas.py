import PySimpleGUI as psg


class TelaChapas():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self, lista_chapas: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['CÓDIGO', 'NOME']
        layout = [[psg.Table(values=lista_chapas,
                             headings=headings,
                             key='LISTA',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(30,30),
                             num_rows=15,
                             enable_events=True)],
                  [psg.Button('ADICIONAR'),
                   psg.Button('ALTERAR'),
                   psg.Button('REMOVER'),
                   psg.Button('VOLTAR')]]
        layout = [[psg.Sizer(0, 300), psg.Column([[psg.Sizer(300, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CHAPAS', layout, margins=(0,0))

    def tela_adiciona_chapa(self):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('- O CÓDIGO DEVE SER UM NÚMERO INTEIRO ENTRE 1 E 99')],
                  [psg.Text('CODIGO'), psg.InputText(key='1')],
                  [psg.Text('NOME'), psg.InputText(key='2')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ADICIONAR CHAPA', layout, margins=(0, 0))

    def tela_remove_chapa(self, chapa: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR A REMOÇÃO DA CHAPA:')],
                  [psg.Text(f'CODIGO: {chapa[0]}')],
                  [psg.Text(f'NOME: {chapa[1]}')],
                  [psg.Submit('CONFIRMAR'), psg.Cancel('CANCELAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - REMOVER CHAPA', layout, margins=(0, 0))

    def tela_altera_chapa(self, chapa:list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR ALTERAÇÃO DA CHAPA:')],
                  [psg.Text(f'CODIGO: {chapa[0]}')],
                  [psg.Text(f'NOME: '), psg.InputText(chapa[1], key='1')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ALTERAR CHAPA', layout, margins=(0, 0))

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

import PySimpleGUI as psg


class TelaEleitores():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self, lista_eleitores: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'CPF', 'CATEGORIA']
        layout = [[psg.Table(values=lista_eleitores,
                             headings=headings,
                             key='LISTA',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(20,20,20),
                             num_rows=20,
                             enable_events=True)],
                  [psg.Button('ADICIONAR'),
                   psg.Button('ALTERAR'),
                   psg.Button('REMOVER'),
                   psg.Button('VOLTAR')]]
        layout = [[psg.Sizer(0, 500), psg.Column([[psg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ELEITORES', layout, margins=(0, 0))

    def tela_adiciona_eleitor(self, categorias: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('NOME'), psg.InputText(key='1')],
                  [psg.Text('CPF'), psg.InputText(key='2')],
                  [psg.Text('CATEGORIA'), psg.Combo(categorias, key='3')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(400, 0)]] + layout, pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ADICIONAR ELEITOR', layout, margins=(0, 0))

    def tela_remove_eleitor(self, cliente: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR A REMOÇÃO DO ELEITOR:')],
                  [psg.Text(f'NOME: {cliente[0]}')],
                  [psg.Text(f'CPF: {cliente[1]}')],
                  [psg.Text(f'CATEGORIA: {cliente[2]}')],
                  [psg.Submit('CONFIRMAR'), psg.Cancel('CANCELAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(400, 0)]] + layout, pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - REMOVER ELEITOR', layout, margins=(0, 0))

    def tela_altera_eleitor(self, cliente:list, categorias:list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR ALTERAÇÃO DO ELEITOR:')],
                  [psg.Text('NOME'), psg.InputText(cliente[0], key='1')],
                  [psg.Text(f'CPF: {cliente[1]}')],
                  [psg.Text('CATEGORIA'), psg.Combo(categorias, cliente[2], key='2')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(400, 0)]] + layout, pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ALTERAR ELEITOR', layout, margins=(0, 0))

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

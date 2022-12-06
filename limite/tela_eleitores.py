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
                             col_widths=(60,27,27),
                             num_rows=38)],
                  [psg.Button('ADICIONAR'),
                   psg.Button('ALTERAR'),
                   psg.Button('REMOVER'),
                   psg.Button('VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ELEITORES', size=(1080,720)).Layout(layout)

    def tela_adiciona_eleitor(self, categories: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('NOME'), psg.InputText(key='1')],
                  [psg.Text('CPF'), psg.InputText(key='2')],
                  [psg.Text('CATEGORIA'), psg.Combo(categories, key='3')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ADICIONAR ELEITOR', size=(1080,720)).Layout(layout)

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

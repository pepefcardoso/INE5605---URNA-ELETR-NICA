import PySimpleGUI as psg


class TelaCandidatos():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self, lista_candidatos: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'CPF', 'CATEGORIA', 'NÚMERO', 'CHAPA', 'CARGO']
        layout = [[psg.Table(values=lista_candidatos,
                             headings=headings,
                             key='LISTA',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(19,19,19,19,19,19),
                             num_rows=38,
                             enable_events=True)],
                  [psg.Button('ADICIONAR'),
                   psg.Button('ALTERAR'),
                   psg.Button('REMOVER'),
                   psg.Button('VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CANDIDATOS', size=(1080,720)).Layout(layout)

    def tela_adiciona_candidato(self, chapas: list, cargos: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('- O CANDIDATO DEVE POSSUIR UM ELEITOR CADASTRADO COM SEU CPF')],
                  [psg.Text('CPF: '), psg.InputText(key='1')],
                  [psg.Text('NÚMERO: '), psg.InputText(key='2')],
                  [psg.Text('CHAPA: '), psg.Combo(chapas, key='3')],
                  [psg.Text('CARGO: '), psg.Combo(cargos, key='4')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ADICIONAR ELEITOR', size=(1080,720)).Layout(layout)

    def tela_remove_candidato(self, cliente: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR A REMOÇÃO DO ELEITOR:')],
                  [psg.Text(f'NOME: {cliente[0]}')],
                  [psg.Text(f'CPF: {cliente[1]}')],
                  [psg.Text(f'CATEGORIA: {cliente[2]}')],
                  [psg.Submit('CONFIRMAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - REMOVER ELEITOR', size=(1080,720)).Layout(layout)

    def tela_altera_candidato(self, cliente:list, categorias:list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR ALTERAÇÃO DO CLIENTE:')],
                  [psg.Text('NOME'), psg.InputText(cliente[0], key='1')],
                  [psg.Text(f'CPF: {cliente[1]}')],
                  [psg.Text('CATEGORIA'), psg.Combo(categorias, cliente[2], key='2')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ALTERAR ELEITOR', size=(1080,720)).Layout(layout)

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

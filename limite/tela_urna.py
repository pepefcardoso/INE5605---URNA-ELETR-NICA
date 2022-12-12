import PySimpleGUI as psg


class TelaUrna():
    def __init__(self):
        self.__window = None

    def init_config(self):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('----- REGRAS DE CONFIGURAÇÃO -----')],
                  [psg.Text('- O CÓDIGO DA URNA DEVE SER UM Nº INTEIRO ENTRE 1 E 99')],
                  [psg.Text('- O CÓDIGO DA URNA NÃO PODERÁ SER ALTERADO APÓS ESTA CONFIGURAÇÃO!')],
                  [psg.Text('- O Nº MÁXIMO DE ELEITORES E CANDIDATOS DEVE SER UM Nº INTEIRO ENTRE 1 E 100000')],
                  [psg.Text('')],
                  [psg.Text('CÓDIGO'), psg.InputText('10', key='codigo')],
                  [psg.Text('MÁXIMO DE ELEITORES'), psg.InputText('10', key='max_eleitores')],
                  [psg.Text('MÁXIMO DE CANDIDATOS'), psg.InputText('10', key='max_candidatos')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]

        layout = [[psg.Sizer(0, 300), psg.Column([[psg.Sizer(400, 0)]] + layout, pad=(0, 0))]]
        self.__window = psg.Window('CONFIGURAÇÃO URNA', layout, margins=(0, 0))

    def abre(self):
        button, values = self.__window.Read()
        return button, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)

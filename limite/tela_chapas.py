from abstract_tela import Tela

class TelaChapa(Tela):

    def mostra_tela(self):
        print('CHAPA')
        print('1 - Lista de Chapas.')
        print('2 - Adicionar Chapa.')
        print('3 - Remove Chapa.')

    def checa_numero(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = int(input(mensagem))
            try:
                if valor_lido not in inteiros_validos:
                    raise ValueError
                return valor_lido
            except ValueError:
            #parei aqui muito sono

    def pega_opcao(self):
        pass
from limite.abstract_tela import Tela

class TelaChapa(Tela):

    def mostra_tela_chapas(self):
        print('CHAPA')
        print('1 - Lista de Chapas')
        print('2 - Adicionar Chapa')
        print('3 - Remove Chapa')
        print('0 - Retornar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 0])
        return opcao

    def pega_opcao(self, mensagem: str = "", opcoes_validas = None):
        while True:
            valor_lido = input(mensagem)
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")
                if opcoes_validas:
                    print('Opções válidas: ', opcoes_validas)
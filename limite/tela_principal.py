from limite.abstract_tela import Tela


class TelaPrincipal(Tela):

    def mostra_tela_inicial(self):
        print('-' * 20)
        print('Urna Eletrônica UFSC')
        print('-' * 20)
        print('1 - Eleitores')
        print('2 - Candidatos')
        print('3 - Turno e Homologação')
        print('0 - Sair')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 0])
        return opcao
    
    def pega_opcao(self, mensagem: str = "", opcoes_validas: [] = None):
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

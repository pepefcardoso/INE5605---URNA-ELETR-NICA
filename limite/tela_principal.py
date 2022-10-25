class TelaPrincipal():

    def mostra_tela(self):
        print(('-' * 5), ' Urna Eletrônica UFSC ', ('-' * 5))
        print()
        print('1 - Eleitores')
        print('2 - Candidatos')
        print('3 - Chapas')
        print('4 - Cargos')
        print('5 - Registros')
        print('6 - Configurações')
        print('7 - Categoria Eleitor')
        print('0 - Sair')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 5, 6, 7, 0])
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

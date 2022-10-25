class TelaChapa():

    def mostra_menu_opcoes(self, nome_menu: str = '', opcoes_menu: list = [], msg_saida: str = ''):
        print(f'----- {nome_menu} -----\n')
        i = 1
        for opcao in opcoes_menu:
            print(f'{i} - {opcao}')
            i += 1
        print(f'0 - {msg_saida}\n')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])
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

    def mostra_chapa(self, nome: str):
        print(f'Chapa: {nome}')

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def pega_nome_chapa(self):
        while True:
            leitura = input("Insira o nome da Chapa: ")
            try:
                nome = str(leitura)
                if not isinstance(nome, str) or (len(leitura) < 1):
                    raise ValueError
                return nome
            except ValueError:
                print("Por favor, insira um nome válido")

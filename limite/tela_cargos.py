class TelaCargos():

    def abre_tela_inicial(self):
        print(('-' * 5), ' Cargos ', ('-' * 5))
        print('1 - Ver Lista de Cargos')
        print('0 - Voltar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 0])
        return opcao

    def mostra_cargo(self, dados_cargo):
        print(f"{dados_cargo.value} : {dados_cargo.name}")

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

    def pega_dado(self):
        while True:
            cargo = int(input('Número do Cargo: '))
            if cargo in [1, 2, 3, 4]:
                return {"cargo": cargo}

    def mostra_mensagem(self, msg):
        print(msg)

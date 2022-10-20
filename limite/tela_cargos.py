from limite.abstract_tela import Tela

class TelaCargos(Tela):

    def mostra_tela(self):
        print(('-' * 5), ' Cargos ', ('-' * 5))
        print('1 - Ver Lista de Cargos')
        print('2 - Adicionar Cargo')
        print('3 - Remover Cargo')
        print('0 - Voltar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3 , 0])
        return opcao

    def mostra_cargo(self, dados_cargo):
        print(f"Cargo: {dados_cargo.cargo}")

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
        cargo = str(input('Nome do Cargo: '))
        return {"cargo": cargo}

    def mostra_mensagem(self, msg: str):
        print(msg)

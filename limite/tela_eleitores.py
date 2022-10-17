from limite.abstract_tela import Tela


class TelaEleitores(Tela):

    def mostra_tela_eleitores(self):
        print('-' * 20)
        print('Eleitores')
        print('-' * 20)
        print('1 - Ver Lista de Eleitores')
        print('2 - Adicionar Eleitores')
        print('3 - Remover Eleitores')
        print('4 - Definir Máximo de Eleitores')
        print('0 - Voltar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def mostra_eleitor(self, dados_eleitor):
        print("\n")
        print(f"Nome: {dados_eleitor['nome']}")
        print(f"Cpf: {dados_eleitor['cpf']}")
        print(f"Categoria: {dados_eleitor['categoria']}")

    def pega_dados_eleitor(self):
        print("Dados do Eleitor")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        categoria = input("Categoria: ")
        return {'nome': nome, 'cpf': cpf, 'categoria': categoria}

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

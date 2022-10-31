from limite.abstract_tela import TelaAbstrata


class TelaCategoria(TelaAbstrata):

    def abre_tela_inicial(self):
        print(('-' * 5), ' Categoria ', ('-' * 5))
        print('1 - Ver Lista de Categorai')
        print('0 - Voltar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 0])
        return opcao

    def mostra_categoria(self, dados_categoria):
        print(f"{dados_categoria.value} : {dados_categoria.name}")

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
            categoria = int(input('Insira o Nº da Categoria: '))
            if categoria in [1, 2, 3]:
                return {"categoria": categoria}

    def mostra_mensagem(self, msg):
        print(msg)

    def mostra_entidade(self):
        pass

from limite.abstract_tela import TelaAbstrata


class TelaEleitores(TelaAbstrata):

    def mostra_menu_opcoes(self):
        super(TelaEleitores, self).mostra_menu_opcoes('ELEITORES',
                                                      ['LISTA DE ELEITORES', 'ADICIONAR ELEITORES', 'REMOVER ELEITORES', 'ALTERAR ELEITOR'],
                                                      'VOLTAR AO MENU INICIAL')

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

    def pega_opcao(self):
        super(TelaEleitores, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])

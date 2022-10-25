from limite.abstract_tela import TelaAbstrata


class TelaEleitores(TelaAbstrata):

    def mostra_menu_opcoes(self):
        super(TelaEleitores, self).mostra_menu_opcoes('ELEITORES',
                                                      ['LISTA DE ELEITORES', 'ADICIONAR ELEITORES', 'REMOVER ELEITORES', 'ALTERAR ELEITOR'],
                                                      'VOLTAR AO MENU INICIAL')

    def pega_opcao(self):
        opcao = super(TelaEleitores, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def mostra_entidade(self, dados_eleitor):
        super(TelaEleitores, self).mostra_entidade(dados_eleitor)

    def pega_dados_eleitor(self):
        print("Dados do Eleitor")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        categoria = input("Categoria: ")
        return {'nome': nome, 'cpf': cpf, 'categoria': categoria}

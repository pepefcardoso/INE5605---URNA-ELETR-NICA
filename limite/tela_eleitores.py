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

    def mostra_mensagem(self, mensagem):
        super(TelaEleitores, self).mostra_mensagem(mensagem)

    def pega_dados_eleitor(self):
        print("\nDados do Eleitor")
        while True:
            nome_lido = input('Nome: ')
            cpf_lido = input('CPF: ')
            categoria_lida = input('Categoria: ')
            try:
                nome = str(nome_lido)
                cpf = str(cpf_lido)
                categoria = str(categoria_lida)
                if (not isinstance(nome, str) or 
                    not isinstance(cpf, str) or 
                    not isinstance(categoria, str) or 
                    len(nome_lido) < 1 or 
                    len(cpf_lido) != 11 or 
                    len(categoria_lida) < 1):
                    raise ValueError
                return {'nome': nome, 'cpf': cpf, 'categoria': categoria}
            except ValueError:
                print('Dados incorretos, tente novamente!')

    def pega_cpf_eleitor(self):
        while True:
            cpf_consulta = input('CPF: ')
            try:
                cpf = str(cpf_consulta)
                if (not isinstance(cpf, str) or
                    len(cpf) < 11):
                    raise ValueError
                return cpf
            except ValueError:
                print('CPF inválido, tente novamente!')

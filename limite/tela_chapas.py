from limite.abstract_tela import TelaAbstrata


class TelaChapa(TelaAbstrata):

    def mostra_menu_opcoes(self):
        super(TelaChapa, self).mostra_menu_opcoes('CHAPAS',
                                                      ['LISTA DE CHAPAS', 'ADICIONAR CHAPA', 'REMOVER CHAPA', 'ALTERAR CHAPA'],
                                                      'VOLTAR AO MENU INICIAL')

    def pega_opcao(self):
        opcao = super(TelaChapa, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def mostra_entidade(self, nome_chapa):
        super(TelaChapa, self).mostra_entidade(nome_chapa)

    def mostra_mensagem(self, mensagem):
        super(TelaChapa, self).mostra_mensagem(mensagem)

    def pega_nome_chapa(self):
        while True:
            nome_consulta = input('Chapa: ')
            try:
                nome_chapa = str(nome_consulta)
                if (not isinstance(nome_chapa, str) or
                    len(nome_chapa) < 1):
                    raise ValueError
                return nome_chapa
            except ValueError:
                print('Chapa inválida, tente novamente!')

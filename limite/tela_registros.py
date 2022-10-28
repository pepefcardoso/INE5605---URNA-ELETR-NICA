from limite.abstract_tela import TelaAbstrata


class TelaRegistros(TelaAbstrata):
    def abre_tela_inicial(self):
        super(TelaRegistros, self).abre_tela_inicial('REGISTROS',
                                                      ['REGISTROS GERAIS', 'REGISTROS 1º TURNO', 'REGISTROS 2º TURNO'],
                                                      'VOLTAR AO MENU INICIAL')

    def abre_tela_registros(self):
        pass

    def pega_opcao(self):
        opcao = super(TelaRegistros, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 0])
        return opcao

    def mostra_entidade(self, dados):
        super(TelaRegistros, self).mostra_entidade(dados)

    def mostra_mensagem(self, mensagem):
        super(TelaRegistros, self).mostra_mensagem(mensagem)

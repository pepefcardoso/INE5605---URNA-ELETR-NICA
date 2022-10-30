from limite.abstract_tela import TelaAbstrata


class TelaRegistros(TelaAbstrata):
    def abre_tela_inicial(self):
        super(TelaRegistros, self).abre_tela_inicial('REGISTROS',
                                                      ['REGISTROS 1º TURNO', 'REGISTROS 2º TURNO'],
                                                      'VOLTAR AO MENU INICIAL')

    def abre_tela_registros(self):
        pass

    def pega_opcao(self):
        opcao = super(TelaRegistros, self).pega_opcao('Escolha uma opção: ', [1, 2, 0])
        return opcao

    def mostra_entidade(self, dados):
        super(TelaRegistros, self).mostra_entidade(dados)

    def mostra_mensagem(self, mensagem):
        super(TelaRegistros, self).mostra_mensagem(mensagem)

    def abre_tela_registros(self, turno):
        print(f'\n----- REGISTROS {turno}º TURNO -----\n')
        print('1 - RESULTADOS GERAIS')
        print('\n0 - VOLTAR\n')

    def pega_opcao_registro(self):
        while True:
            opcoes_validas = [1, 0]
            valor_lido = input('Insira a opção desejada: ')
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")

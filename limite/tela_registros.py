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

    def abre_tela_resultados_gerais(self, turno, dados_reitor, dados_grad, dados_pesq, dados_ext):
        if turno == 1:
            print('\n----- RESULTADOS 1º TURNO -----\n')
        elif turno == 2:
            print('\n----- RESULTADOS 2º TURNO -----\n')
        else:
            print('TURNO INVÁLIDO')
            return
        print('----- RESULTADOS REITOR -----\n')
        for key in dados_reitor:
            print(f'{key} - {dados_reitor[key][1]} ({dados_reitor[key][0]}) - {dados_reitor[key][2]} VOTOS')
        print('\n----- RESULTADOS PRÓ-REITOR GRADUAÇÃO -----\n')
        for key in dados_grad:
            print(f'{key} - {dados_grad[key][1]} ({dados_grad[key][0]}) - {dados_grad[key][2]} VOTOS')
        print('\n----- RESULTADOS PRÓ-REITOR PESQUISA -----\n')
        for key in dados_pesq:
            print(f'{key} - {dados_pesq[key][1]} ({dados_pesq[key][0]}) - {dados_pesq[key][2]} VOTOS')
        print('\n----- RESULTADOS PRÓ-REITOR EXTENSÃO -----\n')
        for key in dados_ext:
            print(f'{key} - {dados_ext[key][1]} ({dados_ext[key][0]}) - {dados_ext[key][2]} VOTOS')

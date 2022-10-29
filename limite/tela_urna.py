from limite.abstract_tela import TelaAbstrata


class TelaUrna(TelaAbstrata):

    def pega_config(self):
        print('\n----- CONFIGURAÇÃO URNA UFSC -----\n')
        print('----- REGRAS DE CONFIGURAÇÃO -----\n')
        print(' - O CÓDIGO DA URNA DEVE SER UM Nº INTEIRO ENTRE 1 E 99')
        print(' - O CÓDIGO DA URNA NÃO PODERÁ SER ALTERADO APÓS ESTA CONFIGURAÇÃO!')
        print(' - O Nº MÁXIMO DE ELEITORES E CANDIDATOS DEVE SER UM Nº INTEIRO ENTRE 1 E 100000\n')
        while True:
            codigo_lido = input('Insira o código da urna: ')
            max_eleitores_lido = input('Insira o Nº máximo de eleitores permitido: ')
            max_candidatos_lido = input('Insira o Nº máximo de candidato permitido: ')
            try:
                codigo = int(codigo_lido)
                max_eleitores = int(max_eleitores_lido)
                max_candidatos = int(max_candidatos_lido)
                if (not isinstance(codigo, int) or
                    not isinstance(max_eleitores, int) or
                    not isinstance(max_candidatos, int) or
                    (codigo not in range(1, 100)) or
                    (max_eleitores not in range(1, 100001)) or
                    (max_candidatos not in range(1, 100001))):
                    raise ValueError
                else:
                    print('\nURNA CONFIGURADA COM SUCESSO!\n')
                    return {'codigo': codigo, 'turno': 1, 'max_eleitores': max_eleitores, 'max_candidatos': max_candidatos}
            except ValueError:
                print('\nA CONFIGURAÇÃO FOI FEITA INCORRETAMENTE, TENTE NOVAMENTE\n')

    def abre_tela_inicial(self):
        super(TelaUrna, self).abre_tela_inicial('URNA ELETRÔNICA UFSC',
                                                ['ELEITORES', 'CANDIDATOS',
                                                'CHAPAS', 'CARGOS',
                                                'CATEGORIAS', 'REGISTROS',
                                                'CONFIGURAÇÕES', 'VOTAÇÃO'],
                                                'ENCERRAR SESSÃO')

    def pega_opcao(self):
        opcao = super(TelaUrna, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 5, 6, 7, 8, 0])
        return opcao

    def mostra_entidade(self, dados_eleitor):
        pass

    def mostra_mensagem(self, mensagem):
        super(TelaUrna, self).mostra_mensagem(mensagem)

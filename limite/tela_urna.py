from limite.abstract_tela import TelaAbstrata


class TelaUrna(TelaAbstrata):

    def tela_pega_config(self):
        print('\n----- CONFIGURAÇÃO URNA UFSC -----\n')
        print('----- REGRAS DE CONFIGURAÇÃO -----\n')
        print(' - O CÓDIGO DA URNA DEVE SER UM Nº INTEIRO ENTRE 1 E 99')
        print(' - O TURNO DA ELEIÇÃO DEVE SER 1 OU 2')
        print(' - O Nº MÁXIMO DE ELEITORES E CANDIDATOS DEVE SER UM INTEIRO MAIOR QUE 0\n')
        while True:
            codigo_lido = input('Insira o código da urna: ')
            turno_lido = input('Insira o turno da eleição: ')
            max_eleitores_lido = input('Insira o Nº máximo de eleitores permitido: ')
            max_candidatos_lido = input('Insira o Nº máximo de candidato permitido: ')
            try:
                codigo = int(codigo_lido)
                turno = int(turno_lido)
                max_eleitores = int(max_eleitores_lido)
                max_candidatos = int(max_candidatos_lido)
                if (not isinstance(codigo, int) or
                    not isinstance(turno, int) or
                    not isinstance(max_eleitores, int) or
                    not isinstance(max_candidatos, int) or
                    (codigo < 1 or codigo > 99) or
                    (turno < 1 or turno > 2) or
                    max_eleitores < 1 or
                    max_candidatos < 1):
                    raise ValueError
                else:
                    print('\nURNA CONFIGURADA COM SUCESSO!\n')
                    return {'codigo': codigo, 'turno': turno, 'max_eleitores': max_eleitores, 'max_candidatos': max_candidatos}
            except ValueError:
                print('\nA CONFIGURAÇÃO FOI FEITA INCORRETAMENTE, TENTE NOVAMENTE\n')

    def mostra_menu_opcoes(self):
        super(TelaUrna, self).mostra_menu_opcoes('URNA ELETRÔNICA UFSC',
                                                      ['ELEITORES', 'CANDIDATOS', 'CHAPAS', 'CARGOS', 'CATEGORIAS', 'REGISTROS', 'CONFIGURAÇÕES'],
                                                      'ENCERRAR SESSÃO')

    def pega_opcao(self):
        opcao = super(TelaUrna, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 5, 6, 7, 0])
        return opcao

    def mostra_entidade(self, dados_eleitor):
        pass

    def mostra_mensagem(self, mensagem):
        super(TelaUrna, self).mostra_mensagem(mensagem)

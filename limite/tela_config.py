from limite.abstract_tela import TelaAbstrata

class TelaConfig(TelaAbstrata):

    def abre_tela_inicial(self):
        super(TelaConfig, self).abre_tela_inicial('CONFIGURAÇÃO',
                                                      ['VER CONFIGURAÇÕES', 
                                                       'ALTERAR CÓDIGO DA URNA', 
                                                       'ALTERAR TURNO DE ELEIÇÃO', 
                                                       'ALTERAR Nº MÁXIMO DE ELEITORES', 
                                                       'ALTERAR Nº MÁXIMO DE CANDIDATOS',
                                                       'INICIAR ELEIÇÃO'],
                                                      'VOLTAR AO MENU INICIAL')

    def pega_opcao(self):
        opcao = super(TelaConfig, self).pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 5, 6, 0])
        return opcao

    def mostra_entidade(self, dados_urna):
        super(TelaConfig, self).mostra_entidade(dados_urna)

    def mostra_mensagem(self, mensagem):
        super(TelaConfig, self).mostra_mensagem(mensagem)

    def pega_atributo(self, atributo, valor_atributo_atual, opcoes_validas):
        print(f'{atributo} atual: {valor_atributo_atual}')
        while True:
            valor_lido = input(f'Insira o novo valor de {atributo}: ')
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")

from limite.abstract_tela import TelaAbstrata


class TelaVoto(TelaAbstrata):
    
    def abre_tela_inicial(self):
        super(TelaVoto, self).abre_tela_inicial('ELEIÇÕES UFSC',
                                                      ['INICIAR VOTO'],
                                                      'ENCERRAR ELEIÇÃO')

    def pega_opcao(self):
        opcao = super(TelaVoto, self).pega_opcao('Escolha uma opção: ', [1, 0])
        return opcao

    def mostra_entidade(self, dados):
        super(TelaVoto, self).mostra_entidade(dados)

    def mostra_mensagem(self, mensagem):
        super(TelaVoto, self).mostra_mensagem(mensagem)

    def pegar_cpf_eleitor(self):
        print('\n----- ELEIÇÕES UFSC -----\n')
        while True:
            cpf_lido = input('Insira o CPF do Eleitor: ')
            try:
                cpf_eleitor = str(eleitor_lido)
                return cpf_eleitor
            except ValueError:
                return False

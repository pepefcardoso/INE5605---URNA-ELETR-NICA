from limite.tela_padrao import TelaPadrao


class TelaVoto(TelaPadrao):
    
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
        valor = input('Insira o CPF do Eleitor: ')
        if (len(valor) == 11 and isinstance(valor, str)):
            return valor
        return

    def pega_voto(self, nome_cargo):
        while True:
            num_voto_lido = input(f'\nInsira o seu voto para {nome_cargo}: ')
            try:
                num_voto = int(num_voto_lido)
                if num_voto in range(1, 99):
                    return num_voto
                else:
                    return 99
            except ValueError:
                return 00

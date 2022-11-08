from limite.tela_padrao import TelaPadrao


class TelaEleitores(TelaPadrao):

    def abre_tela_inicial(self, nome_menu: str = '', opcoes_menu: list = [], msg_saida: str = ''):
        super().abre_tela_inicial(nome_menu, opcoes_menu, msg_saida)

    def pega_opcao(self, mensagem: str = "", opcoes_validas: [] = None):
        opcao = super().pega_opcao(mensagem, opcoes_validas)
        return opcao

    def mostra_entidade(self, dados_eleitor):
        super().mostra_entidade(dados_eleitor)

    def mostra_mensagem(self, mensagem):
        super().mostra_mensagem(mensagem)

    def pega_dados_eleitor(self):
        print("\nDados do Eleitor")
        while True:
            nome_lido = input('Nome: ')
            cpf_lido = input('CPF: ')
            try:
                nome = str(nome_lido)
                cpf = str(cpf_lido)
                if (not isinstance(nome, str) or 
                    not isinstance(cpf, str) or 
                    len(nome_lido) < 1 or 
                    len(cpf_lido) != 11):
                    raise ValueError
                return {'nome': nome.title(), 'cpf': cpf}
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

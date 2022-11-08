from limite.tela_padrao import TelaPadrao


class TelaChapa(TelaPadrao):

    def abre_tela_inicial(self, nome_menu: str = '', opcoes_menu: list = [], msg_saida: str = ''):
        super().abre_tela_inicial(nome_menu, opcoes_menu, msg_saida)

    def pega_opcao(self, mensagem: str = "", opcoes_validas: list = []):
        opcao = super().pega_opcao(mensagem, opcoes_validas)
        return opcao

    def mostra_entidade(self, nome_chapa):
        super().mostra_entidade(nome_chapa)

    def mostra_mensagem(self, mensagem):
        super().mostra_mensagem(mensagem)

    def pega_nome_chapa(self):
        while True:
            nome_consulta = input('Chapa: ')
            try:
                nome_chapa = str(nome_consulta)
                if (not isinstance(nome_chapa, str) or
                    len(nome_chapa) < 1):
                    raise ValueError
                return nome_chapa.title()
            except ValueError:
                print('Chapa inválida, tente novamente!')

    def pega_chapa_num(self, dict_chapas: dict = {}, opcoes_validas: list = []):
        for key in dict_chapas:
            print(f'{key} - {dict_chapas[key]}')
        while True:
            num_chapa_lido = input('Insira o Nº da Chapa escolhida: ')
            try:
                num_chapa = int(num_chapa_lido)
                if opcoes_validas and num_chapa not in opcoes_validas:
                    raise ValueError
                return num_chapa
            except ValueError:
                print("\nTente uma opção válida ou digite 0 para sair!.\n")

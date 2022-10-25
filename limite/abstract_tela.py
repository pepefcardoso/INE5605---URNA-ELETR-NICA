from abc import ABC, abstractmethod


class TelaAbstrata(ABC):

    @abstractmethod
    def mostra_menu_opcoes(self, nome_menu: str = '', opcoes_menu: list = [], msg_saida: str = ''):
        print(f'----- {nome_menu} -----\n')
        i = 1
        for opcao in opcoes_menu:
            print(f'{i} - {opcao}')
            i += 1
        print(f'0 - {msg_saida}\n')
        opcao = self.pega_opcao()
        return opcao

    @abstractmethod
    def pega_opcao(self, mensagem: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")

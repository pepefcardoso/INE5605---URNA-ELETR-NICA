from abc import ABC, abstractmethod


class Tela(ABC):
    @abstractmethod
    def pega_opcao(self):
        pass

    # Vamos padrozinar essa função, não precisa colocar cada um com um nome personalizado;
    @abstractmethod
    def mostra_tela(self, nome_menu: str = '', opcoes_menu: list = [], msg_saida: str = ''):
        print(f'----- {nome_menu} -----\n')
        for opcao in opcoes_menu:
            i = 1
            print(f'{i} - {opcao}')
            i += 1
        print(f'0 - {msg_saida}')

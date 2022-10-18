from abc import ABC, abstractmethod


class Tela(ABC):
    @abstractmethod
    def pega_opcao(self):
        pass

    # Vamos padrozinar essa função, não precisa colocar cada um com um nome personalizado;
    '''
    @abstractmethod
    def mostra_tela(self):
        pass'''

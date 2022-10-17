from abc import ABC, abstractmethod


class Tela(ABC):
    @abstractmethod
    def pega_opcao(self):
        pass

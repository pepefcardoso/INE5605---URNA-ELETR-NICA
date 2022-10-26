from limite.tela_config import TelaConfig


class ControladorConfig:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_config = TelaConfig()

    def mostra_tela_config(self):
        dados_config = self.__tela_config.tela_pega_config()

    def mostra_tela_inicial(self):
        pass

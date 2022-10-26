from limite.tela_config import TelaConfig


class ControladorConfig:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_config = TelaConfig()

    def mostra_tela_config(self):
        dados_config = self.__tela_config.tela_pega_config()

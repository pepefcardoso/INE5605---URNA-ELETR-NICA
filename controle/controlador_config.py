from limite.tela_config import TelaConfig


class ControladorConfig:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_config = TelaConfig()

    def mostra_tela_inicial(self):
        opcoes = {1: self.lista_config, 
                 2: self.altera_codigo, 
                 3: self.altera_turno, 
                 4: self.altera_max_eleitores, 
                 5: self.altera_max_candidatos}
        while True:
            self.__tela_config.abre_tela_inicial()
            opcao = self.__tela_config.pega_opcao()
            if opcao == 0:
                break
            opcoes[opcao]()

    def lista_config(self):
        codigo = self.__controlador_urna.urna.codigo
        turno = self.__controlador_urna.urna.turno
        max_eleitores = self.__controlador_urna.urna.max_eleitores
        max_candidatos = self.__controlador_urna.urna.max_candidatos
        dados_urna = {'codigo': codigo,
                      'turno': turno,
                      'max_eleitores': max_eleitores,
                      'max_candidatos': max_candidatos}
        self.__tela_config.mostra_entidade(dados_urna)

    def altera_codigo(self):
        pass

    def altera_turno(self):
        pass

    def altera_max_eleitores(self):
        pass

    def altera_max_candidatos(self):
        pass

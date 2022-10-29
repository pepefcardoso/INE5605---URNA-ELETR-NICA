from limite.tela_config import TelaConfig


class ControladorConfig:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_config = TelaConfig()

    def mostra_tela_inicial(self):
        opcoes = {1: self.lista_config, 
                 2: self.altera_max_eleitores, 
                 3: self.altera_max_candidatos}
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

    def altera_max_eleitores(self):
        valor = self.__tela_config.pega_atributo('Nº Máximo de Eleitores', 
                                         self.__controlador_urna.urna.max_eleitores, 
                                         range(1, 100000))
        if valor < len(self.__controlador_urna.controlador_eleitores.eleitores):
            self.__tela_config.mostra_mensagem('\nVALOR INFERIOR AO Nº DE ELEITORES JÁ CADASTRADOS!\n')
            return
        else:
            self.__tela_config.mostra_mensagem('\nNº MÁXIMO DE ELEITORES ALTERADO COM SUCESSC\n')
            self.__controlador_urna.urna.max_eleitores = valor

    def altera_max_candidatos(self):
        valor = self.__tela_config.pega_atributo('Nº Máximo de Candidatos', 
                                         self.__controlador_urna.urna.max_candidatos, 
                                         range(1, 100000))
        if valor < len(self.__controlador_urna.controlador_candidatos.candidatos):
            self.__tela_config.mostra_mensagem('\nVALOR INFERIOR AO Nº DE CANDIDATOS JÁ CADASTRADOS!\n')
            return
        else:
            self.__tela_config.mostra_mensagem('\nNº MÁXIMO DE CANDIDATOS ALTERADO COM SUCESSC\n')
            self.__controlador_urna.urna.max_candidatos = valor

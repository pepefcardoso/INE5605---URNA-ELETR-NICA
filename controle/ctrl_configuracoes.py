from limite.tela_configuracoes import TelaConfiguracoes
import PySimpleGUI as psg


class ControladorConfiguracoes():

    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_configuracoes = TelaConfiguracoes()

    def mostra_tela_inicial(self):
        if self.__ctrl_sistema.ctrl_urna.urna.turno == 3:
            self.__tela_configuracoes.mostra_mensagem('AVISO', 'ELEIÇÕES ENCERRADAS')
            return self.__ctrl_sistema.abre_menu_inicial()
        max_eleitores = str(self.__ctrl_sistema.ctrl_urna.urna.max_eleitores)
        max_candidatos = str(self.__ctrl_sistema.ctrl_urna.urna.max_candidatos)
        self.__tela_configuracoes.tela_configuracoes(max_eleitores, max_candidatos)
        while True:
            event, values = self.__tela_configuracoes.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_configuracoes.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'ALTERAR':
                self.altera_configuracoes(values['ELEITORES'], values['CANDIDATOS'])

    def altera_configuracoes(self, max_eleitores: str, max_candidatos: str):
        if (max_eleitores is not None and 
            max_candidatos is not None and
            isinstance(max_eleitores, str) and
            isinstance(max_candidatos, str)):
            try:
                if self.__ctrl_sistema.ctrl_urna.altera_configuracoes(max_eleitores, max_candidatos):
                    self.__tela_configuracoes.atualiza_dados(max_eleitores, max_candidatos)
                    return self.__tela_configuracoes.mostra_mensagem('SUCESSO', 'ALTERAÇÃO CONCLUÍDA!')
            except Exception as e:
                self.__tela_configuracoes.mostra_mensagem('ERRO', e)
        return self.__tela_configuracoes.mostra_mensagem('AVISO', 'ALTERAÇÃO NÃO CONCLUÍDA!')

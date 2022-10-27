from limite.tela_voto import TelaVoto
from entidade.voto import Voto


class ControladorVotos():
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_voto = TelaVoto()

    def mostra_tela_inicial(self):
        while True:
            self.__tela_voto.abre_tela_inicial()
            opcao = self.__tela_voto.pega_opcao()
            if opcao == 0:
                break
            elif opcao == 1:
                self.votar()

    def votar(self):
        eleitor = self.__tela_voto.seleciona_eleitor()
        if eleitor == False:
            return
        

    def seleciona_eleitor(self):
        while True:
            cpf_eleitor = self.__tela_voto.abre_tela_inicial()
            for eleitor in self.__controlador_urna.controlador_eleitores.eleitores:
                if eleitor.cpf == cpf_eleitor:
                    self.__tela_voto.mostra_mensagem(f'\nBem vindo {eleitor.nome}!\n')
                    return eleitor
                elif cpf_eleitor == False:
                    self.__tela_voto.mostra_mensagem(f'\nCPF inválido!\n')
                    self.__tela_voto.mostra_mensagem(f'\nDigite 1 para tentar novamente ou 0 para encerrar tentativa!\n')
                    opcao = self.__tela_voto.pega_opcao()
                    if opcao == 0:
                        return False

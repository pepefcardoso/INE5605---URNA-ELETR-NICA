from limite.tela_voto import TelaVoto
from entidade.voto import Voto
from entidade.eleitor import Eleitor


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
        eleitor = self.seleciona_eleitor()
        if isinstance(eleitor, Eleitor):
            print('deu certo estou no método votar')
        else:
            return
        

    def seleciona_eleitor(self):
        while True:
            cpf_eleitor = self.__tela_voto.pegar_cpf_eleitor()
            for eleitor in self.__controlador_urna.controlador_eleitores.eleitores:
                if eleitor.cpf == cpf_eleitor:
                    self.__tela_voto.mostra_mensagem(f'\nBem vindo {eleitor.nome}!\n')
                    return eleitor
            self.__tela_voto.mostra_mensagem(f'\nCPF inválido!')
            self.__tela_voto.mostra_mensagem(f'Digite 1 para tentar novamente ou 0 para encerrar tentativa!\n')
            opcao = self.__tela_voto.pega_opcao()
            if opcao == 0:
                return

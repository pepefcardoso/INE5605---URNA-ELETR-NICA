from limite.tela_votacao import TelaVotacao
from entidade.voto import Voto
from entidade.eleitor import Eleitor
from entidade.cargo import Cargo
import PySimpleGUI as psg


class ControladorVotacao():
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_votacao = TelaVotacao()

    def mostra_tela_inicial(self):
        self.__tela_votacao.tela_opcoes_inicial(self.__ctrl_sistema.ctrl_urna.urna.turno)
        while True:
            event, values = self.__tela_votacao.abre()
            if event in (psg.WIN_CLOSED, 'VOLTAR'):
                self.__tela_votacao.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'INICIAR':
                self.__tela_votacao.fecha()
                return self.mostra_tela_inicial_votacao()

    def mostra_tela_inicial_votacao(self):
        self.__tela_votacao.tela_opcoes_votacao(self.__ctrl_sistema.ctrl_urna.urna.turno)
        while True:
            event, values = self.__tela_votacao.abre()
            if event in (psg.WIN_CLOSED, 'ENCERRAR'):
                self.__tela_votacao.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'INICIAR':
                self.__tela_votacao.fecha()
                return self.iniciar_votacao()

    def iniciar_votacao(self):
        eleitor = self.selecionar_eleitor()
        if not eleitor:
            return self.mostra_tela_inicial_votacao()
        votos = []
        for i in range(1,5):
            while True:
                num_voto = self.selecionar_voto(Cargo(i))
                if self.confirmar_voto(num_voto, Cargo(i)):
                    votos.append(num_voto)
                    break
        print(votos)
        return votos

    def selecionar_eleitor(self):
        self.__tela_votacao.tela_selecao_eleitor()
        while True:
            event, values = self.__tela_votacao.abre()
            if event in (psg.WIN_CLOSED, 'CANCELAR'):
                self.__tela_votacao.fecha()
                return False
            if event == 'CONFIRMAR':
                try:
                    eleitor = self.__ctrl_sistema.ctrl_urna.busca_eleitor_cpf(values['CPF'])
                    self.__tela_votacao.mostra_mensagem('AVISO', (f'\nNOME: {eleitor.nome}\nCPF: {eleitor.cpf}\nCATEGORIA: {eleitor.categoria.name}'))
                    self.__tela_votacao.fecha()
                    return eleitor
                except Exception as e:
                    self.__tela_votacao.mostra_mensagem('ERRO', e)

    def selecionar_voto(self, cargo: Cargo):
        self.__tela_votacao.tela_seleciona_voto(cargo.name)
        num = ''
        while True:
            event, values = self.__tela_votacao.abre()
            if event == psg.WIN_CLOSED:
                continue
            if event == 'CORRIGIR':
                num = ''
                self.__tela_votacao.atualiza_numero(num)
            if len(num) <= 1 and event.isnumeric():
                num += event
                self.__tela_votacao.atualiza_numero(num)
            if event == 'CONFIRMAR':
                self.__tela_votacao.fecha()
                return num

    def confirmar_voto(self, num: str, cargo: Cargo):
        candidato = self.__ctrl_sistema.ctrl_urna.busca_candidato_numero_cargo(num, cargo)
        if not candidato:
            self.__tela_votacao.fecha()
            return False
        self.__tela_votacao.tela_confirma_voto(cargo.name, 
                                               num, 
                                               candidato[0], 
                                               candidato[1])
        while True:
            event, values = self.__tela_votacao.abre()
            if event in('CANCELAR',psg.WIN_CLOSED):
                self.__tela_votacao.fecha()
                return False
            if event == 'CONFIRMAR':
                self.__tela_votacao.fecha()
                return True

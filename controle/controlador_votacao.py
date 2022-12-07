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
        self.__tela_votacao.tela_votacao()
        numero = ''
        while True:
            event, values = self.__tela_votacao.abre()
            if event in (psg.WIN_CLOSED, 'CONFIRMAR'):
                self.__tela_votacao.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'CORRIGIR':
                numero = ''
                self.__tela_votacao.atualiza_numero(numero)
            if len(numero) <= 1 and event.isnumeric():
                numero += event
                self.__tela_votacao.atualiza_numero(numero)







    '''def mostra_tela_inicial(self):
        while True:
            if self.__controlador_urna.urna.turno == 0:
                self.__tela_voto.mostra_mensagem('\nAS ELEIÇÕES JÁ FORAM ENCERRADAS!')
                break
            self.__tela_voto.abre_tela_inicial()
            opcao = self.__tela_voto.pega_opcao()
            if opcao == 0:
                if self.encerra_votação() == 1:
                    self.__tela_voto.mostra_mensagem(f'\n{self.__controlador_urna.urna.turno}º TURNO DA ELEIÇÃO ENCERRADO')
                    if self.__controlador_urna.urna.turno == 1:
                        self.__controlador_urna.urna.turno = 2
                    elif self.__controlador_urna.urna.turno == 2:
                        self.__controlador_urna.urna.turno = 0
                    break                    
            elif opcao == 1:
                self.votar()

    def votar(self):
        eleitor = self.seleciona_eleitor()
        turno = self.__controlador_urna.urna.turno
        if not self.testar_eleitor_votante(eleitor):
            return False
        elif eleitor == False:
            return False
        else:
            voto_reitor = self.seleciona_voto(Cargo(1))
            voto_grad = self.seleciona_voto(Cargo(2))
            voto_pesq = self.seleciona_voto(Cargo(3))
            voto_ext = self.seleciona_voto(Cargo(4))
            voto = Voto(voto_reitor, voto_grad, voto_pesq, voto_ext, eleitor.categoria, self.__controlador_urna.urna.turno)
            self.__controlador_urna.urna.lista_votos.append(voto)
            if turno == 1:
                self.__controlador_urna.urna.votantes_1_turno.append(eleitor)
            elif turno == 2:
                self.__controlador_urna.urna.votantes_2_turno.append(eleitor)
            self.__tela_voto.mostra_mensagem(f'\nSEUS VOTOS FORAM COMPUTADOS, OBRIGADO!')
            return True

    def seleciona_eleitor(self):
        while True:
            cpf_eleitor = self.__tela_voto.pegar_cpf_eleitor()
            for eleitor in self.__controlador_urna.controlador_eleitores.eleitores:
                if eleitor.cpf == cpf_eleitor:
                    self.__tela_voto.mostra_mensagem(f'\nBem vindo {eleitor.nome}!')
                    return eleitor
            self.__tela_voto.mostra_mensagem(f'\nCPF inválido!')
            self.__tela_voto.mostra_mensagem(f'Digite 1 para tentar novamente ou 0 para encerrar tentativa!\n')
            opcao = self.__tela_voto.pega_opcao()
            if opcao == 0:
                return False

    def seleciona_voto(self, cargo):
        while True:
            num_voto = self.__tela_voto.pega_voto(cargo.name)
            if num_voto == 99:
                self.__tela_voto.mostra_mensagem(f'Seu voto será nulo, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return num_voto
            elif num_voto == 00:
                self.__tela_voto.mostra_mensagem(f'Seu voto será branco, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return num_voto
            elif self.testa_numero_valido(num_voto, cargo) == False:
                self.__tela_voto.mostra_mensagem(f'Seu voto será nulo, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return 99
            else:
                candidato = self.testa_numero_valido(num_voto, cargo)
                self.__tela_voto.mostra_mensagem(f'Seu voto será {candidato.nome}, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return candidato.numero

    def testa_numero_valido(self, num_voto, cargo):
        for candidato in self.__controlador_urna.controlador_candidatos.candidatos:
            if (candidato.numero == num_voto and candidato.cargo.name == cargo.name):
                return candidato
        return False

    def encerra_votação(self):
        while True:
            self.__tela_voto.mostra_mensagem(f'\n1 - ENCERRAR O {self.__controlador_urna.urna.turno}º TURNO')
            self.__tela_voto.mostra_mensagem(f'\n0 - CONTINUAR A ELEIÇÃO\n')
            opcao = self.__tela_voto.pega_opcao()
            return opcao

    def testar_eleitor_votante(self, eleitor):
        turno = self.__controlador_urna.urna.turno
        if turno == 1:
            if eleitor in self.__controlador_urna.urna.votantes_1_turno:
                self.__tela_voto.mostra_mensagem(f'\nO ELEITOR SELECIONADO JÁ VOTOU NESTA ELEIÇÃO!')
                return False
            else:
                return True
        elif turno == 2:
            if eleitor in self.__controlador_urna.urna.votantes_2_turno:
                self.__tela_voto.mostra_mensagem(f'\nO ELEITOR SELECIONADO JÁ VOTOU NESTA ELEIÇÃO!')
                return False
            else:
                return True'''

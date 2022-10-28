from limite.tela_voto import TelaVoto
from entidade.voto import Voto
from entidade.eleitor import Eleitor
from entidade.cargo import Cargo


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
            num_voto = self.seleciona_voto(Cargo(1))
            print(num_voto)
        else:
            print('estou em votar nas deu errado')
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

    def seleciona_voto(self, cargo):
        while True:
            num_voto = self.__tela_voto.pega_voto(cargo.name)
            if num_voto == 99:
                self.__tela_voto.mostra_mensagem(f'Seu voto será nulo, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return num_voto
            elif num_voto == 0:
                self.__tela_voto.mostra_mensagem(f'Seu voto será branco, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return num_voto
            else:
                for candidato in self.__controlador_urna.controlador_candidatos.candidatos:
                    if (candidato.numero == num_voto and candidato.cargo.name == cargo.name):
                        self.__tela_voto.mostra_mensagem(f'Seu voto será {candidato.nome}, digite 1 para confirmar ou 0 para corrigir')
                        opcao = self.__tela_voto.pega_opcao()
                        if opcao == 1:
                            return candidato
                self.__tela_voto.mostra_mensagem(f'Seu voto será nulo, digite 1 para confirmar ou 0 para corrigir')
                opcao = self.__tela_voto.pega_opcao()
                if opcao == 1:
                    return 99

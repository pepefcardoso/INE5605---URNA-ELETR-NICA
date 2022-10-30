from limite.tela_registros import TelaRegistros
from entidade.eleitor import Eleitor
from entidade.candidato import Candidato
from entidade.voto import Voto
from entidade.cargo import Cargo
from entidade.categoria import Categoria


class ControladorRegistro:
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_registros = TelaRegistros()

    def mostra_tela_inicial(self):
        opcoes = {1: self.abre_registros_1_turno,
                  2: self.abre_registros_2_turno}
        while True:
            self.__tela_registros.abre_tela_inicial()
            opcao = self.__tela_registros.pega_opcao()
            if opcao == 0:
                break
            opcoes[opcao]()

    def abre_registros_1_turno(self):
        while True:
            self.__tela_registros.abre_tela_registros(1)
            opcao = self.__tela_registros.pega_opcao_registro()
            if opcao == 0:
                break
            self.mostra_resultados_gerais(1)

    def abre_registros_2_turno(self):
        while True:
            self.__tela_registros.abre_tela_registros(2)
            opcao = self.__tela_registros.pega_opcao_registro()
            if opcao == 0:
                break
            self.mostra_resultados_gerais(2)

    def mostra_resultados_gerais(self, turno):
        dados_reitor = self.calcula_resultados(turno, Cargo(1))
        dados_grad = self.calcula_resultados(turno, Cargo(2))
        dados_pesq = self.calcula_resultados(turno, Cargo(3))
        dados_ext = self.calcula_resultados(turno, Cargo(4))
        self.__tela_registros.abre_tela_resultados_gerais(turno, dados_reitor, dados_grad, dados_pesq, dados_ext)

    def calcula_resultados(self, turno, cargo):
        dados_eleicao = {}
        i = 1
        for candidato in self.__controlador_urna.controlador_candidatos.candidatos:
            if candidato.cargo == cargo:
                dados_eleicao[i] = []
                dados_eleicao[i].insert(0, candidato.numero)
                dados_eleicao[i].insert(1, candidato.nome)
                n_votos = self.conta_votos(candidato.numero, turno, cargo)
                dados_eleicao[i].insert(2, n_votos)
                i += 1
        n_votos_brancos = self.conta_votos(00, turno, cargo)
        dados_eleicao[i] = [00, 'BRANCOS', n_votos_brancos]
        i += 1
        n_votos_nulos = self.conta_votos(99, turno, cargo)
        dados_eleicao[i] = [99, 'NULOS', n_votos_nulos]
        return dados_eleicao

    def conta_votos(self, n_candidato, turno, cargo):
        n_votos = 0
        if cargo == Cargo(1):
            for voto in self.__controlador_urna.urna.lista_votos:
                if (voto.voto_reitor == n_candidato) and (voto.turno == turno):
                    n_votos += 1
            return n_votos
        elif cargo == Cargo(2):
            for voto in self.__controlador_urna.urna.lista_votos:
                if (voto.voto_grad == n_candidato) and (voto.turno == turno):
                    n_votos += 1
            return n_votos
        elif cargo == Cargo(3):
            for voto in self.__controlador_urna.urna.lista_votos:
                if (voto.voto_pesq == n_candidato) and (voto.turno == turno):
                    n_votos += 1
            return n_votos
        elif cargo == Cargo(4):
            for voto in self.__controlador_urna.urna.lista_votos:
                if (voto.voto_ext == n_candidato) and (voto.turno == turno):
                    n_votos += 1
            return n_votos
        else:
            return False
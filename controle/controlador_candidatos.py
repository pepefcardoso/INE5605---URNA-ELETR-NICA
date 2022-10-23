from limite.tela_candidatos import TelaCandidatos
from entidade.candidato import Candidato

class ControladorCandidatos:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_candidatos = TelaCandidatos()
        self.__candidatos = []
        self.__max_candidatos = 0

    def mostra_tela_opcoes(self):
        opcoes = {1: self.lista_candidatos, 2: self.adiciona_candidato,
                  3:self.remove_candidato, 4: self.maximo_candidatos}
        while True:
            opcao = self.__tela_candidatos.mostra_tela()
            if opcao == 0:
                break
            opcoes[opcao]()

    def lista_candidatos(self):
        for candidato in self.__candidatos:
            dados_candidato = {'nome': candidato.nome,
                               'cpf': candidato.cpf,
                               'categoria': candidato.categoria,
                               'numero': candidato.numero,
                               'chapa': candidato.chapa,
                               'cargo': candidato.cargo}
            self.__tela_candidatos.mostra_candidato(dados_candidato)

    def adiciona_candidato(self):
        dados = self.__tela_candidatos.pega_dado()
        cargo = self.__controlador_principal.controlador_cargo.selecionar_cargo()
        categoria = self.__controlador_principal.controlador_categoria.selecionar_categoria()
        candidato = Candidato(nome=dados['nome'],
                              cpf=dados['cpf'],
                              categoria=categoria,
                              numero=dados['numero'],
                              chapa=dados['chapa'],
                              cargo=cargo)
        self.__candidatos.append(candidato)

    def remove_candidato(self):
        pass

    def maximo_candidatos(self):
        numero = self.__tela_candidatos.numero_candidato()
        self.__max_candidatos = numero

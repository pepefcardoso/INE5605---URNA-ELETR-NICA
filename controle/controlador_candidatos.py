from limite.tela_candidatos import TelaCandidatos
from entidade.candidato import Candidato

class ControladorCandidatos:

    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_candidatos = TelaCandidatos()
        self.__candidatos = []

    @property
    def candidatos(self):
        return self.__candidatos

    def mostra_tela_inicial(self):
        opcoes = {1: self.lista_candidatos, 2: self.adiciona_candidato,
                  3:self.remove_candidato, 4: self.maximo_candidatos}
        while True:
            opcao = self.__tela_candidatos.abre_tela_inicial()
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
        cont = 0
        bool = True
        while bool:
            dados = self.__tela_candidatos.pega_dado()
            for candidato in self.__candidatos:
                if dados['cpf'] == candidato.cpf:
                    self.__tela_candidatos.mostra_mensagem(f'CPF: {dados["cpf"]} já está cadastrado!!!')
                    cont += 1
                elif dados['numero'] == candidato.numero:
                    self.__tela_candidatos.mostra_mensagem(f'Número {dados["numero"]} já cadastado! Por favor, escolher outro número!')
                    cont += 1
            if cont == 0:
                bool = False
            cont = 0
        cargo = self.__controlador_urna.controlador_cargo.selecionar_cargo()
        categoria = self.__controlador_urna.controlador_categoria.selecionar_categoria()
        candidato = Candidato(nome=dados['nome'],
                              cpf=dados['cpf'],
                              categoria=categoria,
                              numero=dados['numero'],
                              chapa=dados['chapa'],
                              cargo=cargo)
        self.__candidatos.append(candidato)

    def remove_candidato(self):
        bool = True
        while bool:
            cpf = self.__tela_candidatos.pega_dado_cpf()
            cont = 0
            for candidato in self.__candidatos:
                if cpf == candidato.cpf:
                    self.__candidatos.remove(candidato)
                    self.__tela_candidatos.mostra_mensagem('-' * 20)
                    self.__tela_candidatos.mostra_mensagem(f'Candidato {candidato.nome} excluído!')
                    self.__tela_candidatos.mostra_mensagem('-' * 20)
                    cont += 1
            if cont == 0:
                self.__tela_candidatos.mostra_mensagem(f'CPF não presente na lista.')
                self.__tela_candidatos.mostra_mensagem('-' * 20)
                self.__tela_candidatos.mostra_mensagem('Caso queira sair voltar ao menu inicial, insira o valor de 0.')
                self.__tela_candidatos.mostra_mensagem('-' * 20)
            if cont > 0 or cpf == 0:
                bool = False

    def maximo_candidatos(self):
        numero = self.__tela_candidatos.numero_candidato()
        self.__max_candidatos = numero

    def candidatos_reitor(self):
        lista_numero = []
        self.__tela_candidatos.mostra_mensagem('CANDIDATOS PARA REITOR: ')
        for candidato in self.__candidatos:
            if candidato.cargo.value == 1:
                self.__tela_candidatos.mostra_opcao(numero=candidato.numero, nome=candidato.nome)
                lista_numero.append(candidato.numero)
                self.__tela_candidatos.mostra_mensagem('-'*20)
        lista_numero.append(99)
        voto_reitor = self.__tela_candidatos.pega_opcao(mensagem='NÚMERO DO SEU CANDIDATO OU 99 PARA ANULAR: ',
                                                        opcoes_validas=lista_numero)
        self.__tela_candidatos.mostra_mensagem('-' * 20)
        return voto_reitor

    def candidatos_reitor_graduacao(self):
        lista_numero = []
        self.__tela_candidatos.mostra_mensagem('CANDIDATOS PARA REITOR DE GRADUAÇÃO: ')
        for candidato in self.__candidatos:
            if candidato.cargo.value == 2:
                self.__tela_candidatos.mostra_opcao(numero=candidato.numero, nome=candidato.nome)
                lista_numero.append(candidato.numero)
                self.__tela_candidatos.mostra_mensagem('-' * 20)
        lista_numero.append(99)
        voto_reitor_graduacao = self.__tela_candidatos.pega_opcao(mensagem='NÚMERO DO SEU CANDIDATO OU 99 PARA ANULAR: ',
                                                                  opcoes_validas=lista_numero)
        self.__tela_candidatos.mostra_mensagem('-' * 20)
        return voto_reitor_graduacao

    def candidatos_reitor_pesquisa(self):
        lista_numero = []
        self.__tela_candidatos.mostra_mensagem('CANDIDATOS PARA REITOR DE PESQUISA: ')
        for candidato in self.__candidatos:
            if candidato.cargo.value == 3:
                self.__tela_candidatos.mostra_opcao(numero=candidato.numero, nome=candidato.nome)
                lista_numero.append(candidato.numero)
                self.__tela_candidatos.mostra_mensagem('-' * 20)
        lista_numero.append(99)
        voto_reitor_pesquisa = self.__tela_candidatos.pega_opcao(mensagem='NÚMERO DO SEU CANDIDATO OU 99 PARA ANULAR: ',
                                                                  opcoes_validas=lista_numero)
        self.__tela_candidatos.mostra_mensagem('-' * 20)
        return voto_reitor_pesquisa

    def candidatos_reitor_extensao(self):
        lista_numero = []
        self.__tela_candidatos.mostra_mensagem('CANDIDATOS PARA REITOR DE EXTENSÃO: ')
        for candidato in self.__candidatos:
            if candidato.cargo.value == 4:
                self.__tela_candidatos.mostra_opcao(numero=candidato.numero, nome=candidato.nome)
                lista_numero.append(candidato.numero)
                self.__tela_candidatos.mostra_mensagem('-' * 20)
        lista_numero.append(99)
        voto_reitor_extensao = self.__tela_candidatos.pega_opcao(mensagem='NÚMERO DO SEU CANDIDATO OU 99 PARA ANULAR: ',
                                                                 opcoes_validas=lista_numero)
        self.__tela_candidatos.mostra_mensagem('-' * 20)
        return voto_reitor_extensao


if __name__ == '__main__':
    catcandidato = ControladorCandidatos(123)
    #print(catcandidato.verdadeiro_falso(123, 'cpf'))

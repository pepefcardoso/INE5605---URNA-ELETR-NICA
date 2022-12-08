from entidade.urna import Urna
from entidade.candidato import Candidato
from entidade.eleitor import Eleitor
from entidade.chapa import Chapa
from entidade.cargo import Cargo
from entidade.voto import Voto
from limite.tela_urna import TelaUrna
from controle.excecoes import *
import PySimpleGUI as psg

class ControladorUrna():
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema= ctrl_sistema
        self.__urna = None
        self.__tela_urna = TelaUrna()

    @property
    def urna(self):
        return self.__urna

    @urna.setter
    def urna(self, urna):
        if isinstance(urna, Urna):
            self.__urna = urna

    def configura_urna(self):
        self.__tela_urna.init_config()
        while True:
            button, values = self.__tela_urna.abre()
            if button in (psg.WIN_CLOSED, 'CANCELAR'):
                break
            if button == 'SALVAR':
                try:
                    codigo = values['codigo']
                    max_eleitores = values['max_eleitores']
                    max_candidatos = values['max_candidatos']
                    if len(codigo) < 1 or not codigo.isnumeric():
                        raise CodigoIncorretoException
                    if int(codigo) not in range(1,99):
                        raise CodigoIncorretoException
                    if len(max_eleitores) < 1 or not max_eleitores.isnumeric():
                        raise MaxEleitoresIncorretoException
                    if int(max_eleitores) not in range(1,100001):
                        raise MaxEleitoresIncorretoException
                    if len(max_candidatos) < 1 or not max_candidatos.isnumeric():
                        raise MaxCandidatosIncorretoException
                    if int(max_candidatos) not in range(1,100001):
                        raise MaxCandidatosIncorretoException
                    self.__tela_urna.mostra_mensagem('SUCESSO', 'URNA CONFIGURADA!')
                    self.__urna = Urna(codigo, int(max_eleitores), int(max_candidatos))
                    self.__tela_urna.fecha()
                    return True
                except Exception as e:
                    self.__tela_urna.mostra_mensagem('ERRO', e)
        return False

    def altera_configuracoes(self, max_eleitores: str, max_candidatos: str):
        if len(max_eleitores) < 1 or not max_eleitores.isnumeric():
            raise MaxEleitoresIncorretoException
        if int(max_eleitores) not in range(1,100001):
            raise MaxEleitoresIncorretoException
        if len(max_candidatos) < 1 or not max_candidatos.isnumeric():
            raise MaxCandidatosIncorretoException
        if int(max_candidatos) not in range(1,100001):
            raise MaxCandidatosIncorretoException
        self.__urna.max_eleitores = int(max_eleitores)
        self.__urna.max_candidatos = int(max_candidatos)
        return True

    def lista_eleitores(self):
        lista = []
        for eleitor in self.__urna.eleitores:
            lista.append([eleitor.nome, 
                          eleitor.cpf, 
                          eleitor.categoria.name])
        return lista

    def adiciona_eleitor(self, nome: str, cpf: str, categoria: str):
        if len(self.__urna.eleitores) == self.__urna.max_eleitores:
            raise ListaEleitoresCheiaException
        self.checa_nome(nome)
        self.checa_cpf(cpf)
        categoria = self.busca_categoria_nome(categoria)
        for eleitor in self.__urna.eleitores:
            if eleitor.cpf == cpf:
                raise EleitorDuplicadoException
        self.__urna.eleitores.append(Eleitor(nome, cpf, categoria))
        return True

    def busca_categoria_nome(self, nome:str):
        if nome is not None and isinstance(nome, str):
            for c in self.__urna.categorias:
                if c.name == nome:
                    return c
            raise CategoriaInvalidaException
        raise CategoriaInvalidaException

    def remove_eleitor(self, cpf: str):
        if cpf is not None and isinstance(cpf, str):
            for eleitor in self.__urna.eleitores:
                if eleitor.cpf == cpf:
                    self.__urna.eleitores.remove(eleitor)
                    return True
            raise CpfInvalidoException
        raise CpfInvalidoException

    def altera_eleitor(self, nome: str, cpf: str, categoria: str):
        if cpf is not None and isinstance(cpf, str):
            for eleitor in self.__urna.eleitores:
                if eleitor.cpf == cpf:
                    self.checa_nome(nome)
                    categoria = self.busca_categoria_nome(categoria)
                    eleitor.nome = nome
                    eleitor.categoria = categoria
                    return True
            raise EleitorNaoEncontradoException
        raise CpfInvalidoException

    def checa_nome(self, nome:str):
        if nome is not None:
            if (len(nome)<1 or 
                not isinstance(nome, str)or 
                not all(x.isalpha() or x.isspace() for x in nome)):
                raise NomeInvalidoException
            return True
        raise NomeInvalidoException

    def checa_cpf(self, cpf: str):
        if cpf is not None:
            if (len(cpf)!=11 or 
                not isinstance(cpf, str) or 
                not cpf.isnumeric()):
                raise CpfInvalidoException
            return True
        raise CpfInvalidoException

    def checa_codigo(self, codigo: str):
        if codigo is not None:
            if(len(codigo) not in range(1,3) or
               not isinstance(codigo, str) or
               not codigo.isnumeric()):
                raise CodigoIncorretoException
            return True
        raise CodigoIncorretoException

    def lista_chapas(self):
        lista = []
        for chapa in self.__urna.chapas:
            lista.append([chapa.codigo,
                          chapa.nome])
        return lista

    def adiciona_chapa(self, codigo: str, nome: str):
        if len(self.__urna.chapas) == 99:
            raise ListaChapasCheiaException
        self.checa_codigo(codigo)
        if int(codigo) not in range(1,99):
            raise CodigoIncorretoException
        self.checa_nome(nome)
        for chapa in self.__urna.chapas:
            if chapa.codigo == codigo:
                raise CodigoDuplicadoException
            if chapa.nome == nome:
                raise NomeDuplicadoException
        self.__urna.chapas.append(Chapa(codigo, nome))
        return True

    def remove_chapa(self, codigo: str):
        if codigo is not None and isinstance(codigo, str):
            for chapa in self.__urna.chapas:
                if chapa.codigo == codigo:
                    self.__urna.chapas.remove(chapa)
                    return True
            raise CodigoIncorretoException
        raise CodigoIncorretoException

    def altera_chapa(self, codigo: str, nome: str):
        if codigo is not None and isinstance(codigo, str):
            for chapa in self.__urna.chapas:
                if chapa.codigo == codigo:
                    if self.checa_nome(nome):
                        chapa.nome = nome
                        return True
            raise ChapaNaoEncontradaException
        raise CodigoIncorretoException

    def lista_candidatos(self):
        lista = []
        for candidato in self.__urna.candidatos:
            lista.append([candidato.nome,
                         candidato.cpf,
                         candidato.categoria.name,
                         candidato.numero,
                         candidato.chapa.nome,
                         candidato.cargo.name])
        return lista

    def adiciona_candidato(self, cpf: str, numero: str, chapa: str, cargo: str):
        eleitor = self.retorna_dados_eleitor(cpf)
        if len(self.__urna.candidatos) == self.__urna.max_candidatos:
            raise ListaCandidatosCheiaException
        self.checa_numero(numero)
        chapa = self.busca_chapa_nome(chapa)
        cargo = self.busca_cargo_nome(cargo)
        for candidato in self.__urna.candidatos:
            if candidato.cpf == cpf:
                raise CandidatoDuplicadoException
        self.__urna.candidatos.append(Candidato(eleitor[0],eleitor[1],eleitor[2],numero,chapa,cargo))
        return True

    def remove_candidato(self, cpf: str):
        if cpf is not None and isinstance(cpf, str):
            for candidato in self.__urna.candidatos:
                if candidato.cpf == cpf:
                    self.__urna.candidatos.remove(candidato)
                    return True
            raise CandidatoNaoEncontradoException
        raise CpfInvalidoException

    def altera_candidato(self, cpf: str, numero: str, chapa: str, cargo:str):
        if cpf is not None and isinstance(cpf, str):
            for candidato in self.__urna.candidatos:
                if candidato.numero == numero and candidato.cpf != cpf:
                    raise NumeroDuplicadoException
                if candidato.cpf == cpf:
                    self.checa_numero(numero)
                    chapa = self.busca_chapa_nome(chapa)
                    cargo = self.busca_cargo_nome(cargo)
                    candidato.numero = numero
                    candidato.chapa = chapa
                    candidato.cargo = cargo
                    return True
            raise CandidatoNaoEncontradoException
        raise CpfInvalidoException

    def retorna_dados_eleitor(self, cpf: str):
        self.checa_cpf(cpf)
        for eleitor in self.__urna.eleitores:
            if eleitor.cpf == cpf:
                return [eleitor.nome, eleitor.cpf, eleitor.categoria]
        raise EleitorNaoEncontradoException

    def checa_numero(self, numero: str):
        if numero is not None and isinstance(numero, str):
            if(len(numero) not in range(1,3) or
               not numero.isnumeric()):
                return False
            return True
        raise NumeroInvalidoException

    def busca_chapa_nome(self, nome: str):
        if nome is not None and isinstance(nome, str):
            for c in self.__urna.chapas:
                if c.nome == nome:
                    return c
            raise ChapaInvalidaException
        raise ChapaInvalidaException

    def busca_cargo_nome(self, nome: str):
        if nome is not None and isinstance(nome, str):
            for c in self.__urna.cargos:
                if c.name == nome:
                    return c
            raise CargoInvalidoException
        raise CargoInvalidoException

    def lista_cpf_eleitores(self):
        lista = []
        for eleitor in self.__urna.eleitores:
            lista.append(eleitor.cpf)
        return lista

    def busca_candidato_numero_cargo(self, numero: str, cargo: Cargo):
        if (numero is not None and
            isinstance(numero, str) and
            cargo is not None and
            isinstance(cargo, Cargo)):
            for candidato in self.__urna.candidatos:
                if (candidato.numero == numero and 
                    candidato.cargo == cargo):
                    return [candidato.chapa.nome, candidato.nome]
            if numero == '00':
                return ['BRANCO', 'BRANCO']
            return ['NULO', 'NULO']
        return False

    def checa_eleitor_votacao(self, cpf: str):
        self.checa_cpf(cpf)
        turno = self.__urna.turno
        for eleitor in self.__urna.eleitores:
            if eleitor.cpf == cpf:
                if turno == 1:
                    if eleitor.votou_1t == False:
                        return True
                    else:
                        return False
                if turno == 2:
                    if eleitor.votou_2t == False:
                        return True
                    else:
                        return False
            raise EleitorNaoEncontradoException

    def computa_voto(self, cpf: str, lista_votos: list):
        turno = self.__urna.turno
        self.checa_cpf(cpf)
        self.checa_lista_votos(lista_votos)
        for eleitor in self.__urna.eleitores:
            if eleitor.cpf == cpf:
                if turno == 1:
                    eleitor.votou_1t = True

                    self.__urna.votos.append(Voto(lista_votos[0],
                                             lista_votos[1],
                                             lista_votos[2],
                                             lista_votos[3],
                                             eleitor.categoria,
                                             turno))
                    return True
                else:
                    eleitor.votou_2t = True
                    self.__urna.votos.append(lista_votos[0],
                                             lista_votos[1],
                                             lista_votos[2],
                                             lista_votos[3],
                                             eleitor.categoria,
                                             turno)
                    return True

    def checa_lista_votos(self, lista_votos: list):
        if (lista_votos is not None and
            len(lista_votos) != 4):
            raise VotosInvalidosException
        for i in lista_votos:
            self.checa_numero(i)
        return True

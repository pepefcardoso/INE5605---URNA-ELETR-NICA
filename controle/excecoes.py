class CodigoIncorretoException(Exception):
    def __init__(self):
        super().__init__("CÓDIGO INCORRETO!")

class MaxEleitoresIncorretoException(Exception):
    def __init__(self):
        super().__init__("MÁXIMO DE ELEITORES INCORRETO!")

class MaxCandidatosIncorretoException(Exception):
    def __init__(self):
        super().__init__("MÁXIMO DE CANDIDATOS INCORRETO!")

class DadosInvalidosException(Exception):
    def __init__(self):
        super().__init__("DADOS INVÁLIDOS!")

class NomeInvalidoException(Exception):
    def __init__(self):
        super().__init__("NOME INVÁLIDO!")

class CpfInvalidoException(Exception):
    def __init__(self):
        super().__init__("CPF INVÁLIDO!")

class CategoriaInvalidaException(Exception):
    def __init__(self):
        super().__init__("CATEGORIA INVÁLIDA!")

class EleitorDuplicadoException(Exception):
    def __init__(self):
        super().__init__("ELEITOR DUPLICADO!")

class ListaEleitoresCheiaException(Exception):
    def __init__(self):
        super().__init__("LISTA DE ELEITORES CHEIA!")

class EleitorNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("ELEITOR NÃO ENCONTRADO!")

class ListaChapasCheiaException(Exception):
    def __init__(self):
        super().__init__("LISTA DE CHAPAS CHEIA!")

class CodigoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("CÓDIGO DUPLICADO!")

class NomeDuplicadoException(Exception):
    def __init__(self):
        super().__init__("NOME DUPLICADO!")

class ChapaNaoEncontradaException(Exception):
    def __init__(self):
        super().__init__("CHAPA NÃO ENCONTRADA!")

class ListaCandidatosCheiaException(Exception):
    def __init__(self):
        super().__init__("LISTA DE CANDIDATOS CHEIA!")

class NumeroInvalidoException(Exception):
    def __init__(self):
        super().__init__("NÚMERO INVÁLIDO!")

class NumeroDuplicadoException(Exception):
    def __init__(self):
        super().__init__("NÚMERO DUPLICADO!")

class ChapaInvalidaException(Exception):
    def __init__(self):
        super().__init__("CHAPA INVÁLIDA!")

class CargoInvalidoException(Exception):
    def __init__(self):
        super().__init__("CARGO INVÁLIDO!")

class CandidatoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("CANDIDATO DUPLICADO!")

class CandidatoNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("CANDIDATO NÃO ENCONTRADO!")

class TurnoInvalidoException(Exception):
    def __init__(self):
        super().__init__("TURNO INVÁLIDO!")

class VotosInvalidosException(Exception):
    def __init__(self):
        super().__init__("VOTOS INVÁLIDOS!")

class SemVotosComputadosException(Exception):
    def __init__(self):
        super().__init__("SEM VOTOS COMPUTADOS!")

class ListaInvalidaException(Exception):
    def __init__(self):
        super().__init__("LISTA INVÁLIDA COMPUTADOS!")

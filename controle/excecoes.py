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

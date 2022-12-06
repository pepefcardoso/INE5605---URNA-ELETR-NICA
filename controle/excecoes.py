class CodigoIncorretoException(Exception):
    def __init__(self):
        super().__init__("CÓDIGO INCORRETO!")

class MaxEleitoresIncorretoException(Exception):
    def __init__(self):
        super().__init__("MÁXIMO DE ELEITORES INCORRETO!")

class MaxCandidatosIncorretoException(Exception):
    def __init__(self):
        super().__init__("MÁXIMO DE CANDIDATOS INCORRETO!")

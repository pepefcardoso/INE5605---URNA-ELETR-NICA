from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria

class ControladorCategoria():
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__lista_categoria = Categoria
        self.__tela_categoria = TelaCategoria()

    def lista_categoria(self):
        for categoria in self.__lista_categoria:
            self.__tela_categoria.mostra_categoria(dados_categoria=categoria)

    def retorna_controlador_principal(self):
        self.__controlador_urna.inicia_sistema()

    def selecionar_categoria(self):
        self.lista_categoria()
        dado = self.__tela_categoria.pega_dado()
        for x in self.__lista_categoria:
            if dado['categoria'] == x.value:
                self.__tela_categoria.mostra_mensagem(msg=f'Categoria {x.name} selecionado.')
                return x

    def mostra_tela_inicial(self):
        lista_opcao = {1: self.lista_categoria,
                       0: self.retorna_controlador_principal}
        bool = True
        while bool:
            opcao = self.__tela_categoria.abre_tela_inicial()
            lista_opcao[opcao]()


if __name__ == '__main__':
    #ControladorCategoria(123).lista_categoria()
    from controle.controlador_urna import ControladorPrincipal
    centralizador = ControladorPrincipal().inicia()
    #controlador = ControladorCategoria(123)
    #controlador.abre_tela()
    #controlador.selecionar_categoria()
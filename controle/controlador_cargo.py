from limite.tela_cargos import TelaCargos
from entidade.cargo import Cargo

class ControladorCargo():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_cargo = Cargo
        self.__tela_cargo = TelaCargos()

    def lista_cargo(self):
        for cargo in self.__lista_cargo:
            self.__tela_cargo.mostra_cargo(dados_cargo=cargo)

    def retorna_controlador_principal(self):
        self.__controlador_sistema.inicia()

    def selecionar_cargo(self):
        self.lista_cargo()
        dado = self.__tela_cargo.pega_dado()
        for x in self.__lista_cargo:
            if dado['cargo'] == x.value:
                self.__tela_cargo.mostra_mensagem(msg=f'Cargo {x.name} selecionado.')
                return x



    def abre_tela(self):
        lista_opcao = {1: self.lista_cargo,
                       0: self.retorna_controlador_principal}

        bool = True
        while bool:
            opcao = self.__tela_cargo.mostra_tela()
            lista_opcao[opcao]()

if __name__ == '__main__':
    #ControladorCargo(123).lista_cargo()

    controlador = ControladorCargo(123)
    #controlador.abre_tela()
    controlador.selecionar_cargo()

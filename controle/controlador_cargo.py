from limite.tela_cargos import TelaCargos
from entidade.cargo import Cargo

class ControladorCargo():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_cargo = []
        self.__tela_cargo = TelaCargos()

    def add_cargo(self):
        dado_chapa = self.__tela_cargo.pega_dado()
        bool = False
        for x in self.__lista_cargo:
            if x.cargo.lower() == dado_chapa["cargo"].lower():
                bool = True
        if bool:
            self.__tela_cargo.mostra_mensagem("CARGO JÁ CADASTRADO!")
        else:
            self.__lista_cargo.append(Cargo(cargo=dado_chapa['cargo']))

    def remove_cargo(self):
        dado_chapa = self.__tela_cargo.pega_dado()
        bool = False
        for x in self.__lista_cargo:
            if x.cargo.lower() == dado_chapa["cargo"].lower():
                self.__lista_cargo.remove(x)
                self.__tela_cargo.mostra_mensagem(f'CARGO {x.cargo} EXCLUÍDO!')
                bool = True
        if not bool:
            self.__tela_cargo.mostra_mensagem(f'NÃO HÁ CARGO {dado_chapa["cargo"]} NA LISTA')

    def lista_cargo(self):
        for x in self.__lista_cargo:
            self.__tela_cargo.mostra_cargo(dados_cargo = x)

    def retorna_controlador_principal(self):
        pass

    def abre_tela(self):
        lista_opcao = {1: self.lista_cargo,
                       2: self.add_cargo,
                       3: self.remove_cargo,
                       0: self.retorna_controlador_principal}

        bool = True
        while bool:
            opcao = self.__tela_cargo.mostra_tela()
            lista_opcao[opcao]()
            if opcao == 0:
                break

if __name__ == '__main__':
    teste = ControladorCargo(123)
    teste.abre_tela()
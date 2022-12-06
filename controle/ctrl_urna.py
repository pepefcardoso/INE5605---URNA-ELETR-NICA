from entidade.urna import Urna
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
            button, values = self.__tela_urna.abre_tela()
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
                    self.__urna = Urna(codigo, max_eleitores, max_candidatos)
                    self.__tela_urna.fecha_tela()
                    return True
                except Exception as e:
                    self.__tela_urna.mostra_mensagem('ERRO', e)
        return False

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
                    if len(codigo) < 1 or not codigo.isnumeric or int(codigo) not in range(1,99):
                        raise CodigoIncorretoException
                    if len(max_eleitores) < 1 or not max_eleitores.isnumeric or int(codigo) not in range(1,99):
                        raise MaxEleitoresIncorretoException
                    if len(max_candidatos) < 1 or not max_candidatos.isnumeric or int(codigo) not in range(1,99):
                        raise MaxCandidatosIncorretoException
                    self.__tela_urna.mostra_mensagem('SUCESSO', 'URNA CONFIGURADA!')
                except Exception as e:
                    self.__tela_urna.mostra_mensagem('ERRO', e)


'''
    def pega_config(self):
        while True:
            codigo_lido = input('Insira o código da urna: ')
            max_eleitores_lido = input('Insira o Nº máximo de eleitores permitido: ')
            max_candidatos_lido = input('Insira o Nº máximo de candidato permitido: ')
            try:
                codigo = int(codigo_lido)
                max_eleitores = int(max_eleitores_lido)
                max_candidatos = int(max_candidatos_lido)
                if (not isinstance(codigo, int) or
                    not isinstance(max_eleitores, int) or
                    not isinstance(max_candidatos, int) or
                    (codigo not in range(1, 100)) or
                    (max_eleitores not in range(1, 100001)) or
                    (max_candidatos not in range(1, 100001))):
                    raise ValueError
                else:
                    print('\nURNA CONFIGURADA COM SUCESSO!\n')
                    return {'codigo': codigo, 'turno': 1, 'max_eleitores': max_eleitores, 'max_candidatos': max_candidatos}
            except ValueError:
                print('\nA CONFIGURAÇÃO FOI FEITA INCORRETAMENTE, TENTE NOVAMENTE\n')
'''
from entidade.voto import Voto
from limite.tela_urna import TelaUrna

class ControladorVoto():
    def __init__(self, controlador_urna):
        self.__controlador_urna = controlador_urna
        self.__tela_urna = TelaUrna()
        self.__lista_voto = []

    def mostra_tela_inicial(self):
        self.votacao()
        opcoes = {1: self.cpf_para_votar, 
                  2: self.encerra_votacao}
        while True:
            opcao = self.__tela_urna.mostra_eleicao()
            if opcao == 2:
                break
            opcoes[opcao]()

    def votacao(self):
        candidatos = self.__controlador_urna.controlador_candidatos.candidatos
        eleitores = self.__controlador_urna.controlador_eleitores.eleitores
        self.__controlador_urna.urna.lista_eleitor = eleitores
        self.__controlador_urna.urna.lista_candidatos = candidatos

    def cpf_para_votar(self):
        while True:
            cpf = self.__tela_urna.pegar_cpf()
            if cpf == 0:
                break
            lista_eleitores = self.__controlador_urna.urna.lista_eleitor
            lista_candidatos = self.__controlador_urna.urna.lista_candidatos
            bool = False
            dono_eleitor = None
            for eleitor in lista_eleitores:
                if eleitor.cpf == cpf:
                    bool = True
                    dono_eleitor = eleitor
            cand_voto = False
            dono_cand = None
            for candidato in lista_candidatos:
                if candidato.cpf == cpf:
                    cand_voto = True
                    dono_cand = candidato
            lista_quem_ja_votou = self.__controlador_urna.urna.lista_quem_ja_votou
            ja_votou = False
            for pessoa in lista_quem_ja_votou:
                if pessoa.cpf == cpf:
                    ja_votou = True
            if (bool or cand_voto) and not ja_votou:
                voto_reitor = self.__controlador_urna.controlador_candidatos.candidatos_reitor()
                voto_reitor_graduacao = self.__controlador_urna.controlador_candidatos.candidatos_reitor_graduacao()
                voto_reitor_pesquisa = self.__controlador_urna.controlador_candidatos.candidatos_reitor_pesquisa()
                voto_reitor_extensao = self.__controlador_urna.controlador_candidatos.candidatos_reitor_extensao()
                voto = Voto(voto_reitor= voto_reitor,
                            voto_grad=voto_reitor_graduacao,
                            voto_pesquisa=voto_reitor_pesquisa,
                            voto_extensa=voto_reitor_extensao)
                self.__lista_voto.append(voto)
                self.__controlador_urna.urna.add_voto(voto)
                if bool:
                    self.__controlador_urna.urna.add_dono_do_voto(dono_do_voto=dono_eleitor)
                else:
                    self.__controlador_urna.urna.add_dono_do_voto(dono_do_voto=dono_cand)
            elif (bool or cand_voto) and ja_votou:
                self.__tela_urna.mostra_mensagem(f'{cpf} JÁ VOTOU! INSIRA OUTRO CPF!')
            elif not bool and not cand_voto:
                self.__tela_urna.mostra_mensagem(f'{cpf} NÃO CADASTRADO NA URNA!')


    def encerra_votacao(self):
        pass


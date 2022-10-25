class TelaCandidatos():

    def mostra_tela(self):
        print('-' * 20)
        print('Candidatos')
        print('-' * 20)
        print('1 - Ver Lista de Candidatos')
        print('2 - Adicionar Candidatos')
        print('3 - Remover Candidatos')
        print('4 - Definir Máximo de Candidatos')
        print('0 - Voltar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def mostra_candidato(self, dados_candidato):
        print(f"Nome: {dados_candidato['nome']}")
        print(f"Cpf: {dados_candidato['cpf']}")
        print(f"Categoria: {dados_candidato['categoria'].name}")
        print(f"Número: {dados_candidato['numero']}")
        print(f"Chapa: {dados_candidato['chapa']}")
        print(f"Cargo: {dados_candidato['cargo'].name}")

    def mostra_mensagem(self, msg):
        print(msg)

    def pega_dado(self):
        nome = str(input('Nome do Candidato: '))
        cpf = int(input('CPF do Candidato: '))
        while True:
            numero = int(input('Número do Candidato: '))
            if numero <= 98 and numero >= 1:
                break
        chapa = str(input('Chapa do Candidato: '))
        return {'nome': nome, 'cpf': cpf, 'numero': numero, 'chapa': chapa}

    def pega_dado_cpf(self):
        cpf = int(input('CPF do Candidato para excluir: '))
        return cpf

    def numero_candidato(self):
        while True:
            numero = input("Números de Candidatos a cadastrar: ")
            try:
                dado = int(numero)
                if not dado >= 1:
                    raise Exception
                return dado
            except Exception:
                print('Valor Inválido, informe um número maior que 1.')


    def pega_opcao(self, mensagem: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")
                if opcoes_validas:
                    print('Opções válidas: ', opcoes_validas)

from limites.tela_abstrata import TelaAbstrata

class TelaDisciplina(TelaAbstrata):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("PROFESSORES")
        print("Escolha a opcao")
        print("1 - Incluir disciplina")
        print("2 - Alterar disciplina")
        print("3 - Listar disciplinas")
        print("4 - Excluir disciplina")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha alguma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def le_num_inteiro(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('ERRO! Digite um valor correto.')
                if inteiros_validos:
                    print('Valores validos:', inteiros_validos)

    def pega_dados_disciplina(self):
        print("-------- DADOS DISCIPLINA ----------")
        nome = input("Nome: ")
        codigo = input("Código: ")
        limite = input("Limite: ")
        professor = input("Professor")

        return {"nome:": nome, "codigo": codigo, "limite": limite, "professor": professor}

    def mostra_disciplina(self, dados_disciplina):
        print("NOME DA DISCIPLINA: ", dados_disciplina["nome"])
        print("CODIGO DA DISCIPLINA: ", dados_disciplina["codigo"])
        print("LIMITE DA DISCIPLINA ", dados_disciplina["limite"])
        print("PROFESSOR DA DISCIPLINA ", dados_disciplina["professor"])
        print("\n")

    def seleciona_disciplina(self):
        codigo = input("Código da disciplina: ")
        return codigo
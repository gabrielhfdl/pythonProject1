from limites.tela_abstrata import TelaAbstrata

class TelaAlunos(TelaAbstrata):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("ALUNOS")
        print("Escolha a opcao")
        print("1 - Incluir aluno")
        print("2 - Alterar aluno")
        print("3 - Listar aluno")
        print("4 - Excluir aluno")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha alguma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_aluno(self):
        print("--- DADOS DO ALUNO ---")
        nome = input('Nome: ')
        matricula = input('Matricula: ')
        idade = self.verifica_idade('Idade: ', list(range(1, 151, 1)))
        return {"nome": nome, "matricula": matricula, "idade": idade}

    def mostrar_aluno(self, dados_aluno):
        print("NOME DO ALUNO: ", dados_aluno["nome"])
        print("MATRICULA DO ALUNO: ", dados_aluno["matricula"])
        print("IDADE DO ALUNO: ", dados_aluno["idade"])
        print("---------------------")

    def selecionar_aluno(self):
        matricula = input("Entre com a matricula do aluno que deseja selecionar: ")
        return matricula

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

    def verifica_idade(self, idade: str = '', valores_validos_idades: [] = None):
        while True:
            idade_lida = input(idade)
            try:
                idade = int(idade_lida)
                if valores_validos_idades and idade not in valores_validos_idades:
                    raise ValueError
                return idade
            except ValueError:
                print('ERRO!')
                if valores_validos_idades:
                    print('Entre com um valor de idade entre: ', valores_validos_idades)

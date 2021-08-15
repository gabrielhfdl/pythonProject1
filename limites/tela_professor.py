from limites.tela_abstrata import TelaAbstrata

class TelaProfessor(TelaAbstrata):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("PROFESSORES")
        print("Escolha a opcao")
        print("1 - Incluir professor")
        print("2 - Alterar professor")
        print("3 - Listar professor")
        print("4 - Excluir professor")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha alguma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_professor(self):
        print("--- DADOS DO PROFESSOR ---")
        nome = input('Nome: ')
        codigo = input('Código: ')
        idade = int(input('Idade: '))
        return {"nome": nome, "codigo": codigo, "idade": idade}  ## fazer validade para entradas dps

    def mostrar_professor(self, dados_professor):
        print("NOME DO PROFESSOR: ", dados_professor["nome"])
        print("CODIGO DO PROFESSOR: ", dados_professor["codigo"])
        print("IDADE DO PROFESSOR: ", dados_professor["idade"])
        print("---------------------")

    def selecionar_professor(self):
        codigo = input("Entre com o código do professor que deseja selecionar: ")
        return codigo

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
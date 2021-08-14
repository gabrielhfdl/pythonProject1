class TelaProfessor:
    def tela_opcoes(self):
        print("PROFESSORES")
        print("Escolha a opcao")
        print("1 - Incluir professor")
        print("2 - Alterar professor")
        print("3 - Listar professor")
        print("4 - Excluir professor")
        print("5 - Buscar professor por código")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_professor(self):
        print("--- DADOS DO PROFESSOR ---")
        nome = input('Nome: ')
        codigo = input('Código: ')
        idade = int(input('Idade'))
        return {"nome": nome, "codigo": codigo, "idade": idade}  ## fazer validade para entradas dps

    def mostrar_professor(self, dados_professor):
        print("NOME DO PROFESSOR: ", dados_professor["nome"])
        print("CODIGO DO PROFESSOR: ", dados_professor["codigo"])
        print("IDADE DO PROFESSOR: ", dados_professor["idade"])

    def selecionar_professor(self):
        codigo = int(input("Entre com o código do professor que deseja selecionar"))
        return codigo

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

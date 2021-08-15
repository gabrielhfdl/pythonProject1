from limites.tela_abstrata import TelaAbstrata
from entidade.professor import Professor
from controle.controlador_professor import Professor

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
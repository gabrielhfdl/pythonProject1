from limites.tela_abstrata import TelaAbstrata

class TelaSistema(TelaAbstrata):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("\n---- SEJA BEM VINDO AO CURSO DE SISTEMAS ---- \n")
        print("Escolha sua opcao")
        print("1 - Entrar na tela de Professores")
        print("2 - Entrar na tela de Alunos")
        print("3 - Entrar na tela de Disciplinas")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 0])
        return opcao

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

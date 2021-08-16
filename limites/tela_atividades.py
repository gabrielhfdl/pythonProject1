from limites.tela_abstrata import TelaAbstrata

class TelaAtividades(TelaAbstrata):

    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print("ATIVIDADES")
        print("Escolha a opcao")
        print("1 - Incluir atividades")
        print("2 - Alterar atividades")
        print("3 - Listar atividades")
        print("4 - Excluir atividades")
        print("0 - Retornar")
        opcao = self.le_num_inteiro("Escolha alguma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_atividades(self):
        print("--- DADOS DA ATIVIDADE ---")
        titulo = input('Titulo: ')
        descricao = input('Descricao: ')
        prazo = input('Prazo: ')
        data_entregue = input('Data de Entrega: ')
        nota = input(': ')
        status = input(': ')
        return {{"titulo": atividade.titulo,"descricao": atividade.descricao,"prazo": atividade.prazo, "data de entrega": atividade.data_entregue, "nota": nota, "status": status}}  ## fazer validade para entradas dps

    def mostrar_atividades(self, dados_atividades):
        print("TITULO DA ATIVIDADE: ", dados_atividades["titulo"])
        print("---------------------")

    def selecionar_atividades(self):
        titulo = input("Entre com a titulo do atividades que deseja selecionar: ")
        return titulo

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
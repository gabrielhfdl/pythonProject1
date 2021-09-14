from limites.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaProfessor(TelaAbstrata):

    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_opcoes()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('--- PROFESSORES ---', font=("Arial", 25))],
            [sg.Radio('Incluir professor', "RD1", key='1')],
            [sg.Radio('Alterar professor', "RD1", key='2')],
            [sg.Radio('Listar professores', "RD1", key='3')],
            [sg.Radio('Excluir professor', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CADASTRO DE PROFESSORES').Layout(layout)

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def pega_dados_professor(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('--- DADOS DO PROFESSOR ---', font=("Arial", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('CADASTRO DE PROFESSOR').Layout(layout)

        button, values = self.open()

        nome = values['nome']
        codigo = values['telefone']
        idade = values['cpf']

        self.close()
        return {"nome": nome, "codigo": codigo, "idade": idade}


        # nome = input('Nome: ')
        # codigo = input('Código: ')
        # idade = self.verifica_idade('Idade: ', list(range(1, 151, 1)))
        # return {"nome": nome, "codigo": codigo, "idade": idade}

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
                    print('Entre com um valor de idade entre 1 e 150 ')
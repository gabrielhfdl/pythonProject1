from limites.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaAlunos(TelaAbstrata):

    def __init__(self):
        self.__window = None
        self.init_opcoes()


    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('--- ALUNOS ---', font=("Arial", 25))],
            [sg.Radio('Incluir aluno', "RD1", key='1')],
            [sg.Radio('Alterar aluno', "RD1", key='2')],
            [sg.Radio('Listar aluno', "RD1", key='3')],
            [sg.Radio('Excluir aluno', "RD1", key='4')],
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

    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('--- DADOS DO ALUNO ---', font=("Arial", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Matrícula:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('CADASTRO DE ALUNOS').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        matricula = int(values['matricula'])
        idade = int(values['idade'])
        self.close()
        return {"nome": nome, "matricula": matricula, "idade": idade}

    def selecionar_aluno(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('--- SELECIONAR ALUNO PELA MATRICULA ---', font=("Helvica", 25))],
            [sg.Text('Digite a matricula do aluno:', font=("Helvica", 15))],
            [sg.Text('MATRÍCULA:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]

        self.__window = sg.Window('Selecionar aluno').Layout(layout)
        button, values = self.open()
        matricula = int(values['matricula'])
        self.close()
        return matricula

    def mostrar_aluno(self, dados_aluno):
        string_todos_amigos = ""
        for dado in dados_aluno:
            string_todos_amigos = string_todos_amigos + "Nome: " + (dado["nome"]) + '\n'
            string_todos_amigos = string_todos_amigos + "Matricula: " + str(dado["matricula"]) + '\n'
            string_todos_amigos = string_todos_amigos + "Idade: " + str(dado["idade"]) + '\n\n'

        sg.Popup('--- LISTA DE ALUNOS ---', string_todos_amigos)

    def mostrar_mensagem(self, mensagem):
        sg.popup("", mensagem)

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

    def verifica_idade(self, idade, valores_validos_idades: [] = None):
        while True:
            idade_lida = input(idade)
            try:
                idade = int(idade_lida)
                if valores_validos_idades and idade not in valores_validos_idades:
                    raise ValueError
                return idade
            except ValueError:
                self.mostrar_mensagem('Erro! Insira um entre 1-150')
                if valores_validos_idades:
                    print('Entre com um valor de idade entre 1 e 150 ')

from limites.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaDisciplina(TelaAbstrata):

    def __init__(self):
        super().__init__()

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

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('-------- AMIGOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir disciplina', "RD1", key='1')],
            [sg.Radio('Alterar disciplina', "RD1", key='2')],
            [sg.Radio('Listar disciplinas', "RD1", key='3')],
            [sg.Radio('Excluir disciplina', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de disciplinas').Layout(layout)

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
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('-------- DADOS DISCIPLINA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Limite', size=(15, 1)), sg.InputText('', key='limite')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        codigo = int(values['codigo'])
        limite = int(values['limite'])

        self.close()
        return {"nome": nome, "codigo": codigo, "limite": limite}

    def mostra_disciplina(self, dados_disciplina):
        string_todas_disciplinas = ''
        for dados in dados_disciplina:
            string_todas_disciplinas = string_todas_disciplinas + "NOME DISCIPLINA: " + (dados["nome"]) + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "CÓDIGO DISCIPLINA: " + str(dados["codigo"]) + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "LIMITE DISCIPLINA: " + str(dados["limite"]) + '\n\n'

        sg.Popup('-------- LISTA DE DISCIPLINAS ----------', string_todas_disciplinas)

    def seleciona_disciplina(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('-------- SELECIONAR DISCIPLINA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da disciplina:', font=("Helvica", 15))],
            [sg.Text('CÓDIGO:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar disciplina').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        self.close()
        return codigo

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
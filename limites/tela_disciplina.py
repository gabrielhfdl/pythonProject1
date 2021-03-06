from limites.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
from excecoes.nao_eh_string import NaoEhString


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
            [sg.Text('-------- DISCIPLINAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir disciplina', "RD1", key='1')],
            [sg.Radio('Alterar disciplina', "RD1", key='2')],
            [sg.Radio('Listar disciplinas', "RD1", key='3')],
            [sg.Radio('Excluir disciplina', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de disciplinas').Layout(layout)

    def pega_dados_disciplina(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('-------- DADOS DISCIPLINA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Limite', size=(15, 1)), sg.InputText('', key='limite')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Disciplinas').Layout(layout)

        try:

            button, values = self.open()
            nome = values['nome']

            if len(nome) == 0 or type(nome) != str:
                raise NaoEhString

            codigo = int(values['codigo'])
            limite = int(values['limite'])

            if limite > 40 or limite < 0:
                raise ValueError

            self.close()
            return {"nome": nome, "codigo": codigo, "limite": limite}

        except ValueError:
            self.mostrar_mensagem('ERRO: Escolha um código com valor inteiro e limite MENOR do que 40')
            self.close()
            return self.pega_dados_disciplina()

        except NaoEhString:
            self.mostrar_mensagem('ERRO: Verifique o nome!')
            self.close()
            return self.pega_dados_disciplina()


    def mostra_disciplina(self, dados_disciplina):
        string_todas_disciplinas = ''
        for dados in dados_disciplina:
            string_todas_disciplinas = string_todas_disciplinas + "Nome disciplina: " + (dados["nome"]) + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "Código disciplina: " + str(dados["codigo"]) + '\n'
            string_todas_disciplinas = string_todas_disciplinas + "Limite disciplina: " + str(dados["limite"]) + '\n\n'

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

        try:
            button, values = self.open()
            codigo = int(values['codigo'])
            self.close()
            return codigo
        except ValueError:
            self.mostrar_mensagem('ERRO: Disciplina não existe!')
            self.close()
            return self.tela_opcoes()


    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values


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

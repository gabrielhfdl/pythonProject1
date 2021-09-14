from limites.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaSistema(TelaAbstrata):
    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
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

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def init_components(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout = [
            [sg.Text('--- BEM VINDO AO CURSO DE SISTEMAS DE INFORMAÇÃO ---', font=("Arial",20))],
            [sg.Text('Escolha sua opção de menu:', font=("Arial",10))],
            [sg.Radio('Menu de professores',"RD1", key='1')],
            [sg.Radio('Menu de alunos',"RD1", key='2')],
            [sg.Radio('Menu de disciplinas',"RD1", key='3')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('CADASTRO SISTEMAS DE INFORMAÇÃO - UFSC ').Layout(layout)

    def close(self):
        self.__window.Close()

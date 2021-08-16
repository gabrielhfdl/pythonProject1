from limites.tela_sistema import TelaSistema
from controle.controlador_professor import ControladorProfessor
from controle.controlador_disciplinas import ControladorDisciplinas
from controle.controlador_alunos import ControladorAlunos


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_professores = ControladorProfessor(self)
        self.__controlador_disciplinas = ControladorDisciplinas(self)
        self.__controlador_alunos = ControladorAlunos(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def cadastro_professores(self):
        self.__controlador_professores.abre_tela()

    def cadastro_alunos(self):
        self.__controlador_alunos.abre_tela()

    def cadastro_disciplinas(self):
        self.__controlador_disciplinas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastro_professores, 2: self.cadastro_alunos, 3: self.cadastro_disciplinas,
                        0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
from limites.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina

class ControladorDisciplinas:
    def __init__(self, controlador_sistema):
        self.__disciplinas = []
        self.__tela_disciplina = TelaDisciplina()
        self.__controlador_sistema = controlador_sistema

    def incluir_disciplina(self):
        pass

    def alterar_disciplina(self):
        pass

    def listar_disciplinas(self):
        pass

    def excluir_disciplina(self):
        pass


    def abre_tela(self):
        lista_opcoes = {1: self.incluir_disciplina,
                        2: self.alterar_disciplina,
                        3: self.listar_disciplinas,
                        4: self.excluir_disciplina,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_disciplina.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

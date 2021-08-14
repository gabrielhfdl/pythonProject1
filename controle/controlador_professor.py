from limites.tela_professor import TelaProfessor
from entidade.professor import Professor

class ControladorProfessor:
    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def buscar_professor_por_codigo(self, codigo: int):
        for professor in self.__professores:
            if(professor.codigo == codigo):
                return professor
            return None

    def incluir_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        professor = Professor(dados_professor["nome"], dados_professor["codigo"], dados_professor["idade"])
        self.__professores.append(professor)

    def alterar_professor(self):
        pass


    def listar_professores(self):
        for professor in self.__professores:
            self.__tela_professor.mostrar_professor({"nome": professor.nome, "codigo": professor.codigo, "idade": professor.idade})

    def excluir_professor(self):
        pass




    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor,
                        2: self.alterar_professor,
                        3: self.listar_professores,
                        4: self.excluir_professor,
                        5: self.buscar_professor_por_codigo,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
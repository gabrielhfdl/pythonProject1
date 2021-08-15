from limites.tela_professor import TelaProfessor
from entidade.professor import Professor

class ControladorProfessor:
    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def buscar_professor_por_codigo(self, codigo: int):
        for professor in self.__professores:
            if professor.codigo == codigo:
                return professor
            return None

    def incluir_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        professor = Professor(dados_professor["nome"], dados_professor["codigo"], dados_professor["idade"])
        self.__professores.append(professor)

    def excluir_professor(self):
        self.listar_professores()
        codigo_professor = self.__tela_professor.pega_dados_professor()
        professor = self.buscar_professor_por_codigo(codigo_professor)

        if(professor is not None):
            self.__professores.remove(professor)
            self.listar_professores()
        else:
            self.__tela_professor.mostrar_mensagem('ERRO: Professor não existe!')

    def alterar_professor(self):
        self.listar_professores()
        codigo_professor = self.__tela_professor.selecionar_professor()
        professor = self.buscar_professor_por_codigo(codigo_professor)
        if professor is not None:
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.codigo = novos_dados_professor["codigo"]
            professor.idade = novos_dados_professor["idade"]
            self.listar_professores()
        else:
            self.__tela_professor.mostrar_professor("ERRO: Professor não existe")

    def listar_professores(self):
        for professor in self.__professores:
            self.__tela_professor.mostrar_professor({"nome": professor.nome,
                                                     "codigo": professor.codigo,
                                                     "idade": professor.idade})

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


from limites.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina

class ControladorDisciplinas:
    def __init__(self, controlador_sistema):
        self.__disciplinas = []
        self.__tela_disciplina = TelaDisciplina()
        self.__controlador_sistema = controlador_sistema

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def incluir_disciplina(self):
        dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
        disciplina = Disciplina(dados_disciplina["nome"],
                                dados_disciplina["codigo"],
                                dados_disciplina["limite"],
                                dados_disciplina["professor"])
        self.__disciplinas.append(disciplina)

    def lista_disciplinas(self):
        for disciplina in self.__disciplinas:
            self.__tela_disciplina.mostra_disciplina({"nome": disciplina.nome,
                                                      "codigo": disciplina.codigo,
                                                      "limite": disciplina.limite,
                                                      "professor": disciplina.professor})

    def pega_disciplina_por_codigo(self, codigo: int):
        for disciplina in self.__disciplinas:
            if disciplina.codigo == codigo:
                return disciplina
            return None

    def excluir_disciplina(self):
        self.lista_disciplinas()
        codigo_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_codigo(codigo_disciplina)

        if disciplina is not None:
            self.__disciplinas.remove(disciplina)
            self.lista_disciplinas()
        else:
            self.__tela_disciplina.mostrar_mensagem("ERRO: Disciplina não existe")

    def alterar_disciplina(self):
        self.lista_disciplinas()
        codigo_disciplina = self.__tela_disciplina.seleciona_disciplina()
        disciplina = self.pega_disciplina_por_codigo(codigo_disciplina)

        if disciplina is not None:
            novos_dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
            disciplina.nome = novos_dados_disciplina["nome"]
            disciplina.codigo = novos_dados_disciplina["codigo"]
            disciplina.limite = novos_dados_disciplina["limite"]
            self.lista_disciplinas()
        else:
            self.__tela_disciplina.mostrar_mensagem("Erro: Tente novamente")



    def abre_tela(self):
        lista_opcoes = {1: self.incluir_disciplina,
                        2: self.alterar_disciplina,
                        3: self.lista_disciplinas,
                        4: self.excluir_disciplina,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_disciplina.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

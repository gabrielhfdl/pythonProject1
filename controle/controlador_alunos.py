from limites.tela_alunos import TelaAlunos
from entidade.aluno import Aluno


class ControladorAlunos:
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_alunos = TelaAlunos()
        self.__controlador_sistema = controlador_sistema

    def buscar_aluno_por_matricula(self, matricula: int):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
            return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_alunos.pega_dados_aluno()
        aluno = aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["idade"])
        self.__alunos.append(aluno)

    def excluir_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_alunos.pega_dados_aluno()
        aluno = self.buscar_aluno_por_matricula(matricula_aluno)

        if(aluno is not None):
            self.__alunos.remove(aluno)
        else:
            self.__tela_alunos.mostrar_mensagem('ERRO: aluno não existe!')

    def alterar_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_alunos.selecionar_aluno()
        aluno = self.buscar_aluno_por_matricula(matricula_aluno)
        if aluno is not None:
            novos_dados_aluno = self.__tela_alunos.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.matricula = novos_dados_aluno["matricula"]
            aluno.idade = novos_dados_aluno["idade"]
            self.listar_alunos()
        else:
            self.__tela_alunos.mostrar_aluno("ERRO: aluno não existe")

    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_alunos.mostrar_aluno({"nome": aluno.nome,
                                                     "matricula": aluno.matricula,
                                                     "idade": aluno.idade})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_aluno,
                        2: self.alterar_aluno,
                        3: self.listar_alunos,
                        4: self.excluir_aluno,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_alunos.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
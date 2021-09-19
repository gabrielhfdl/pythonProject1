from limites.tela_alunos import TelaAlunos
from entidade.aluno import Aluno
from DAOs.aluno_dao import AlunoDAO


class ControladorAlunos:
    def __init__(self, controlador_sistema):
        self.__alunos_DAO = AlunoDAO()
        self.__tela_alunos = TelaAlunos()
        self.__controlador_sistema = controlador_sistema

    def buscar_aluno_por_matricula(self, matricula: int):
        for aluno in self.__alunos_DAO.get_all():
            if aluno.matricula == matricula:
                return aluno
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_alunos.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["idade"])
        self.__alunos_DAO.add(aluno)
        self.listar_alunos()

    def excluir_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_alunos.selecionar_aluno()
        aluno = self.buscar_aluno_por_matricula(matricula_aluno)

        if(aluno is not None):
            self.__alunos_DAO.remove(aluno.matricula)
            self.__tela_alunos.mostrar_mensagem('Aluno excluído com sucesso!')
            self.listar_alunos()
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
            self.__alunos_DAO.update(aluno)
            self.listar_alunos()
        else:
            self.__tela_alunos.mostrar_aluno("ERRO: Aluno não existe")

    def listar_alunos(self):
        try:
            dados_alunos = []
            if len(self.__alunos_DAO.get_all()) == 0:
                raise Exception
            for aluno in self.__alunos_DAO.get_all():
                dados_alunos.append({"nome": aluno.nome, "matricula": aluno.matricula, "idade": aluno.idade})
            self.__tela_alunos.mostrar_aluno(dados_alunos)

        except Exception:
            self.__tela_alunos.mostrar_mensagem('A sua lista está vazia!')

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
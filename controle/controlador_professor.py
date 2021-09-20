from limites.tela_professor import TelaProfessor
from entidade.professor import Professor
from DAOs.professor_dao import ProfessorDAO
from excecoes.codigo_ja_existente import CodigoJaExistente
from excecoes.lista_vazia import ListaVazia

class ControladorProfessor:
    def __init__(self, controlador_sistema):
        self.__professor_DAO = ProfessorDAO()
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def buscar_professor_por_codigo(self, codigo: int):
        for professor in self.__professor_DAO.get_all():
            if(professor.codigo == codigo):
                return professor
        return None

    def incluir_professor(self):

        try:
            dados_professor = self.__tela_professor.pega_dados_professor()
            professor = Professor(dados_professor["nome"], dados_professor["codigo"], dados_professor["idade"])
            for i in self.__professor_DAO.get_all():
                if dados_professor['codigo'] == i.codigo:
                    raise CodigoJaExistente
            self.__professor_DAO.add(professor)

        except CodigoJaExistente:
            self.__tela_professor.mostrar_mensagem("Erro! Código já existente para esse Professor")


    def excluir_professor(self):
        self.listar_professores()
        codigo_professor = self.__tela_professor.selecionar_professor()
        professor = self.buscar_professor_por_codigo(codigo_professor)

        try:
            if(professor is not None):
                self.__professor_DAO.remove(professor.codigo)
                self.listar_professores()
            else:
                self.__tela_professor.mostrar_mensagem('ERRO: Professor não existe!')
                self.__tela_professor.close()
                return self.__tela_professor.tela_opcoes()

        except ValueError:
            self.__tela_professor.mostrar_mensagem('ERRO: Entre com um número inteiro!')
            self.__tela_professor.close()
            return self.__tela_professor.tela_opcoes()


    def alterar_professor(self):
        try:
            self.listar_professores()
            codigo_professor = self.__tela_professor.selecionar_professor()
            professor = self.buscar_professor_por_codigo(codigo_professor)

            if (professor is not None):
                novos_dados_professor = self.__tela_professor.pega_dados_professor()
                professor.nome = novos_dados_professor["nome"]
                professor.codigo = novos_dados_professor["codigo"]
                professor.idade = novos_dados_professor["idade"]
                self.__professor_DAO.update(professor)
                self.listar_professores()
            else:
                self.__tela_professor.mostrar_mensagem("ERRO: Professor não existe")

        except TypeError:
            self.__tela_professor.mostrar_mensagem("Verifique sua entrada!")
            self.__tela_professor.close()
            return self.__tela_professor.tela_opcoes()

    def listar_professores(self):
        dados_professores = []

        try:
            if len(self.__professor_DAO.get_all()) == 0:
                raise ListaVazia
            for professor in self.__professor_DAO.get_all():
                dados_professores.append({"nome": professor.nome, "codigo": professor.codigo, "idade": professor.idade})
            self.__tela_professor.mostrar_professor(dados_professores)

        except ListaVazia:
            self.__tela_professor.mostrar_mensagem('A sua lista está vazia!')


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_professor,
                        2: self.alterar_professor,
                        3: self.listar_professores,
                        4: self.excluir_professor,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_professor.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()


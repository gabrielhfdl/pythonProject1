from limites.tela_atividades import TelaAtividades
from entidade.atividade import Atividade


class ControladorAtividades:
    def __init__(self, controlador_sistema):
        self.__atividades = []
        self.__tela_atividades = TelaAtividades()
        self.__controlador_sistema = controlador_sistema

    def buscar_atividade_por_matricula(self, matricula: int):
        for atividade in self.__atividades:
            if atividade.matricula == matricula:
                return atividade
            return None

    def incluir_atividade(self):
        dados_atividade = self.__tela_atividades.pega_dados_atividade()
        atividade = atividade(dados_atividade["titulo"], dados_atividade["prazo"], dados_atividade["descricao"], dados_atividade["data_entregue"], dados_atividade["nota"], dados_atividade["status"])
        self.__atividades.append(atividade)

    def excluir_atividade(self):
        self.listar_atividades()
        matricula_atividade = self.__tela_atividades.pega_dados_atividade()
        atividade = self.buscar_atividade_por_matricula(matricula_atividade)

        if(atividade is not None):
            self.__atividades.remove(atividade)
        else:
            self.__tela_atividades.mostrar_mensagem('ERRO: atividade não existe!')

    def alterar_atividade(self):
        self.listar_atividades()
        matricula_atividade = self.__tela_atividades.selecionar_atividade()
        atividade = self.buscar_atividade_por_matricula(matricula_atividade)
        if atividade is not None:
            novos_dados_atividade = self.__tela_atividades.pega_dados_atividade()
            atividade.nome = novos_dados_atividade["nome"]
            atividade.matricula = novos_dados_atividade["matricula"]
            atividade.idade = novos_dados_atividade["idade"]
            self.listar_atividades()
        else:
            self.__tela_atividades.mostrar_atividade("ERRO: Atividade não existe")

    def listar_atividades(self):
        for atividade in self.__atividades:
            self.__tela_atividades.mostrar_atividade({"titulo": atividade.titulo,"descricao": atividade.matricula,"prazo": atividade.prazo, "data de entrega": atividade.data_entregue, "nota": nota, "status": status})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_atividade,
                        2: self.alterar_atividade,
                        3: self.listar_atividades,
                        4: self.excluir_atividade,
                        0: self.retornar}
        while True:
            opcao_escolhida = self.__tela_atividades.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
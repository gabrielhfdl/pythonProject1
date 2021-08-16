from datetime import date

class Atividades:
    def __init__(self, titulo: str, descricao: str, prazo: date, data_entregue: date, nota: int, status: str):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prazo = prazo
        self.__data_entregue = data_entregue
        self.__nota = nota
        self.__status = status
        
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def prazo(self):
        return self.__prazo

    @prazo.setter
    def prazo(self, prazo):
        self.__prazo = prazo

    @property
    def data_entregue(self):
        return self.__data_entregue

    @data_entregue.setter
    def data_entregue(self, data_entregue):
        self.__data_entregue = data_entregue

    @property
    def nota(self):
        return self.__nota

    @data_entregue.setter
    def nota(self, nota):
        self.__nota = nota

    @property
    def status(self):
        return self.__status

    @data_entregue.setter
    def status(self, status):
        self.__status = status

class Trabalho(Atividades):
    def __init__(self, titulo: str, descricao: str, prazo: date, data_entregue: date, nota: int, status: str, nome: str):
        super().__init__(titulo, descricao, prazo, data_entregue, nota, status)
        self.__nome = nome

class Prova(Atividades):
    def __init__(self, titulo: str, descricao: str, prazo: date, data_entregue: date, nota: int, status: str, nome: str):
        super().__init__(titulo, descricao, prazo, data_entregue, nota, status)
        self.__nome = nome

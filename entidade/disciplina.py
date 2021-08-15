from entidade.professor import Professor

class Disciplina:
    def __init__(self, nome: str, codigo: int, limite: int, professor: Professor):
        self.__nome = nome
        self.__codigo = codigo
        self.__limite = limite
        if (isinstance(professor, Professor)):
            self.__professor = professor

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor: Professor):
        if (isinstance(professor, Professor)):
            self.__professor = professor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


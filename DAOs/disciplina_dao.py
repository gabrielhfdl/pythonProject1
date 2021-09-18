from DAOs.dao import DAO
from entidade.disciplina import Disciplina


class DisciplinaDAO(DAO):
    def __init__(self):
        super().__init__('disciplinas.pkl')

    def add(self, disciplina: Disciplina):
        if (isinstance(disciplina.codigo, int)) and (disciplina is not None) and isinstance(disciplina, Disciplina):
            super().add(disciplina.codigo, disciplina)

    def update(self, disciplina: Disciplina):
        if((disciplina is not None) and isinstance(disciplina, Disciplina) and isinstance(disciplina.codigo, int)):
            super().update(disciplina.codigo, disciplina)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
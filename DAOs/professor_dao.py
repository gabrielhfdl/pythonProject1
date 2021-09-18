from DAOs.dao import DAO
from entidade.professor import Professor


class ProfessorDAO(DAO):
    def __init__(self):
        super().__init__('professores.pkl')

    def add(self, professor: Professor):
        if (isinstance(professor.codigo, int)) and (professor is not None) and isinstance(professor, Professor):
            super().add(professor.codigo, professor)

    def update(self, professor: Professor):
        if((professor is not None) and isinstance(professor, Professor) and isinstance(professor.codigo, int)):
            super().update(professor.codigo, professor)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)


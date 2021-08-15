from abc import ABC, abstractmethod


class TelaAbstrata(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def le_num_inteiro(self):
        pass
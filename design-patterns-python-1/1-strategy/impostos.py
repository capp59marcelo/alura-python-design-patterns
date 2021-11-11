import abc

from orcamento import Orcamento


class Imposto(abc.ABC):
    @abc.abstractmethod
    def calcula(self, orcamento: Orcamento) -> float:
        raise NotImplementedError()


class ICMS(Imposto):
    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.1


class ISS(Imposto):
    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.06

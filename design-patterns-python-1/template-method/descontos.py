import abc

from orcamento import Orcamento


class IDesconto(abc.ABC):
    @abc.abstractmethod
    def calcula(self, orcamento: Orcamento) -> float:
        raise NotImplementedError


class DescontoPorCincoItens(IDesconto):
    def __init__(self, proximo_desconto: IDesconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento: Orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class DescontoPorMaisDeQuinhentosReais(IDesconto):
    def __init__(self, proximo_desconto: IDesconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento: Orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)


class SemDesconto(IDesconto):
    def calcula(self, orcamento: Orcamento):
        return 0

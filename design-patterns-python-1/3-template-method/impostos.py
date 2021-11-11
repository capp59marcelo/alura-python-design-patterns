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


class TemplateDeImpostoCondicional(Imposto):
    def calcula(self, orcamento: Orcamento) -> float:
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abc.abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento: Orcamento) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def maxima_taxacao(self, orcamento: Orcamento) -> float:
        raise NotImplementedError()

    @abc.abstractmethod
    def minima_taxacao(self, orcamento: Orcamento) -> float:
        raise NotImplementedError()


class ICPP(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento: Orcamento):

        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento: Orcamento):
        maior_que_100 = self.__tem_item_maior_que_100_reais(orcamento)
        return orcamento.valor > 500 and maior_que_100

    def maxima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento: Orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento: Orcamento):

        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

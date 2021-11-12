from __future__ import annotations

import abc
from typing import Any

from orcamento import Orcamento


class Imposto(object):
    def __init__(self, outro_imposto: Imposto = None) -> None:
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento: Orcamento) -> float:
        # trata se o imposto tem próximo ou não
        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abc.abstractmethod
    def calcula(self, orcamento: Orcamento) -> float:
        raise NotImplementedError()


class ICMS(Imposto):
    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)


def decorator_iss(metodo_ou_funcao: Any):
    def wrapper(self: Any, orcamento: Orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0

    return wrapper


class ISS(Imposto):
    @decorator_iss
    def calcula(self, orcamento: Orcamento) -> float:
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)


class TemplateDeImpostoCondicional(Imposto):
    def calcula(self, orcamento: Orcamento) -> float:
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

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

# -*- coding: UTF-8 -*-
from impostos import ICMS, ISS, Imposto
from orcamento import Orcamento


class CalculaImpostos(object):
    def realiza_calculo(self, orcamento: Orcamento, imposto: Imposto) -> None:
        imposto_calculado: float = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == "__main__":

    orcamento = Orcamento(500.0)
    calculador_de_impostos: CalculaImpostos = CalculaImpostos()
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

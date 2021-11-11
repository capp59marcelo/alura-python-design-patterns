# -*- coding: UTF-8 -*-
from descontos import (
    DescontoPorCincoItens,
    DescontoPorMaisDeQuinhentosReais,
    SemDesconto,
)
from orcamento import Item, Orcamento


class CalculadorDeDescontos(object):
    def calcula(self, orcamento: Orcamento):
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDeQuinhentosReais(SemDesconto())
        )
        return desconto.calcula(orcamento)


if __name__ == "__main__":

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item A", 100.0))
    orcamento.adiciona_item(Item("Item B", 50.0))
    orcamento.adiciona_item(Item("Item C", 400.0))

    calculador_de_descontos = CalculadorDeDescontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print(f"Desconto calculado : {desconto}")
    # imprime 38.5

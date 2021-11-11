from impostos import ICMS, ICPP, IKCV, ISS, Imposto
from orcamento import Item, Orcamento


class CalculaImpostos(object):
    def realiza_calculo(self, orcamento: Orcamento, imposto: Imposto) -> None:
        imposto_calculado: float = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == "__main__":

    calculador: CalculaImpostos = CalculaImpostos()
    orcamento: Orcamento = Orcamento()
    orcamento.adiciona_item(Item("ITEM 1", 50))
    orcamento.adiciona_item(Item("ITEM 2", 200))
    orcamento.adiciona_item(Item("ITEM 3", 250))

    print("ISS e ICMS")
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print("ICPP e IKCV")
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

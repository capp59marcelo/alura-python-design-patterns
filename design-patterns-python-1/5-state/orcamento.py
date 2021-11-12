import abc


class Item(object):
    def __init__(self, nome: str, valor: float):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


class Orcamento(object):
    def __init__(self):
        self.__itens: list[Item] = []
        self.estado_atual: EstadoDeUmOrcamento = EmAprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(orcamento)

    def reprova(self):
        self.estado_atual.reprova(orcamento)

    def finaliza(self):
        self.estado_atual.finaliza(orcamento)

    def aplica_desconto_extra(self):

        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto: float):

        self.__desconto_extra += desconto

    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):
        return tuple(self.__itens)

    # perguntamos para o orçamento o total de itens
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item: Item):
        self.__itens.append(item)


class EstadoDeUmOrcamento(abc.ABC):
    @abc.abstractmethod
    def aplica_desconto_extra(self, orcamento: Orcamento):
        raise NotImplementedError()

    @abc.abstractmethod
    def aprova(self, orcamento: Orcamento):
        raise NotImplementedError()

    @abc.abstractmethod
    def reprova(self, orcamento: Orcamento):
        raise NotImplementedError()

    @abc.abstractmethod
    def finaliza(self, orcamento: Orcamento):
        raise NotImplementedError()


class EmAprovacao(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento: Orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento: Orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento: Orcamento):
        raise Exception("Orçamento em aprovação não podem ir para finalizado")


class Aprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento: Orcamento):
        raise Exception("Orçamento já está aprovado")

    def reprova(self, orcamento: Orcamento):
        raise Exception("Orçamento aprovados não podem ser reprovados")

    def finaliza(self, orcamento: Orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento):
        raise Exception("Orçamentos reprovados não receberam desconto extra")

    def aprova(self, orcamento: Orcamento):
        raise Exception("Orçamento reprovado não pode ser aprovado")

    def reprova(self, orcamento: Orcamento):
        raise Exception("Orçamento reprovado não pode ser reprovado novamente")

    def finaliza(self, orcamento: Orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento: Orcamento):
        raise Exception("Orçamentos finalizados não receberam desconto extra")

    def aprova(self, orcamento: Orcamento):
        raise Exception("Orçamentos finalizados não podem ser aprovados novamente")

    def reprova(self, orcamento: Orcamento):
        raise Exception("Orçamentos finalizados não podem ser reprovados")

    def finaliza(self, orcamento: Orcamento):
        raise Exception("Orçamentos finalizados não podem ser finalizados novamente")


if __name__ == "__main__":
    orcamento: Orcamento = Orcamento()
    orcamento.adiciona_item(Item("ITEM 1", 50))
    orcamento.adiciona_item(Item("ITEM 2", 200))
    orcamento.adiciona_item(Item("ITEM 3", 250))

    orcamento.aprova()
    orcamento.reprova()

# -*- coding: utf-8 -*-

import abc
from datetime import date


class Comando(abc.ABC):
    @abc.abstractmethod
    def executa(self):
        pass


class Pedido(object):
    def __init__(self, cliente: str, valor: float):

        self._cliente = cliente
        self._valor = valor
        self._status = "NOVO"
        self._data_finalizacao = None

    def paga(self):
        self._status = "PAGO"

    def finaliza(self):
        self._data_finalizacao = date.today()
        self._status = "ENTREGUE"

    @property
    def cliente(self):
        return self._cliente

    @property
    def valor(self):
        return self._valor

    @property
    def status(self):
        return self._status

    @property
    def data_finalizacao(self):
        return self._data_finalizacao


class FilaDeTrabalho(object):
    def __init__(self):
        self._comandos: list[Comando] = []

    def adiciona(self, comando: Comando):
        self._comandos.append(comando)

    def processa(self):
        for comando in self._comandos:
            comando.executa()


class ConcluiPedido(Comando):
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    def executa(self):
        self._pedido.finaliza()


class PagaPedido(Comando):
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    def executa(self):
        self._pedido.paga()


if __name__ == "__main__":

    pedido1 = Pedido("Cliente 1", 100)
    pedido2 = Pedido("Cliente 2", 200)

    fila_de_trabalho = FilaDeTrabalho()
    fila_de_trabalho.adiciona(PagaPedido(pedido1))
    fila_de_trabalho.adiciona(PagaPedido(pedido2))
    fila_de_trabalho.adiciona(ConcluiPedido(pedido1))

    fila_de_trabalho.processa()

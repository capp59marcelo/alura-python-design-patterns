from __future__ import annotations

import abc

import impressora


class Expressao(abc.ABC):
    def __init__(self, expressao_esquerda: Expressao, expressao_direita: Expressao):
        self._expressao_esquerda: Expressao = expressao_esquerda
        self._expressao_direita: Expressao = expressao_direita

    @property
    def expressao_esquerda(self):
        return self._expressao_esquerda

    @property
    def expressao_direita(self):
        return self._expressao_direita

    @abc.abstractmethod
    def avalia(self) -> float:
        raise NotImplementedError()

    def aceita(self, visitor: impressora.Impressora) -> str:
        raise NotImplementedError()


class Numero(Expressao):
    def __init__(self, numero: float):
        self._numero = numero

    def avalia(self):
        return self._numero

    def aceita(self, visitor: impressora.Impressora) -> str:
        return visitor.visita_numero(self)


class Subtracao(Expressao):
    def avalia(self):
        return self._expressao_esquerda.avalia() - self._expressao_direita.avalia()

    def aceita(self, visitor: impressora.Impressora) -> str:
        return visitor.visita_subtracao(self)


class Soma(Expressao):
    def avalia(self):
        return self._expressao_esquerda.avalia() + self._expressao_direita.avalia()

    def aceita(self, visitor: impressora.Impressora) -> str:
        return visitor.visita_soma(self)


if __name__ == "__main__":

    expressao_esquerda = Subtracao(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    visitor = impressora.Impressora()
    print(expressao_conta.aceita(visitor))

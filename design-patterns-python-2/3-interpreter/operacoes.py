import abc


class Expressao(abc.ABC):
    @abc.abstractmethod
    def avalia(self) -> float:
        raise NotImplementedError()


class Numero(Expressao):
    def __init__(self, numero: float):
        self._numero = numero

    def avalia(self):
        return self._numero


class Subtracao(Expressao):
    def __init__(self, expressao_esquerda: Expressao, expressao_direita: Expressao):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita

    def avalia(self):
        return self._expressao_esquerda.avalia() - self._expressao_direita.avalia()


class Soma(Expressao):
    def __init__(self, expressao_esquerda: Expressao, expressao_direita: Expressao):
        self._expressao_esquerda = expressao_esquerda
        self._expressao_direita = expressao_direita

    def avalia(self):
        return self._expressao_esquerda.avalia() + self._expressao_direita.avalia()


if __name__ == "__main__":

    expressao_esquerda = Subtracao(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    resultado = expressao_conta.avalia()
    print(resultado)

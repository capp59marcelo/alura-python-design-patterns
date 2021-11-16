from datetime import date


class Contrato(object):
    def __init__(self, data: date, cliente: str, tipo: str):
        self._data = data
        self._cliente = cliente
        self._tipo = tipo

    @property
    def data(self) -> date:
        return self._data

    @data.setter
    def data(self, data: date) -> None:
        self._data = data

    @property
    def cliente(self) -> str:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: str):
        self._cliente = cliente

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self._tipo = tipo

    def avanca(self) -> None:
        if self._tipo == "NOVO":
            self._tipo = "EM ANDAMENTO"
        elif self._tipo == "EM ANDAMENTO":
            self._tipo = "ACERTADO"
        elif self._tipo == "ACERTADO":
            self._tipo = "CONCLUIDO"

    def salva_estado(self):
        return Estado(Contrato(data=self._data, cliente=self._cliente, tipo=self._tipo))

    def restaura_estado(self, estado):
        self._data = estado.contrato.data
        self._cliente = estado.contrato.cliente
        self._tipo = estado.contrato.tipo


class Estado(object):
    def __init__(self, contrato: Contrato):
        self._contrato = contrato

    @property
    def contrato(self):
        return self._contrato


class Historico(object):
    def __init__(self):
        self._estados_salvos: list[Estado] = []

    def obtem_estado(self, indice: int) -> Estado:
        return self._estados_salvos[indice]

    def adiciona_estado(self, estado: Estado) -> None:
        self._estados_salvos.append(estado)


if __name__ == "__main__":

    historico = Historico()

    contrato = Contrato(data=date.today(), cliente="Flávio Almeida", tipo="NOVO")

    print(contrato.tipo)
    print(contrato.cliente)

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato.tipo)
    print(contrato.cliente)

    contrato.avanca()
    contrato.cliente = "Romulo Henrique"
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    print(contrato.tipo)
    print(contrato.cliente)

    contrato.restaura_estado(historico.obtem_estado(0))

    print(contrato.tipo)
    print(contrato.cliente)

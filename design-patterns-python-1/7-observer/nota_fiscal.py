from datetime import date


class Item(object):
    def __init__(self, nome: str, valor: float):
        self.__nome: str = nome
        self.__valor: float = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


class NotaFiscal(object):
    def __init__(
        self,
        razao_social: str,
        cnpj: str,
        itens: "list[Item]",
        data_de_emissao: date = date.today(),
        detalhes: str = "",
        observadores=[],
    ):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception("Detalhes da nota não pode ter mais do que 20 caracteres")
        self.__detalhes = detalhes
        self.__itens = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return self.__itens


if __name__ == "__main__":

    from observadores import envia_por_email, imprime, salva_no_banco

    itens = [Item("ITEM A", 100), Item("ITEM B", 200)]
    observadores = [envia_por_email, imprime, salva_no_banco]
    nota_fiscal = NotaFiscal(
        cnpj="012345678901234", razao_social="FHSA Limitada", itens=itens, observadores=observadores
    )

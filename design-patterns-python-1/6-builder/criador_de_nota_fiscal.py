from datetime import date

from nota_fiscal import Item, NotaFiscal


class CriadorDeNotaFiscal(object):
    def __init__(self):

        self._razao_social: str
        self._cnpj: str
        self._data_de_emissao: date
        self._itens: list[Item]
        self._detalhes: str

    def com_razao_social(self, razao_social: str):
        self._razao_social = razao_social
        return self

    def com_cnpj(self, cnpj: str):
        self._cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao: date):
        self._data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens: "list[Item]"):
        self._itens = itens
        return self

    def com_detalhes(self, detalhes: str):
        self._detalhes = detalhes
        return self

    def constroi(self):

        if not hasattr(self, "_razao_social"):
            raise Exception("Razão Social deve ser preenchida")

        if not hasattr(self, "_cnpj"):
            raise Exception("CNPJ deve ser preenchido")

        if not hasattr(self, "_itens"):
            raise Exception("Itens deve ser preenchido")

        if not hasattr(self, "__data_de_emissao"):
            self._data_de_emissao = date.today()

        if not hasattr(self, "_detalhes"):
            self._detalhes = ""

        return NotaFiscal(
            razao_social=self._razao_social,
            cnpj=self._cnpj,
            data_de_emissao=self._data_de_emissao,
            itens=self._itens,
            detalhes=self._detalhes,
        )

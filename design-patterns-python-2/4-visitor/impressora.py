from operacoes import Expressao


class Impressora(object):
    def visita_soma(self, soma: Expressao) -> str:
        return f"({soma.expressao_esquerda.aceita(self)} + {soma.expressao_direita.aceita(self)})"

    def visita_subtracao(self, subtracao: Expressao) -> str:
        return f"({subtracao.expressao_esquerda.aceita(self)} - {subtracao.expressao_direita.aceita(self)})"

    def visita_numero(self, numero: Expressao) -> str:
        return f"{numero.avalia()}"

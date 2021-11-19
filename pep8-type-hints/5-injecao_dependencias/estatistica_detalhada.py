from typing import Dict, List, Union


class EstatisticaDetalhada:
    def __init__(self, agencia: str, dia: int):
        self.agencia = agencia
        self.dia = dia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict[str, Union[List[str], str, int]]:
        estatistica: Dict[str, Union[List[str], str, int]] = {}

        estatistica["dia"] = self.dia
        estatistica["agencia"] = self.agencia
        estatistica["quantidade de clientes atendidos"] = len(clientes_atendidos)
        estatistica["clientes atendidos"] = clientes_atendidos

        return estatistica

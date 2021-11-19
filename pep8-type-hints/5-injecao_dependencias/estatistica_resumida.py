from typing import Dict, List, Union


class EstatisticaResumida:
    def __init__(self, agencia: str, dia: int):
        self.agencia = agencia
        self.dia = dia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> Dict[str, Union[List[str], str, int]]:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica[f"{self.agencia}-{self.dia}"] = len(clientes_atendidos)

        return estatistica

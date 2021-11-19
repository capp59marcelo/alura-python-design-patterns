from typing import Dict, List, Union

from constantes import CODIGO_PRIORITARIO
from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{CODIGO_PRIORITARIO}{self.codigo}"

    def chama_cliente(self, caixa: int) -> List[str]:
        mostrar: list[str] = []
        cliente_atual = self.fila.pop(0)
        mostrar.append(f"Cliente: ]{cliente_atual} - Caixa {caixa}")

        if len(self.fila) >= 3:
            mostrar.append(f"Próximo: {self.fila[0]}")
            mostrar.append(f"Fique atento: {self.fila[1]}")

        self.clientes_atendidos.append(cliente_atual)

        return mostrar

    def estatistica(self, dia: str, agencia: str, flag: str) -> Dict[str, Union[List[str], str, int]]:
        estatistica: Dict[str, Union[List[str], str, int]] = {}

        if flag != "detail":
            estatistica = {f"{agencia} - {dia}": len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["clientes atendidos"] = self.clientes_atendidos
            estatistica["quantidade de clientes atendidos"] = len(self.clientes_atendidos)

        return estatistica

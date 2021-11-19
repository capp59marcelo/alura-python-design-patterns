import abc
from typing import Dict, List, Union

from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaBase(metaclass=abc.ABCMeta):

    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    def inseri_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> List[str]:
        ...

    def estatistica(self, retorna_estatistica: Classes) -> Dict[str, Union[int, str, List[str]]]:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)

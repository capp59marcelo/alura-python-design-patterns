from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from estatistica_resumida import EstatisticaResumida
from fabrica_fila import FabricaFila

fila_teste = FabricaFila.pega_fila(TIPO_FILA_NORMAL)
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

fila_teste_2 = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.estatistica(EstatisticaResumida("20/03/2025", 1245)))

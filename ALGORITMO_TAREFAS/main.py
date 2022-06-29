#ALGORITMO TAREFAS
from Tarefa import Tarefa
from ListaTarefa import ListaTarefa

t1 = Tarefa("T1", 1, 2)
t2 = Tarefa("T2", 2, 3)
t3 = Tarefa("T3", 3, 4)
t4 = Tarefa("T4", 4, 5)
t5 = Tarefa("T5", 5, 7)
t6 = Tarefa("T6", 6, 8)

listaTarefa = ListaTarefa([t1, t2, t3, t4, t5, t6])
listaTarefa.gerarLista()

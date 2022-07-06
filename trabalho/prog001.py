from tarefa import Tarefa
from tarefa import Tarefas

t1 = Tarefa("T1", 1, 2, 1)
t2 = Tarefa("T2", 3, 6, 3)
t3 = Tarefa("T3", 2, 3, 2)
t4 = Tarefa("T4", 1, 5, 5)

tarefas = Tarefas([t1, t2, t3, t4])
solucao = tarefas.getSolucao()

for s in solucao:
    print(s.getDescricao())
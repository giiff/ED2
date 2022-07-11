from tarefa import Tarefa
from tarefa import Tarefas

t1 = Tarefa("T1", 1, 5, 500)
t2 = Tarefa("T2", 1, 3, 300)
t3 = Tarefa("T3", 3, 5, 300)

tarefas = Tarefas([t1, t2, t3])
solucao = tarefas.getSolucao()

for s in solucao:
    print(s.getDescricao())

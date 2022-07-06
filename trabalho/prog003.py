from tarefa import Tarefa
from tarefa import Tarefas

t1 = Tarefa("T1", 2, 12, 500)
t2 = Tarefa("T2", 5, 11, 300)
t3 = Tarefa("T3", 2, 6, 300)

tarefas = Tarefas([t1, t2, t3])
solucao = tarefas.getSolucao()

for s in solucao:
    print(s.getDescricao())
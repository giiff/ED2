from tarefa import Tarefa
from tarefa import Tarefas

# a = Tarefa("a", 0, 6, 0)
# b = Tarefa("b", 1, 4, 30)
# c = Tarefa("c", 3, 5, 31)
# d = Tarefa("d", 3, 8, 10)
# e = Tarefa("e", 4, 7, 5)
# f = Tarefa("f", 5, 9, 11)
# g = Tarefa("g", 6, 10, 20)
# h = Tarefa("h", 8, 11, 4)

a = Tarefa("a", 0, 6, 1)
b = Tarefa("b", 1, 4, 1)
c = Tarefa("c", 3, 5, 2)
d = Tarefa("d", 3, 8, 3)
e = Tarefa("e", 4, 7, 4)
f = Tarefa("f", 5, 9, 5)
g = Tarefa("g", 6, 10, 6)
h = Tarefa("h", 8, 11, 7)

tarefas = Tarefas([a,b,c,d,e,f,g,h])
solucao = tarefas.getSolucao()

for s in solucao:
    print(s.getDescricao())
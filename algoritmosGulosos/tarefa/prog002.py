# Solução 1
from tarefas import Tarefa

t4 = Tarefa("T4", 1, 5)
t3 = Tarefa("T3", 2, 3)
t2 = Tarefa("T2", 3, 6)
t1 = Tarefa("T1", 1, 2)

tarefas = [t4, t3, t2, t1]

tarefas.sort(key=lambda x: x.getTamanho())

textoTarefas = "Tarefas: "
for t in tarefas:
    textoTarefas += t.getDescricao() + " "
print(textoTarefas)

solucao = {tarefas[0]}

pos = 0
for i in range(1, len(tarefas), +1):
    if tarefas[i].getInicio() >= tarefas[pos].getFim():
        solucao.add(tarefas[i])
        pos = i

textoSolucao = "Solucao: "
for s in solucao:
    textoSolucao += s.getDescricao() + " "
print(textoSolucao)

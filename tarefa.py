#!/usr/bin/env python
# coding: utf-8

# In[32]:


class Grafo:

  def __init__(self, x, i ,f):
    self.Vertices = x
    self.inicio = i
    self.fim = f
    self.peso = f - i

#Esclher o que termina primeiro:
o1 = Grafo("T1", 0, 2)
o2 = Grafo("T2", 1, 3)
o3 = Grafo("T3", 2, 6)
o4 = Grafo("T4", 4, 6)


lista=[o1, o2, o3, o4, o5]

lista.sort(key=lambda t: t.fim)
for item in lista:
  print(item.fim, item.Vertices)
sol=[]
sol.append(lista[0])
posicao = 0

for i in range(1, len(lista), +1):
  if lista[i].inicio >= lista[posicao].fim:
    solucao.append(lista[i])
    pos = i
print("A quantidade de tarefas é: ", len(sol))


# In[ ]:





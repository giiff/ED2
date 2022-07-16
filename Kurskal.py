
import sys

subgrupo = dict() 
classif = dict()  


def make_set(grafo):
  vertices = list()
  
  for linha in grafo:
    if not (linha[1] in vertices):
      vertices.append(linha[1])
    subgrupo[linha[1]] = linha[1]
    classif[linha[1]] = 1
  
  return vertices


def find(vertice):
  if subgrupo[vertice] != vertice: 
    subgrupo[vertice] = find(subgrupo[vertice]) 
  return subgrupo[vertice]


def union(vertice1, vertice2):
  v1_rotulo = find(vertice1)
  v2_rotulo = find(vertice2)
  
  if v1_rotulo != v2_rotulo:
    if classif[v1_rotulo] > classif[v2_rotulo]:
      subgrupo[v2_rotulo] = v1_rotulo
      classif[v1_rotulo] += classif[v2_rotulo]
    else:
      subgrupo[v1_rotulo] = v2_rotulo
      classif[v2_rotulo] += classif[v1_rotulo]


def kruskal(grafo, vertices, k_clusters):
  MST = list()
  
  clusters = len(vertices)

  for aresta in grafo:
    peso, vertice1, vertice2 = aresta
    if clusters <= k_clusters: 
      break

    if find(vertice1) != find(vertice2): 
      union(vertice1, vertice2)
      MST.append(aresta)
      clusters -= 1
  

def rotule(raiz):
  def rerotule(vertice):
    for j in subgrupo.items():
          if j[1] != j[0] and j[1] == vertice: 
            subgrupo[j[0]] = v  
            rerotule(j[0])
  i = list()
  j = list()
  for v in raiz:
    for i in subgrupo.items(): 
      if i[1] == v: 
        rerotule(i[0])


def order_out_data():
  rotulos = list()
  raiz = list()
  
  for i, j in subgrupo.items(): # Encontra os vertices raiz
    if i == j:
      raiz.append(i)
  rotule(raiz)
  
  try:
    for i, j in subgrupo.items():
      rotulos.append([int(i), int(j)])
  except:
    for i, j in subgrupo.items():
      rotulos.append([i, j])
  
  rotulos.sort()
  
  for i in rotulos:
    print i
  
  return rotulos


def Dict_Arestas(lista):
  grafo = list() 
  
  for j in range(len(lista)):
    i = lista[j].split()
    grafo.append([float(i[2]), i[0], i[1]])
  
  vertices = make_set(grafo)
  grafo.sort()
  
  return grafo, vertices


try:
  elements = sys.argv[1]
except IndexError:
  elements = 'teste.txt'

try:
  k_clusters = int(sys.argv[2])
except IndexError:
  print 'Informe a quantidade de grupos!'
  sys.exit()
  
dados = open(elements, "r")
lista = dados.readlines()  

grafo, vertices = Dict_Arestas(lista)
kruskal(grafo, vertices, k_clusters)
order_out_data()


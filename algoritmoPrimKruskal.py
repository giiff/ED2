import sys

class Grafo():
    def __init__(self, valor):
        self.quantidade_vertices = valor;
        self.matrizGrafo = [[0 for column in range(valor)]for row in range(valor)]
        self.pais = [i for i in range(valor)]

    def imprimir_resultado(self, pai):
        menor_distancia = 0

        for i in range(1, self.quantidade_vertices):
            menor_distancia += self.matrizGrafo[i][pai[i]]
            print('VERTICE({}, {}) PESO:{}'.format(pai[i], i, self.matrizGrafo[i][pai[i]]))
        print("Menor Distancia = {}".format(menor_distancia))

    def minKey(self, menor_caminho, flags_menor_caminho):
        min = sys.maxsize
        for v in range(self.quantidade_vertices):
            if menor_caminho[v] < min and flags_menor_caminho[v] == False:
                min = menor_caminho[v]
                indice_vertice = v

        return indice_vertice

    def prim(self):
        menor_caminho = [sys.maxsize] * self.quantidade_vertices
        pai = [None] * self.quantidade_vertices
        menor_caminho[0] = 0
        flags_menor_caminho = [False] * self.quantidade_vertices
        pai[0] = -1

        for cout in range(self.quantidade_vertices):
            u = self.minKey(menor_caminho, flags_menor_caminho)
            flags_menor_caminho[u] = True
            for v in range(self.quantidade_vertices):
                if self.matrizGrafo[u][v] > 0 and flags_menor_caminho[v] == False and menor_caminho[v] > self.matrizGrafo[u][v]:
                    menor_caminho[v] = self.matrizGrafo[u][v]
                    pai[v] = u

        self.imprimir_resultado(pai)

    def find(self, i):
        while self.pais[i] != i:
            i = self.pais[i]
        return i

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        self.pais[a] = b

    def kruskal(self):
        matriz_grafo = self.matrizGrafo

        for i in range(self.quantidade_vertices):
            for j in range(self.quantidade_vertices):
                if self.matrizGrafo[i][j] == 0:
                    matriz_grafo[i][j] = sys.maxsize

        menor_distancia = 0

        for i in range(self.quantidade_vertices):
            self.pais[i] = i

        cont = 0

        while cont < self.quantidade_vertices - 1:
            min = sys.maxsize
            a = -1
            b = -1
            for i in range(self.quantidade_vertices):
                for j in range(self.quantidade_vertices):
                    if self.find(i) != self.find(j) and matriz_grafo[i][j] < min:
                        min = matriz_grafo[i][j]
                        a = i
                        b = j
            self.union(a, b)
            print('VERTICE({}, {}) PESO:{}'.format(a, b, min))
            cont += 1
            menor_distancia += min
        print("Menor Distancia = {}".format(menor_distancia))

#TESTES
g = Grafo(5)
g.matrizGrafo = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

print("PRIM")
g.prim()
print("\nKRUSKAL")
g.kruskal()

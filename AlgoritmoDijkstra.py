import sys


class Grafo():

    def __init__(self, quantidadeVertices):
        self.quantidadeVertices = quantidadeVertices
        self.matrizGrafo = [[0 for column in range(quantidadeVertices)] for row in range(quantidadeVertices)]

    def imprimirDistancia(self, distancia):
        print("Distância do vértice da fonte:")
        for node in range(self.quantidadeVertices):
            print(node, "t", distancia[node])

    def distanciaMinima(self, distancia, sptSet):

        valorMinimo = sys.maxsize

        for v in range(self.quantidadeVertices):
            if distancia[v] < valorMinimo and sptSet[v] == False:
                valorMinimo = distancia[v]
                indiceValorMinimo = v

        return indiceValorMinimo

    def dijkistra(self, fonte):

        distancia = [sys.maxsize] * self.quantidadeVertices
        distancia[fonte] = 0
        sptSet = [False] * self.quantidadeVertices

        for i in range(self.quantidadeVertices):
            u = self.distanciaMinima(distancia, sptSet)
            sptSet[u] = True

            for v in range(self.quantidadeVertices):
                if self.matrizGrafo[u][v] > 0 and sptSet[v] == False and distancia[v] > distancia[u] + self.matrizGrafo[u][v]:
                    distancia[v] = distancia[u] + self.matrizGrafo[u][v]

        self.imprimirDistancia(distancia)

grafo = Grafo(9)
grafo.matrizGrafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

grafo.dijkistra(0)
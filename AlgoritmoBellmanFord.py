class Grafo():
    def __init__(self, quantidadeVertices):
        self.quantidadeVertices = quantidadeVertices
        self.matrizGrafo =[]

    def adicionarAresta(self, u, v, w):
        self.matrizGrafo.append([u, v, w])

    # utility function used to print the solution
    def imprimirBellmanFord(self, dist):
        print("Distancia do Vertice da Origem")
        for i in range(self.quantidadeVertices):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
        distancia = [float("Inf")] * self.quantidadeVertices
        distancia[src] = 0

        for _ in range(self.quantidadeVertices - 1):
            for u, v, w in self.matrizGrafo:
                if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]:
                    distancia[v] = distancia[u] + w

        for u, v, w in self.matrizGrafo:
            if distancia[u] != float("Inf") and distancia[u] + w < distancia[v]:
                print("Graph contains negative weight cycle")
                return

        self.imprimirBellmanFord(distancia)

g = Grafo(5)
g.adicionarAresta(0, 1, -1)
g.adicionarAresta(0, 2, 4)
g.adicionarAresta(1, 2, 3)
g.adicionarAresta(1, 3, 2)
g.adicionarAresta(1, 4, 2)
g.adicionarAresta(3, 2, 5)
g.adicionarAresta(3, 1, 1)
g.adicionarAresta(4, 3, -3)
g.BellmanFord(0)
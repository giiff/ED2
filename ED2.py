import sys
 
class Grafo():
 
    def __init__(self, vertx):
        self.V = vertx
        self.grafo = [[0 for coluna in range(vertx)]
                      for r in range(vertx)]
 
    def pSol(self, dist):
        print("Distancia melhor")
        for no in range(self.V):
            print(no, "para", dist[no])
 

    def minDistancia(self, dist, sptSet):
 

        min = sys.maxsize
 

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijkstra(self, source):
 
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V
 
        for intem in range(self.V):
 
            u = self.minDistancia(dist, sptSet)
 
            sptSet[u] = True
 

            for v in range(self.V):
                if self.grafo[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.grafo[u][v]: 
                    dist[v] = dist[u] + self.grafo[u][v]
 
        self.pSol(dist)

f = Grafo(2)
f.grafo = [[0, 4, 0, 0, 1, 0, 0, 8, 3],
           [3, 0, 8, 0, 4, 0, 0, 1, 0],

           ]
 
f.dijkstra(0)
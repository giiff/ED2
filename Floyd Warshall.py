# Algoritmo Floyd Warshall em python

# O número de vértices
nV = 4

INF = 999


# Implementação do algoritmo
def floyd_warshall(G):
    distancia = list(map(lambda i: list(map(lambda j: j, i)), G))

     # Adiciona vértices individualmente
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):      
                distancia[i][j] = min(distancia[i][j], distancia[i][k] + distancia[k][j])
    print_solucao(distancia)


# Imprimindo a solução
def print_solucao(distancia):
    for i in range(nV):
        for j in range(nV):
            if(distancia[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distancia[i][j], end="  ")
        print(" ")


G = [[0,   3,   4, INF],
     [INF, 0,   INF, 5],
     [INF, INF, 0,   3],
     [8,   INF, INF, 0]]

floyd_warshall(G)
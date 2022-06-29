#ALGORITMO MOCHILA
from audioop import reverse


class Mochila:
    def __init__(self, valor):
        self.__capacidade = valor
        self.__itens = []

    def getCapacidade(self):
        return self.__capacidade

    def getItens(self):
        return self.__itens

    def encher(self, listaItens):
        listaItens.sort(key = lambda x : x.getMedia(), reverse = True)
      
        
        for i in listaItens:
            print(i.getMedia())

        capacidadeDisponivel = self.getCapacidade()
        posicao = 0

        while capacidadeDisponivel != 0:
            print(capacidadeDisponivel)
            if (listaItens[posicao].getPeso() <= capacidadeDisponivel):
                self.__itens.append(listaItens[posicao])
                capacidadeDisponivel -= listaItens[posicao].getPeso()
            else:
                posicao+=1
        
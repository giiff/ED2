#ALGORITMO ITEM
class Item:
    def __init__(self, nome, peso, valor):
        self.__nome = nome
        self.__peso = peso
        self.__valor = valor
    
    def getNome(self):
        return self.__nome
    def getPeso(self):
        return self.__peso
    def getValor(self):
        return self.__valor
    def getMedia(self):
        return self.__valor/self.__peso
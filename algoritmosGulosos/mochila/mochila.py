class Item:
    def __init__(self, nome, peso, valor):
        self.__nome = nome
        self.__peso = peso
        self.__valor = valor

    def getPeso(self):
        return self.__peso

    def getValorItem(self):
        return self.__valor / self.__peso


class Mochila:
    def __init__(self, pesoMaximo):
        self.__pesoMaximo = pesoMaximo

    def guardarItensPorValor(self, itens=[Item]):
        itens.append(itens)
        #itens.sort(key=lambda x: x.getValorItem())
        solucao = {itens[0]}
        pesoAtual = solucao[0].getPeso()
        for i in range(1, len(itens), +1):
            if pesoAtual > self.__pesoMaximo:
                return solucao
            if pesoAtual + itens[i].getPeso() > self.__pesoMaximo:
                continue
            solucao.add(itens[i])
        return solucao

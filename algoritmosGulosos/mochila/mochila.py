class Item:
    def __init__(self, nome, peso, valor):
        self.__nome = nome
        self.__peso = peso
        self.__valor = valor

    def getNome(self):
        return self.__nome

    def getPeso(self):
        return self.__peso

    def getValorItem(self):
        return self.__valor / self.__peso


class Mochila:
    def __init__(self, pesoMaximo, itens=[]):
        self.__pesoMaximo = pesoMaximo
        self.__itens = itens

    def getItens(self):
        return self.__itens

    def adicionarItem(self, item: Item):
        self.__itens.append(item)

    def getPesoAtual(self):
        peso = 0
        for t in self.__itens:
            peso += t.getPeso()
        return peso

    def guardarItensPorValor(self, itens=[Item]):
        itens.sort(key=lambda x: x.getValorItem())
        for i in range(1, len(itens), +1):
            if self.getPesoAtual() >= self.__pesoMaximo:
                return
            if self.getPesoAtual() + itens[i].getPeso() > self.__pesoMaximo:
                return
            self.adicionarItem(itens[i])

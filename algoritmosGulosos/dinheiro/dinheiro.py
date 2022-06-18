from numpy import double


class Dinheiro:
    def __init__(self, nome: str, valor: double):
        self.__nome = nome
        self.__valor = valor

    def getValor(self):
        return self.__valor

    def __lt__(self, other):
        return self.__valor < other.__valor

    def getNome(self):
        if self.__valor < 1:
            return f"{self.__nome} centavos"
        else:
            return f"{self.__nome} " + ("real" if self.__valor == 1 else "reais")


class Saque:
    def __init__(self):
        self.__dinheiroDecrescente = [
            Dinheiro("Cinco", 0.05),
            Dinheiro("Dez", 0.1),
            Dinheiro("Vinte e cinco", 0.25),
            Dinheiro("Cinquenta", 0.5),
            Dinheiro("Um", 1),
            Dinheiro("Dois", 2),
            Dinheiro("Cinco", 5),
            Dinheiro("Dez", 10),
            Dinheiro("Vinte", 20),
            Dinheiro("Cinquenta", 50),
            Dinheiro("Cem", 100),
            Dinheiro("Duzentos", 200)]
        self.__dinheiroDecrescente.sort(reverse=True)

    def sacarComMaisNotas(self, quantidadeSacar: double, dinheiroSaque=[], indexDinheiroVez=0):
        if indexDinheiroVez >= len(self.__dinheiroDecrescente):
            return dinheiroSaque
        dinheiroVez = self.__dinheiroDecrescente[indexDinheiroVez]
        if quantidadeSacar >= dinheiroVez.getValor():
            dinheiroSaque.append(dinheiroVez)
            quantidadeSacar -= dinheiroVez.getValor()
        if quantidadeSacar < dinheiroVez.getValor():
            indexDinheiroVez += 1
        if quantidadeSacar > 0:
            dinheiroSaque = self.sacarComMaisNotas(
                quantidadeSacar, dinheiroSaque, indexDinheiroVez)
        return dinheiroSaque

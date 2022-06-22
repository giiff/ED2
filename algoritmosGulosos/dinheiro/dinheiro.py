import math
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

    # Solução 1
    def sacarComMaisNotasIterativo(self, valorSacar: double):
        dinheiroSaque = []
        indexVez = 0
        while(valorSacar > 0):
            if valorSacar < self.__dinheiroDecrescente[len(self.__dinheiroDecrescente)-1].getValor():
                return dinheiroSaque
            dinheiroVez = self.__dinheiroDecrescente[indexVez]
            if valorSacar < dinheiroVez.getValor():
                indexVez += 1
                continue
            dinheiroSaque.append(dinheiroVez)
            valorSacar -= dinheiroVez.getValor()
        return dinheiroSaque

    # Solução 2
    def sacarComMaisNotasIterativo2(self, valorSacar: double):
        maiorNota = self.__dinheiroDecrescente[0]
        dinheiroSaque = []
        if valorSacar >= maiorNota.getValor():
            qtdMaiorNota = math.floor(valorSacar / maiorNota.getValor())
            valorMaioresNotas = qtdMaiorNota * maiorNota.getValor()
            valorSacar -= valorMaioresNotas
            for i in range(qtdMaiorNota):
                dinheiroSaque.append(maiorNota)
        dinheiroSaque.extend(self.sacarComMaisNotasIterativo(valorSacar))
        return dinheiroSaque

    # Solução 3
    def sacarComMaisNotasRecursivo(self, valorSacar: double, dinheiroSaque=[], indexDinheiroVez=0):
        if indexDinheiroVez >= len(self.__dinheiroDecrescente):
            return dinheiroSaque
        dinheiroVez = self.__dinheiroDecrescente[indexDinheiroVez]
        if valorSacar >= dinheiroVez.getValor():
            dinheiroSaque.append(dinheiroVez)
            valorSacar -= dinheiroVez.getValor()
        if valorSacar < dinheiroVez.getValor():
            indexDinheiroVez += 1
        if valorSacar > 0:
            dinheiroSaque = self.sacarComMaisNotasRecursivo(
                valorSacar, dinheiroSaque, indexDinheiroVez)
        return dinheiroSaque

class Arco:
    def __init__(self, peso, lugarDeOrigem, lugarDeDestino):
        self.__peso = peso
        self.__lugarDeOrigem = lugarDeOrigem
        self.__lugarDeDestino = lugarDeDestino

    def setPeso(self, peso):
        self.__peso = peso

    def getPeso(self):
        return self.__peso

    def getLugarDeOrigem(self):
        return self.__lugarDeOrigem

    def getLugarDeDestino(self):
        return self.__lugarDeDestino


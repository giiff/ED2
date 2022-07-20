class Lugar:
    def __init__(self, fichas, nome):
        self.__fichas = fichas
        self.__nome = nome

    def setFichas(self, fichas):
        self.__fichas = fichas

    def getFichas(self):
        return self.__fichas

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
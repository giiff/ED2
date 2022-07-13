class Professor:
    def __init__(self, nome, altura, preferencia):
        self.__nome = nome
        self.__altura = altura
        self.__preferencia = preferencia

    def getAltura(self):
        return self.__altura

    def getNome(self):
        return self.__nome

    def getPreferencia(self):
        return self.__preferencia
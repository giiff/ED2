class Vagao:
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__ocupado = False
        self.__professor = None

    def ocupar(self, nome):
        self.__professor = nome
        self.__ocupado = True

    def desocupar(self):
        self.__professor = None
        self.__ocupado = True

    def getCodigo(self):
        return self.__codigo

    def getProfessor(self):
        return self.__professor

    def getOcupado(self):
        return self.__ocupado
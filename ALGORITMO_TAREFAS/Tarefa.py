#ALGORITMO TAREFAS
class Tarefa:
    def __init__(self, nome, inicio, fim):
        self.__nome = nome
        self.__i = inicio
        self.__f = fim
    
    def getNome(self):
        return self.__nome
    def getInicio(self):
        return self.__i
    def getFim(self):
        return self.__f
        
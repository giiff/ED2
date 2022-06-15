class Tarefa:
    def __init__(self, descricao, inicio, fim):
        self.__descricao = descricao
        self.__inicio = inicio
        self.__fim = fim

    def getDescricao(self):
        return self.__descricao

    def getInicio(self):
        return self.__inicio

    def getFim(self):
        return self.__fim

    def getTamanho(self):
        return self.__fim - self.__inicio
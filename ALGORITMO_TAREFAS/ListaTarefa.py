#ALGORITMO TAREFAS
class ListaTarefa:
    def __init__(self, tarefas):
        self.__tarefas = tarefas

    def gerarLista(self):
        self.__tarefas.sort(key = lambda x: x.getFim())
        listaOrganizada = []
        listaOrganizada.append(self.__tarefas[0])
        posicao = 0
        for i in range(1, len(self.__tarefas), +1):
            if self.__tarefas[i].getInicio() >= listaOrganizada[posicao].getFim():
                listaOrganizada.append(self.__tarefas[i])
                posicao = i
        for i in range(len(listaOrganizada)):
            print(listaOrganizada[i].getNome())
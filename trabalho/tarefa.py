from audioop import reverse


class Tarefa:
    def __init__(self, descricao, inicio, fim, peso):
        if peso <= 0:
            print("Peso zero não é permitido")
            return
        self.__descricao = descricao
        self.__inicio = inicio
        self.__fim = fim
        self.__peso = peso

    def getDescricao(self):
        return self.__descricao

    def getInicio(self):
        return self.__inicio

    def getFim(self):
        return self.__fim

    def getTamanho(self):
        return self.__fim - self.__inicio

    def getPeso(self):
        return self.__peso

    def getGanhoPorTempo(self):
        return self.getPeso() / self.getTamanho()

class Tarefas:
    def __init__(self, tarefas = [Tarefa]):
        self.__tarefas = tarefas
        
    def getSolucao(self):
        tarefas = self.__tarefas
        tarefas.sort(key=lambda x: x.getFim())
        tarefas.sort(key=lambda x: x.getGanhoPorTempo(), reverse=True)
        solucao = {tarefas[0]}
        anterior = 0
        for i in range(1, len(tarefas), +1):
            if tarefas[i].getInicio() >= tarefas[anterior].getFim():
                solucao.add(tarefas[i])
                anterior = i
        return solucao

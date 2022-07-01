class Tarefa:
    def __init__(self, nomeT, inicioT, fimT):
        self.__nomeT = nomeT
        self.__inicioT = inicioT
        self.__fimT = fimT

    def getNomeTarefa(self):
        return self.__nomeT

    def getInicioTarefa(self):
        return self.__inicioT

    def getFimTarefa(self):
        return self.__fimT

    def getTamanho(self):
        return self.__fimT - self.__inicioT


t1 = Tarefa("T1", 1, 2)
t2 = Tarefa("T2", 3, 6)
t3 = Tarefa("T3", 2, 3)

tarefas = [ t1, t2,t3 ]

tarefas.sort(key=lambda x: x.getFimTarefa())

solucao = {tarefas[0]}

pos = 0
for i in range(1, len(tarefas), +1):
    if tarefas[i].getInicio() >= tarefas[pos].getFim():
        solucao.add(tarefas[i])
        pos = i

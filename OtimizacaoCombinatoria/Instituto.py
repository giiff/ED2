from Professor import Professor
from Vagao import Vagao


class Instituto:
    def __init__(self, vagoes, professores):
        self.__armario = vagoes
        self.__professores = professores

    def set_armario(self):
        professores = self.__professores
        professores.sort(key=lambda x: x.getAltura(), reverse=True)

        for i in range(len(self.__armario)):
            for j in range(len(self.__armario[i])):
                professores = self.inserir_professor(professores, i, j)

    def inserir_professor(self, professores, i, j):
        for k in range(len(professores)):
            if self.__armario[i][j].getCodigo() in professores[k].getPreferencia():
                self.__armario[i][j].ocupar(professores[k].getNome())
                del professores[k]
                return professores
        if (self.__armario[i][j].getOcupado() == False):
            self.__armario[i][j].ocupar(professores[0].getNome())
            del professores[0]
            return professores

    def imprimir_armario(self):
        for i in range(len(self.__armario)):
            for j in range(len(self.__armario[i])):
                print(self.__armario[i][j].getCodigo(), " - ", self.__armario[i][j].getProfessor())
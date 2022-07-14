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

    def set_armario2(self):
        professores2 = self.__professores
        professores2.sort(key=lambda x: x.getAltura(), reverse=True)

        for i in range(len(self.__armario)):
            for j in range(len(self.__armario[i])):
                professores2 = self.inserir_professor_preferencia(professores2, i, j)

        for i in range(len(self.__armario)):
            for j in range(len(self.__armario[i])):
                if self.__armario[i][j].getOcupado() == False:
                    self.__armario[i][j].ocupar(professores2[0].getNome())
                    del professores2[0]

    def inserir_professor_preferencia(self, professores, i, j):
        for k in range(len(professores)):
            if self.__armario[i][j].getCodigo() in professores[k].getPreferencia():
                self.__armario[i][j].ocupar(professores[k].getNome())
                del professores[k]
                return professores
        return professores

    def desocupar_armario(self):
        for i in range(len(self.__armario)):
            for j in range(len(self.__armario[i])):
                self.__armario[i][j].desocupar()

    def imprimir_armario(self):
        print("ARMARIO:")
        for i in range(len(self.__armario)):
            for j in range(len(self.__armario[i])):
                print(self.__armario[i][j].getCodigo(), " - ", self.__armario[i][j].getProfessor())
from Professor import Professor
from Vagao import Vagao

class Instituto:
    def __init__(self, vagoes, professores):
        self.__armario = vagoes
        self.__professores = professores

    def getArmario(self):
        return self.__armario

    def getProfessores(self):
        return self.__professores

    def set_armario(self):
        p_disponivel = self.getProfessores()
        p_disponivel.sort(key=lambda x: x.getAltura(), reverse=True)

        for i in range(len(self.getArmario())):
            for j in range(len(self.getArmario()[i])):
                p_disponivel = self.inserir_professor(p_disponivel, i, j)

    def inserir_professor(self, p_disponivel, i, j):
        for k in range(len(p_disponivel)):
            if self.getArmario()[i][j].getCodigo() in p_disponivel[k].getPreferencia():
                self.__armario[i][j].ocupar(p_disponivel[k].getNome())
                del p_disponivel[k]
                return p_disponivel
        if (self.getArmario()[i][j].getOcupado() == False):
            self.__armario[i][j].ocupar(p_disponivel[0].getNome())
            del p_disponivel[0]
            return p_disponivel

    def set_armario_preferencia(self):
        p_disponivel = self.getProfessores()
        p_disponivel.sort(key=lambda x: x.getAltura(), reverse=True)

        for i in range(len(self.getArmario())):
            for j in range(len(self.getArmario()[i])):
                p_disponivel = self.inserir_professor_preferencia(p_disponivel, i, j)

        for i in range(len(self.getArmario())):
            for j in range(len(self.getArmario()[i])):
                if self.getArmario()[i][j].getOcupado() == False:
                    self.getArmario()[i][j].ocupar(p_disponivel[0].getNome())
                    del p_disponivel[0]

    def inserir_professor_preferencia(self, p_disponivel, i, j):
        for k in range(len(p_disponivel)):
            if self.getArmario()[i][j].getCodigo() in p_disponivel[k].getPreferencia():
                self.getArmario()[i][j].ocupar(p_disponivel[k].getNome())
                del p_disponivel[k]
                return p_disponivel
        return p_disponivel

    def desocupar_armario(self):
        for i in range(len(self.getArmario())):
            for j in range(len(self.getArmario()[i])):
                self.getArmario()[i][j].desocupar()

    def imprimir_armario(self):
        print("ARMARIO:")
        for i in range(len(self.getArmario())):
            for j in range(len(self.getArmario()[i])):
                print(self.getArmario()[i][j].getCodigo(), " - ", self.getArmario()[i][j].getProfessor())
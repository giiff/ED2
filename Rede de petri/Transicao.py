class Transicao:
    def __init__(self, nome, ordem):
        self.__nome = nome
        self.__ordem = ordem
        self.__situacao = True

    def setFichas(self, fichas):
        self.__fichas = fichas

    def getFichas(self):
        return self.__fichas

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def getOrdem(self):
        return self.__ordem

    def getSituacao(self):
        return self.__situacao

    def setSituacao(self, situacao):
        self.__situacao = situacao


    def getArcosAnteriores(self, listaDeArcos):
        arcosAnteriores = []
        for arco in listaDeArcos:
            if arco.getLugarDeDestino() == self:
                arcosAnteriores.append(arco)
        return arcosAnteriores

    def getArcosPosteriores(self, listaDeArcos):
        arcosPosteriores = []
        for arco in listaDeArcos:
            if arco.getLugarDeOrigem() == self:
                arcosPosteriores.append(arco)
        return arcosPosteriores

    def validarTransicao(self, listaDeArcos):
        #
        arcosAnteriores = self.getArcosAnteriores(listaDeArcos)
        arcosPosteriores = self.getArcosPosteriores(listaDeArcos)

        #Verifica as condicoes
        for arco in arcosAnteriores:
            if arco.getPeso() > arco.getLugarDeOrigem().getFichas():
                return self.setSituacao(False)
        #Se todas as condicoes forem verdadeiras, realiza a troca dos valores
        for arco in arcosAnteriores:
            arco.getLugarDeOrigem().setFichas(arco.getLugarDeOrigem().getFichas() - arco.getPeso())
        for arco in arcosPosteriores:
            arco.getLugarDeDestino().setFichas(arco.getLugarDeDestino().getFichas() + arco.getPeso())
        return self.setSituacao(True)








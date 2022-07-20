from Arco import Arco
from Lugar import Lugar
from Transicao import Transicao

class MontagemDeCarros:
    def __init__(self, rodas, chassis, motores, faroisD, faroisT):
        self.__lugares = list()
        self.__arcos = list()
        self.__transicoes = list()

        montarCarro = Transicao("Montar carro", 1)
        enviarCarro = Transicao("Enviar carro", 2)

        self.setTransicoes([montarCarro, enviarCarro])

        # setando os lugares
        rodas = Lugar(rodas, "Rodas")
        chassis = Lugar(chassis, "Chassis")
        motores = Lugar(motores, "Motores")
        faroisDianteiros = Lugar(faroisD, "Farois dianteiros")
        faroisTraseiros = Lugar(faroisT, "Farois traseiros")
        carroMontado = Lugar(0, "Carros montados")
        carrosEnviados = Lugar(0, "Carros enviados")

        self.setLugares([rodas, chassis, motores, faroisTraseiros, faroisDianteiros, carroMontado, carrosEnviados])

        # setando arcos
        arcoRodas = Arco(4, rodas, montarCarro)
        arcoChassis = Arco(1, chassis, montarCarro)
        arcoMotores = Arco(1, motores, montarCarro)
        arcoFaroisDianteiros = Arco(2, faroisDianteiros, montarCarro)
        arcoFaroisTraseiros = Arco(2, faroisTraseiros, montarCarro)
        arcoCarroMontado = Arco(1, montarCarro, carroMontado)
        arcoCarrosMontados = Arco(3, carroMontado, enviarCarro)
        arcoEnviarCarrosMontados = Arco(3, enviarCarro, carrosEnviados)

        self.setArcos([arcoRodas, arcoChassis, arcoMotores, arcoFaroisDianteiros, arcoFaroisTraseiros, arcoCarroMontado, arcoCarrosMontados,arcoEnviarCarrosMontados])


    def setLugares(self, lugares):
        self.__lugares = lugares

    def getLugares(self):
        return self.__lugares

    def setArcos(self, arcos):
        self.__arcos = arcos

    def getArcos(self):
        return self.__arcos

    def setTransicoes(self, transicoes):
        self.__transicoes = transicoes

    def getTransicoes(self):
        return self.__transicoes

    def getListaDeTransicoesOrdenadas(self):
        listaDeTransicoesOrdenadas = self.getTransicoes()
        listaDeTransicoesOrdenadas.sort(key=lambda x: x.getOrdem())
        return listaDeTransicoesOrdenadas

    def resultado(self):
        for lugar in self.getLugares():
            print(f"{lugar.getNome()} : {lugar.getFichas()}")

    def iniciarMontagem(self):
        sequenciaDeTransicoes = self.getListaDeTransicoesOrdenadas()
        cont = 0
        while(True):
            for transicoes in sequenciaDeTransicoes:
                transicaoAtual = transicoes
                transicaoAtual.validarTransicao(self.getArcos())
            #Conta a quantidade de condicoes que nao podem mais ser ativadas
            for transicao in sequenciaDeTransicoes:
                if not transicao.getSituacao():
                    cont+=1
            if cont == len(sequenciaDeTransicoes):
                for transicao in sequenciaDeTransicoes:
                    transicao.setSituacao(True)
                return self.resultado()
            cont = 0

    def adicionarPecas(self, rodas, chassis, motores, faroisDianteiros, faroisTraseiros):
        for lugar in self.getLugares():
            if lugar.getNome() == "Rodas":
                lugar.setFichas(lugar.getFichas() + rodas)
            elif lugar.getNome() == "Chassis":
                lugar.setFichas(lugar.getFichas() + chassis)
            elif lugar.getNome() == "Motores":
                lugar.setFichas(lugar.getFichas() + motores)
            elif lugar.getNome() == "Farois dianteiros":
                lugar.setFichas(lugar.getFichas() + faroisDianteiros)
            elif lugar.getNome() == "Farois traseiros":
                lugar.setFichas(lugar.getFichas() + faroisTraseiros)







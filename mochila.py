
class Minerio:
	def __init__(self, descriçao, peso, valor):
		self.descriçao = descriçao
		self.peso = peso
		self.valor = valor

	def getValor(self):
		return self.valor

	def getDescriçao(self):
		return self.descriçao

	def getMedia(self):
		return (self.peso / self.valor)


class Mochila:
	def __init__(self, peso):
		self.peso = peso
		self.minerios = []

	def encherMochila(self, lista):
		peso_restante = self.peso
		lista.sort(key = lambda i: i.getMedia())
		pos = 0
		while peso_restante != 0:
			if(lista[pos].getValor() <= peso_restante):
				self.minerios.append(lista[pos])
				peso_restante -= lista[pos].getValor()
			else:
				pos+=1

	def getMinerios(self):
		return self.minerios



mochila = Mochila(50)

lista = [Minerio("Ouro", 20, 6000), 
		 Minerio("Diamante", 10, 3000),
		 Minerio("Cobre", 15, 1000),]

mochila.encherMochila(lista)





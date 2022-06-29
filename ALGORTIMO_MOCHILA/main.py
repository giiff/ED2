from Item import Item
from Mochila import Mochila

mochila = Mochila(50)
listaItens = [Item("Ouro", 3, 100), Item("prata",2,20), Item("diamante", 8, 800), Item("cobre",1,5)]
mochila.encher(listaItens)
for item in mochila.getItens():
    print(item.getNome())
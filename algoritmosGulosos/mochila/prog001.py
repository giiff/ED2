from mochila import Item
from mochila import Mochila

i1 = Item("ouro", 3, 100)
i2 = Item("prata", 2, 20)
i3 = Item("diamante", 8, 800)
i4 = Item("cobre", 1, 5)

mochila = Mochila(15)

itens = [i1, i2, i3, i4]
itens.sort(key=lambda x: x.getValorItem())
mochila.guardarItensPorValor(itens)
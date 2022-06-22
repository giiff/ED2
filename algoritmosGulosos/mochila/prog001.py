from mochila import Item
from mochila import Mochila

i1 = Item("ouro", 3, 100)
i2 = Item("prata", 2, 20)
i3 = Item("diamante", 8, 800)
i4 = Item("cobre", 1, 5)

mochilaPorValor = Mochila(15)
mochilaPorValor.guardarItensPorValor([i1, i2, i3, i4])

# Mostrando resultado das pedras guardadas
textoMochila = "Pedras guardadas: "
for i in mochilaPorValor.getItens():
    textoMochila += i.getNome() + " "
print(textoMochila)

# Mostrando o peso atual da mochila
pesoMochilaTexto = f"Peso mochila: {mochilaPorValor.getPesoAtual()}"
print(f"{pesoMochilaTexto}")
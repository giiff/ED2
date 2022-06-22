from numpy import double
from dinheiro import Saque

saque = Saque()

qtdSacar = (double)(input("Digite a quantidade de dinheiro que deseja sacar: R$ "))

dinheiroSacado = saque.sacarComMaisNotasIterativo2(qtdSacar)

print("\n\n##### Dinheiro sacado ####\n")
dinheiroTexto = ""
for dinheiro in dinheiroSacado:
    dinheiroTexto += f"R$ {dinheiro.getValor()} ({dinheiro.getNome()})\n"
print(dinheiroTexto)
print("##########################")
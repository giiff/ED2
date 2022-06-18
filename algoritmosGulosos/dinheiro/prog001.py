from numpy import double
from dinheiro import Saque

saque = Saque()

textoOutput = "Digite a quantidade de dinheiro que deseja sacar: R$ "

qtdSacar = (double)(input(textoOutput))
textoOutput += str(qtdSacar)

dinheiroSacado = saque.sacarComMaisNotas(qtdSacar)

textoOutput += "\n\n##### Dinheiro sacado ####\n"
for dinheiro in dinheiroSacado:
    textoOutput += f"R$ {dinheiro.getValor()} ({dinheiro.getNome()})\n"
textoOutput += "##########################\n"

print(textoOutput)

# Salvando resultados em um arquivo txt
with open('Output.txt', 'w') as outputArquivo:
    outputArquivo.write(textoOutput)

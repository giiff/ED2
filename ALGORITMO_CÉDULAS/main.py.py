#ALGORITMO CÉDULAS
valor = int(input("Valor:"))
qt_cem, qt_cinquenta, qt_vinte, qt_dez, qt_cinco, qt_dois, qt_um = 0, 0, 0, 0, 0, 0, 0

while(valor>0):
    if (valor >= 100):
        valor -= 100
        qt_cem += 1
    elif(valor >= 50):
        valor -= 50
        qt_cinquenta += 1
    elif(valor >= 20):
        valor -= 20
        qt_vinte += 1
    elif(valor >= 10):
        valor -= 10
        qt_dez += 1
    elif(valor >= 5):
        valor -= 5
        qt_cinco += 1
    elif(valor >= 2):
        valor -= 2
        qt_cinco += 1
    elif(valor >= 1):
        valor -= 1
        qt_cinco += 1

print("Quantidade cédulas 100:", qt_cem)
print("Quantidade cédulas 50:", qt_cinquenta)
print("Quantidade cédulas 20:", qt_vinte)
print("Quantidade cédulas 10:", qt_dez)
print("Quantidade cédulas 5:", qt_cinco)
print("Quantidade cédulas 2:", qt_dois)
print("Quantidade cédulas 1:", qt_um)

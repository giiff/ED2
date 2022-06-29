a  = int(input("digite o valor : "))

l = [100, 50, 20, 10, 5, 2, 1]

l1 = int( a / l[0])
l11 = a - ( l1 * l[0])
print(f"{l1} notas de 100")

l2 = int( l11 / l[1])
l22 = l11 - ( l2 * l[1])
print(f"{l2} notas de 50")

l3 = int( l22 / l[2])
l33 = l22 - ( l3 * l[2])
print(f"{l3} notas de 20")

l4 = int( l33 / l[3])
l44 = l33 - ( l4 * l[3])
print(f"{l4} notas de 10")

l5 = int( l44 / l[4])
l55 = l44 - ( l5 * l[4])
print(f"{l5} notas de 5")

l6 = int( l55 / l[5])
l66 = l55 - ( l6 * l[5])
print(f"{l6} notas de 1")
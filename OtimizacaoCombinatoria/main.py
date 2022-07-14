#JULIANO E LUCAS 
from Instituto import Instituto
from Professor import Professor
from Vagao import Vagao

v = [
  [Vagao(123), Vagao(745)],
  [Vagao(894), Vagao(713)],
  [Vagao(333), Vagao(222)]
]
v2 = [
  [Vagao(123), Vagao(745)],
  [Vagao(894), Vagao(713)],
  [Vagao(333), Vagao(222)]
]
p = [
  Professor("Afrânio", 185, [894]),
  Professor("Jaime", 181, [222, 745]),
  Professor("Samara", 174, [894, 894]),
  Professor("Ugo", 175, [745, 894]),
  Professor("Maria", 174, [713]),
  Professor("Dama de Paus", 195, [222])]
p2 = [
  Professor("Afrânio", 185, [894]),
  Professor("Jaime", 181, [222, 745]),
  Professor("Samara", 174, [894, 894]),
  Professor("Ugo", 175, [745, 894]),
  Professor("Maria", 174, [713]),
  Professor("Dama de Paus", 195, [222])]


i = Instituto(v, p)
i.set_armario()
i.imprimir_armario()

i2 = Instituto(v2, p2)
i2.set_armario_preferencia()
i2.imprimir_armario()


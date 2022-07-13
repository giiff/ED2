from Instituto import Instituto
from Professor import Professor
from Vagao import Vagao

vagoes = [
  [Vagao(123), Vagao(745)],
  [Vagao(894), Vagao(713)],
  [Vagao(333), Vagao(222)]
]
professores = [
  Professor("Afrânio", 185, [713, 894]),
  Professor("Jaime", 181, [123, 745]),
  Professor("Samara", 174, [894, 894]),
  Professor("Ugo", 175, [745, 894]),
  Professor("Maria", 174, [894, 894]),
  Professor("Dama de Paus", 195, [123, 222])]

i = Instituto(vagoes, professores)
i.set_armario()
i.imprimir_armario()

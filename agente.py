from numpy import zeros, fromiter, ndenumerate
from numpy.random import randint as rand
from numpy import sign, ceil
from os import system

# True significa sujeira
space = zeros((3, 3), bool)
for elem in rand(0, 3, (rand(9), 2)): space[*elem] = 1

# A função mostrada abaixo tem o objetivo de detectar sujeira
casas = fromiter((idx for idx, elem in ndenumerate(space) if elem), "2i")

# Casa do início
atual = (1, 1)

system("cls||clear")
print(f"Estado inicial do espaço:\n{space}\n")

contador = 0
for casa in casas:
  while any(atual != casa):
    dif = (casa - atual) / 2
    dif = sign(dif) * ceil(abs(dif))
    dif = dif.astype(int)
    atual += dif
    contador += 1
    print(f"O robô se moveu para {atual}")
  space[*atual] = 0
  print(f"O robô limpou a casa {atual}")
  print(f"O espaço ficou assim:\n{space}\n")

try: print(f"A eficiência foi de {len(casas) / contador}")
except ZeroDivisionError: print("O robô nem se mexeu!")
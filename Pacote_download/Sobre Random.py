import random
from datetime import date
lista = ['pedra', 'papel', 'tesoura']
escolha = random.choice(lista)
print(escolha)


# MEU TESTE AQUI, NEM É SOBRE RANDOM, É MAIS SOBRE DATETIME
hoje = date.today().year
ano = 2003
atual = date.today().year
lista = []
for c in range(hoje, 2003, - 1):
    if c % 4 == 0 and c % 100 != 0 or c % 400 == 0:
        lista.append(366)
    else:
        lista.append(365)
print(lista)
print(sum(lista))

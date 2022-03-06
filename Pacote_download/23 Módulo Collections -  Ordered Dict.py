""""
Módulo Collection -  Ordered Dict

https://docs.python.org/pt-br/3/library/collections.html#collections.OrderedDict

# O dicionário normal nõa garante a ordem dos elementos
# Já o Ordered Dict, como o nome já diz, garante a ordem de inserção do dicionário
# Para utilizar o Ordered Dict é preciso fazer o seu import
# Todas as funções e métodos que funcionam em um dicionário normal funcionam num Ordere Dict

from collections import OrderedDict
dici = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
for k, v in dici.items():
    print(k, v)
dici = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for k, v in dici.items():
    print(k, v)

# Dicionário normal
dici = {'a': 1, 'b': 2}
dici2 = {'b': 2, 'a': 1}
print(dici == dici)  # O resultado vai ser True, pois para o dicionário normal a ordem não importa
# Ordered Dict
dici1 = OrderedDict({'a': 1, 'b': 2})
dici3 = OrderedDict({'b': 2, 'a': 1})
print(dici1 == dici3)  # O resultado vai ser False, pois o Ordered Dict leva em conta ordem
"""

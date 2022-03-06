"""
Dictcionaty Comprehension

Pense o seguinte:

se quisermos criare uma lista fazemos:

lista = ["a", 4, True, "", 2.9]

or

list(("a", 4, True, "", 2.9))

Se quisermos fazer uma tupla:

lista = ("a", 4, True, "", 2.9)

or

tupla = tuple("a", 4, True, "", 2.9)

Se quisermos criar um conjunto:

conjunto = {"a", 4, True, "", 2.9}

Se quisermos criar um dicionário:

dic = {"b": 8, "c": 9, "a": 8}

# Syntax Dictionary Comprehension

{chave: valor for valor in iterável}

# Exemplos

num = {"b": 8, "c": 9, "a": 8}

square = {key: values ** 2 for key, values in num.items()}
print(square)

set_by_dictionary = {values ** 2 for values in num.values()}
print(set_by_dictionary)
print(type(set_by_dictionary))

numeros = [1, 2, 3, 4, 5]  # Lembrando que poderia ser uma tupla ou um conjunto.
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# Lembrando que em dicionários não se pode haver repetição de chaves
# Caso tenha um valor repetido, será desconsiderado.]

chaves = "abcde"
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: numeros[i] for i in range(0, len(valores))}
print(mistura)
"""

valores = [1, 2, 3, 4, 5]

dicio = {num: ("PAR" if num % 2 == 0 else "IMPAR") for num in valores}
print(dicio)

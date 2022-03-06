"""
Set Comprehension

lista = [1, 2, 3, 4, 5}
set = {1, 2, 3, 4, 5}
"""

se = {num for num in range(0, 7)}
print(se)

se1 = {x ** 2 for x in range(11)}
print(se1)

se2 = {x: x ** 2 for x in range(11)}
print(se2)

nome = "Luis Guilherme"
se3 = {nome: letra for letra in nome}
print(se3)

se4 = {nome[i]: nome[i] for i in range(0, len(nome))}
print(se4)

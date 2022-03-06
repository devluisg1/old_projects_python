"""
List Comprehenssion

Utilizando list comprehenssions nós podemos gerar novas listas a partir de
outros iteraveis

[ dado for dado in iterável ]

numeros = [1, 2, 3, 4, 5]
res = [num * 10 for num in numeros]
print(res)
print()

loop = 0
for c in range(6):
    res1 = [num * numeros[c + 1] for num in numeros]
    loop += 1
    print(res1)
    if loop == 4:
        break


def square(value):
    return value ** 2


def maiuscula(name):
    name = name.replace(name, name.upper())
    return name


print()
res2 = [square(num) for num in numeros]
print(res2)

print()
nome = ["Luis", "Guilherme", "Luis", "Guilherme", "Luis", "Guilherme"]
print([maiuscula(n) for n in nome])
print([name.upper() for name in nome])

lista = [num * 3 for num in range(10)]
print(lista)

boollist = [bool(valor) for valor in [0, "", [], 4, 9, 5, 0]]
print(boollist)

strlist = [str(valor) for valor in [1, 7, 2, 8]]
print(strlist)

lista2 = ["lUIS", "gUI"]
res = [letra.upper() for letra in lista2]
print(res)

lis = [1, 7, 8, 0, 8]
lista = []
pos = 0

for c in lis:
    lista.append(c ** 2)

print(lista)

lista5 = []

while pos < len(lis):
    lista5.append(lis[pos] ** 2)
    pos += 1

print(lista5)
"""

"""
2° Parte

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehendsion
"""
"""
# Exemplos

num = list((2, 9, 8, 0, 6, 3, 2, 6))
par = [c for c in num if c != 0 and c % 2 == 0]
impar = [c for c in num if c != 0 and c % 2 != 0]
print(par)
print(impar)
print([c for c in num if c != 0 and c % 2])
print([c for c in num if c != 0 and not c % 2])

lista = "dnafka"
print([c for c in range(len(lista)) for c in lista[c]])


nome = "Luis GUILHERME"
lista = []
for c in nome:
    if c not in " ":
        lista.append(c)
print(lista)


nome = "Luis GUILHERME"
print([c for c in nome if c not in " "])
"""

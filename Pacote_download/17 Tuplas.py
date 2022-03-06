"""
Tuplas

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação
em uma tupla gera um nova tupla

# Tuplas sõa representadas por parênteses
# O cuidado a se tomar é de que: Tuplas são definidas por a vírgula e não por parênteses
# Pode-se gerar uma tupla com range
# O processo de desempacotamento em tuplas é igual o de listas
# Vale lembrar que caso haja um número maior ou menor de elementos doque de variáveis e vice-versa, dará erro
# Métodos de adicão e remoção de elementos em uma túpla não existem, dado o fato de tuplas não serem imutáveis
# Métodos de soma, máximo e mínimo são os mesmos que os das listas, como nas listas os valores precisam ser int e reais
# Há como fazer concatenação de tuplas através de , e do operador +
# Tuplas são imutáveis, porém pode-se sobrescrever os valores destas usando concatenação
# Pode-se verificar os elementos de uma tupla do mesmo jeito de uma lista
# É possível iterar sobre tupla com repetição while e for
# Aconselha-se que use tuplas para coleções que não têm necessidade de mutar, ex: MÊSES
# Pode-se fazer slices em tuplas da mesma forma que se faz nas listas

tupla1 = tuple(range(1, 7))
tupla2 = ("A", "B", "C")
tupla3 = (1, 2, 3)
tupla4 = tuple("LUIS GUILHERME")

tupla = (4, "i", [], True, 4.7)
print(type(tupla))

print(type(()))
tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))
tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))
tupla3 = (4)
print(tupla3)
print(type(tupla3))
tupla4 = (4,)
print(tupla4)
print(type(tupla4))
tupla5 = 5,
print(tupla5)
print(type(tupla5))
(4) > Não é tupla
(4,) > É tupla
4, > É tupla

num = range(1, 7)
tupla1 = tuple(num)
print(tupla1)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

tupla = ("Luis", "Guilherme")
prnm, sgdnm = tupla
print(prnm, sgdnm)

tupla = range(1, 7)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(tupla.__len__())
print(len(tupla))

tupla1 = tuple(range(1, 7))
tupla2 = ("A", "B", "C")
tupla3 = (1, 2, 3)
print(tupla1, tupla1)
soma = tupla2 + tupla3
print(soma)
print(tupla1 + tupla2 + tupla3)
print(tupla1 + tupla3)

tupla1 = tuple(range(1, 7))
tupla2 = ("A", "B", "C")
tupla3 = (1, 2, 3)
print(2 in tupla3)
print("L" in tupla2)
print(8 in tupla1)

for c in tupla1:
    print(c)
for ind, let in enumerate(tupla2):
    print(ind, let)
i = 0
while i < len(tupla4):
    print(tupla4[i])
    i += 1

print(tupla3.count(1))
print(tupla2.count("A"))
print(tupla4.count("E"))

print(tupla4.index("I", 4))

print(tupla4[1])
print(tupla2[2])
print(tupla3[2])

-- Motivos de usar tuplas
# Tuplas são mais rápidas.
# O seu código fica mais seguro, devido a imutábilidade
# Na tupla não temos o problema de shallow copy

tupla = (1, 2, 3)
print(tupla)
nova = tupla
print(nova)
outra = (1, 5, 8, 7)
nova = outra + nova
print(nova)

for c, in enumerate(lanche):
    print(lanche[c])


for c in tupla:
    print(c)

c = 0
enumerate(lanche)
while c < len(lanche):
    print(lanche[c])
    c += 1
"""






"""
Listas
Listas em python funcionam como vetores ou matrizes, são os famosos arrays em outras linguagens
A diferença é que em python as listas são DINÂMICAS e também podermos colacar QUALQUER tipo de dado

Linguagens C/Java: arrays
    Possuem tamanho e tipo de dados fixos!
    Por exemplo se criar um array do tipo int e tamanho 5
    ela só suportará no máximo 5 valores do tipo inteiro
Dinâmico:
    Não possuem tamanho fixo, ou seja, pode-se adicionar elementos, o limite é a memória de computador
Qualquer tipo de dados:
    As listas não possuem qualquer tipo de dado, ou seja pode-se adicionar int, num, bool, float
As listas em python são presentadas por colchetes
As listas são mutáveis, podem mudar constantemente

# Podemos checar facilmente valores contidos em uma lista
# Podemos ordenar uma lista
# Podemos adcionar valores em uma lista
# Com a função append só podemos colocar um elemento por vez
# A função extend não aceita valor único, apenas valores iteraveis
# A função insert adiciona um elemento em uma lista no índice selecionado
# A função insert não apaga valores, ela move o valor que antes estava no índice selecionado para a direita
# Podemos concatenar uma lista na outra, usando +, porém isso equivale o mesmo de usar a função extend
# Podemos reverter uma instring com a função reverse ou usando slice
# É fácil também copiar uma lista usando a função copy
# Pode-se usar o len para contar quantos elementos tem uma lista
# Podemos excluir o último elemento de uma lista usando o pop
# Pode-se remover um elemento pelo índice com a função pop voltando para esquerda o elemento a frente do removido
# Pode-se excluir todos os elementos de ums lista usando a função clear
# Pode-se remover um elemento de uma lista com a função remove e com del
# Pode-se organizar uma lista com o método sort, pode-se organaiza-la de trás pra frente com sort(reverse=True)
# Pode-se replicar os elementos de uma lista multiplanco ela pelo número de vezes de que deseja replicar
# Pode-se separar uma string com a função split transformando-a em uma lista
# Pode-se juntar uma lista com a função join transformando-a numa string
# É possível iterar sobre listas usando for e while
# É possível criar listas com varáveis também
# Listas em python estão em formas indexadas, pode-se acessar os elementos através dos índices
# Imagine as listas como uma roda e valores negativos acessam os índices de trás para frente
# O modo de achar o índice de um elemento é usando a função index
# Pode-se usar a função index escolhando lugares específicos para onde caçar os índices dos elemetos
# Pode-se facilmente usar slices em uma lista
# Ainda usando slice pode-se inverter os valores de uma lista
# Pode-se somar todos os valores de uma lista usando o operador sum, ver o valor máximo usando max e o mínimo usando min
# Pode-se tranformar uma lista em tupla usando o comando tuple()
# Pode-se desempacotar lista, caso haja mais elementos doque varáveis ou haja mais variáveis doque elementos dará erro
# Pode-se copiar uma lista para outra da forma deep copy ou shalow copy
# Com shallow copy a mudança aplicada em uma aplica na outra, com deep copy a mudança só se aplica em uma das listas
# Há como fazer o Deep Copy com fatiamento, apenas diga que a nova lista recebe os valores da outra. Ex: nova = old[:]
# É muito importante saber colocar uma tupla dentro de outra

lista1 = [1, 6, 78, 8, 65, 2323, 78, 3212, 65, 45, 7, 45]
lista2 = ["L", "U", "I", "S", " ", "G", "U", "I", "L", "H", "E", "R", "M", "E"]
lista3 = []
lista4 = list(range(11))
nome = "Luis Guilherme".upper()
lista5 = list(nome)
lista6 = ["c", 4, 4.5, True, bin(998), [123, 1234, 12345]]

print(lista5)
print(lista4)
lista5.sort()
print(lista5)
lista1.sort()
print(lista1)
print(lista1.count(4))
lista1.insert(4, 5)
print(lista1)
lista1.extend(lista5)
print(lista1)
lista1 = lista1 + lista5
print(lista1)

escolha = str(input("Deseja procurar número ou letra? ")).upper().strip()
if escolha == "LET":
    let = str(input("Qual letra deseja procurar na lista5? "))
    if let in lista5:
        print(f"Tem {let} em {lista5}")
    else:
        print("Não têm!")
elif escolha == "NUM":
    lis = int(input("Qual o número da lista que deseja procurar? "))
    num = int(input(f"Qual o número deseja procurar na lista{lis}"))
    if lis == 1:
        if num in lista1:
            print(f"Tem {num} em {lista1}")
        else:
            print("Não têm!")
    elif lis == 4:
        if num in lista4:
            print(f"Tem {num} em {lista4}")
        else:
            print("Não têm!")
    else:
        print("LISTA INEXISTENTE")

let = str(input("Letra desejada: ")).upper()
if let in lista2:
    print(f"Tem {let} em {lista5}\n"
          f"São {lista5.count(let)}")
else:
    print("Não tem a letra ", let

adi = int(input("Qual número deseja adicionar na lista1? "))
lista1.append(adi)
print(lista1)

adi = str(input("Qual número deseja adicionar na lista1? "))
lista1.append(adi)
print(lista1)

lista1.append([1, 2, 3])
print(lista1)
if [1, 2, 3] in lista1:
    print("Encontrei a lista!")
else:
    print("Não encontrei")

lista1.extend([1, 454, 98987])
print(lista1)

print(lista1[:: - 1])
print(lista2[:: - 1])
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
lista6 = lista2
print(lista6)
lista6 = lista2.copy()
print(lista6)

print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))
print(len(lista5))

print(lista5)
lista5.pop()
print(lista5)
lista5.pop()
print(lista5)

lista5.clear()
print(lista5)

lista4 = lista4 * 5
print(lista4)

nome = nome.split()
print(nome)
nome1 = "Luis, python"
nome1 = nome1.split(",")
print(nome1)
print("*".join(lista5))
nome = "Luis Guilherme".split()
print(nome)
nome = " ".join(nome)
print(nome)

soma = 0
for c in lista1:
    print(c)
    soma += c
print(soma)

soma = ""
for c in lista5:
    print(c)
    soma += c
print(soma)

carrinho = []
while True:
    prdt = input("Quais os produtos foram compros? [Q P/Sair]: ").upper()
    if prdt != "Q":
        carrinho.append(prdt)
    else:
        break
for c in carrinho:
    print(c)

print(lista2[7])
print(lista2[-1])

for c in lista5:
    print(c)

indice = 0
while indice <= len(lista5) - 1:
    print(lista5[indice])
    indice += 1

for ind, cor in enumerate(lista5):
    print(ind, cor)

print(lista5.index("I"))

import random
lista = []
while True:
    num = random.randint(1, 15)
    lista.append(num)
    escolha = str(input("Parar? "))
    if escolha == "S":
        break
print(lista)

print(lista5.index("U", 2))
print(lista5.index("I", 3))
print(lista5.index("G", 3, 6))

print(lista5[0: 7: 2])
print(lista5[5:: 3])
print(lista5[-1])
print(lista5[:: 2])
print(lista5[:: - 1])
print(lista5[: 2])
print(lista5[: 4])
print(lista5[5:])
name = ["Luis", "Guilherme"]
name[0], name[1] = name[1], name[0]
print(name)
nomes = ["Luis", "Guilherme"]
nomes.reverse()
print(nomes)

print(sum(lista1))
print(max(lista1))
print(min(lista1))

print(lista1)
print(type(lista1))

tupla = tuple(lista1)
print(tupla)
print(type(tupla))

lista = [1, 2, 3]
num1, num2, num3, = lista
print(num1, num2, num3)

lista = [1, 2, 3]
print(lista)
nova = lista.copy()
nova = lista[:]
print(nova)
nova.append(4)
print(nova)
print(lista)
print("**")
lista = [1, 2, 3]
print(lista)
nova = lista
print(nova)
nova.append(4)
print(nova)
print(lista)

pessoas = []
nome = input("Qual o nome? ")
idadae = int(input("Qual a idade? "))
data = nome, f"idade {idadae}"
print(data)
dados = [["Luis", 15], ["Guilherme", 17], list(data)]
print(dados)
pessoas.append(dados[0])
print(pessoas)
pessoas.append(dados)
print(pessoas)

pessoas = []
nome = input("Qual o nome? ")
idadae = int(input("Qual a idade? "))
data = nome, idadae
print(data)
dados = [["Luis", 15], ["Guilherme", 17], list(data)]
print(dados)
pessoas.append(dados[0])
print(pessoas)
pessoas.append(dados)
print(pessoas)
print(pessoas[0][1])
print(pessoas[0][0])
print(pessoas[1][1])

galera = [["Luis", 13], ["Guilherme", 14], ["Alves", 15]]
for c in galera:
    print(f"{c[0]} tem {c[1]} anos")

lista = []
dado = []
while True:
    nome = str(input("Nome do produto: "))
    price = float(input("Qual o preço "))
    data = [nome, price]
    dado.append(data)
    escolha = str(input("Deseja parar? [S/N]: ")).upper().strip()
    if escolha == "S":
        lista.append(dado)
        break
print(lista)

galera = [["Luis", 13], ["Guilherme", 14], ["Alves", 15]]

galera = []
dado = []
for c in range(1, 4):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

galera = []
dado = []
maior = menor = 0
for c in range(1, 4):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)
for c in galera:
    if c[1] >= 18:
        print(f"{c[0]} é maior de idade pois tem {c[1]} anos")
        maior += 1
    else:
        print(f"{c[0]} não é maior de idade, pois tem {c[1]} anos0")
        menor += 1

lista = [1, 2, 3]
for c in range(len(lista)):
    print(lista[c] * lista[c - 1])

nome = "Luis"
lista = []
for c in nome:
    lista.append(c)

print(lista)
print("+".join(lista))

st = input(str("Digite um número: "))
lista = []
lista1 = []
for c in st:
    lista.append(int(c))
soma = sum(lista)
for i in st:
    lista1.append(i)
lista1 = " + ".join(lista1)
print(lista1, "=", soma)

st = str(4454)
lista = []
for c in st:
    lista.append(int(c))
soma = sum(lista)
print(soma)
lista1 = "+".join(st)
print(lista1, "=", soma)
"""



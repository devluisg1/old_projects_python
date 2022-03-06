"""
Loops são estruturas de repetição, utilizamos iterar sobre sequências ou valores iteráveis
Pode-se fazer loops for em:
STRINGS:
nome = "Luis"
LISTAS:
lista = [0, 1, 2, 3, 4]
RANGE:
num = range(0, 11)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for c in range(10):
    print(sum(range(10)))
    if sum(range(10)) == 45:
        break


for c in range(0, 10, 2):
    print(c)


for i in range(len(a)):
    print(i, a[i])


for c in range(2, 10):
    for x in range(2, c):
        if c % x == 0:
            print(c, "Não é primo")
            break
    else:
        print(c, "É primo")

for c in range(1, 5):
    n = int(input("dkjfka: "))
    if n == 0:
        break

for c in range(1, 5):
    n = int(input("dkjfka: "))
    if n == 0:
        break

"""

nome = "Luis Guilherme"
lista = [0, 1, 2, 3, 4]
num = range(11)
for letra in nome:
    print(letra)


for ind, let in enumerate(nome):
    print(ind, let)

for valor in enumerate(nome):
    print(valor[0])
    # print(valor[1])

# Em enumerate com duas variáveis a primeira equivale o índice, a segunda equivale a letra!
# Se retirarmos a primeira, a segunda assume valor de índice e letra em forma de tupla
soma = 0
loop = int(input("Quantas vezes quer rodar o loop? "))
for c in range(1, loop + 1):
    num = int(input(f"Informe o valor: {c}/{loop} "))
    soma += num

print(soma)
nome = "Luis Guilherme"
for c in nome:
    print(c, end="")

for c in range(4):
    n = int(input("Digite um valor: "))

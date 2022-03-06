"""
    MAIOR E MENOR DE UMA LISTA
    MEU BUG
lista = []
for c in range(1, 6):
    n = int(input(f"Digite o {c}° valor: (APENAS VALORES INTEIROS) (EVITE REPETIR NÚMEROS)"))
    lista.append(n)
menor = min(lista)
lenme = lista.count(menor)
maior = max(lista)
lenma = lista.count(maior)
if lenme == 1:
    print(f"O menor número é {menor} e aparece na posição {lista.index(menor)}")
if lenme == 2:
    print(f"O menor número é {menor} e aparece nas posiçãos {lista.index(menor)}...{lista.index(menor, 2)}")
if lenme == 3:
    print(f"O menor número é {menor} e aparece nas posiçãos {lista.index(menor)}...{lista.index(menor, 2)}..."
          f"{lista.index(menor, 4)}")
if lenme == 4:
    print(f"O menor número é {menor} e aparece nas posiçãos {lista.index(menor)}...{lista.index(menor, 2)}..."
          f"{lista.index(menor, 3)}...{lista.index(menor,  4)}")
if lenme == 5:
    print(f"O menor número é {menor} e aparece nas posiçãos {lista.index(menor)}...{lista.index(menor, 1)}..."
          f"{lista.index(menor, 2)}...{lista.index(menor, 3)}...{lista.index(menor, - 1)}")
if lenma == 1:
    print(f"O maior número é {maior} e aparece na posição {lista.index(maior)}")
if lenma == 2:
    print(f"O maior número é {maior} e aparece nas posiçãos {lista.index(maior)}...{lista.index(maior, 2)}")
if lenma == 3:
    print(f"O maior número é {maior} e aparece nas posiçãos {lista.index(maior)}...{lista.index(maior, 2)}..."
          f"{lista.index(menor, 4)}")
if lenma == 4:
    print(f"O maior número é {maior} e aparece nas posiçãos {lista.index(maior)}...{lista.index(maior, 2)}..."
          f"{lista.index(maior, 3)}...{lista.index(maior,  4)}")
if lenma == 5:
    print(f"O maior número é {maior} e aparece nas posiçãos {lista.index(maior)}...{lista.index(maior, 1)}..."
          f"{lista.index(maior, 2)}...{lista.index(maior, 3)}...{lista.index(maior, - 1)}")

    JEITO CERTO
lista = []
for c in range(1, 6):
    n = int(input(f"Digite o {c}° valor: (APENAS VALORES INTEIROS) "))
    lista.append(n)
menor = min(lista)
maior = max(lista)
print(f"O maior valor foi {maior} e apareceu nas posições", end=" ")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}", end="...")
print(f"\nO menor valor foi {menor} e apareceu nas posições", end=" ")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}", end="...")
"""

"""
    VALORES ÚNICOS EM UMA LISTA
lista = []
while True:
    n = int(input("Digite valores de números inteiros: "))
    if n in lista:
        print("=="*10)
        print("Valor não adicionado pois foi duplicado")
    else:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    escolha = str(input("Quer continuar? [S/N]: ")).upper()
    if escolha == "N":
        break
print(f"Os valores digitados foram {sorted(lista)}")
"""

"""
    LISTA EM ORDEM SEM USAR O SORT
lista = []
for c in range(1, 6):
    n = int(input("Digite um número inteiro: "))
    if c == 1 or n > lista[-1]:
        lista.append(n)
        print(f"Valor {n} adicionado ao fim da lista")
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Valor {n} adicionado na posição {pos}")
                break
            pos += 1
print(lista)
"""

"""
    DADOS DE UMA LISTA
lista = []
while True:
    n = int(input("Digite um número: "))
    escolha = str(input("Quer continuar? [S/N]: ")).upper()
    lista.append(n)
    if escolha == "N":
        break
lista.sort(reverse=True)
print(f"Você digitou {len(lista)} elementos")
print(f"A lista em ordem decrescente é {lista}")
if 5 in lista:
    print("Número 5 encontrado na lista")
else:
    print("Número 5 não encontrado na lista")
"""

"""
    LISTA DE PARES E ÍMPARES
lista = []
listapar = []
listaimpar = []
pares = 0
impares = 0
while True:
    n = int(input("Digite um número: "))
    escolha = str(input("Quer continuar? [S/N]: ")).upper()
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    elif n % 2 != 0:
        listaimpar.append(n)
    if escolha == "N":
        break
print(f"A lista completa é {lista}")
print(f"A lista de números pares é {listapar}")
print(f"A lista de número ímpares é {listaimpar}")
"""

"""
    CONTANDO PARÊNTESES NAS EXPRESSÕES
num = input("Digite a sua expreção: ")
list(num)
le = num.count("(")
re = num.count(")")
if le != re:
    print("Expressão inválida!")
else:
    print("Expressão válida!")

lista = []
simb = "("
num = input("Digite a sua expreção: ")
for simb in num:
    if simb == "(":
        lista.append("(")
    elif simb == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("Válida")
else:
    print("Inválida")
"""

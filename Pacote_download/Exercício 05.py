# from time import sleep
# from datetime import date

"""
    CONTAGEM REGRESSIVA
for c in range(10, -1, - 1):
    print(c)
    sleep(1)
print("\033[35mAcabou\033[m")
"""

""""
    NÚMEROS PARES DE 2 À 50
for c in range(2, 51, 2):
    print(c, end=" ")
print("Acabou")
"""

"""
    DIVISÍVEIS E SOMAS
soma = 0
imx = 0
pmx = 0
print("==" * 20)
intervalo1 = int(input("Qual o 1° parte do intervalo da busca? "))
intervalo2 = int(input("Qual o 2° parte do intervalo da busca? "))
escolha = int(input("Deseja por número ímpares ou pares? ÍMPAR [0] PAR [1] "))
divi = int(input("Divisiveies por quanto? APERTE 0 SE DESEJA NÃO DECLARAR ESTE REQUISÍTO "))
if escolha == 1:
    for c in range(intervalo1, intervalo2 + 1):
        if c % 2 != 0 and c % divi == 0:
            imx += 1
            soma += c
    print(f"A soma dos {imx} valores que se encaixam na sua escolha é"
          f" {soma}")
elif escolha == 0:
    for c in range(intervalo1, intervalo2 + 1):
        if c % 2 == 0 and c % divi == 0:
            pmx += 1
            soma += c
    print(f"A soma dos {pmx} valores que se encaixam na sua escolha é"
          f" {soma}")
else:
    print("ESCOLHA DE PAR OU ÍMPAR INVÁLIDA")
print("==" * 20)
"""

"""
    TABUADA
print("==" * 10)
print("Suas opções:\n"
      "[1] - ADIÇAÕ\n"
      "[2] - SUBTRAÇÃO\n"
      "[3] - MULTIPLICAÇÃO\n"
      "[4] - DIVISÃO")
print("==" * 10)
escolha = int(input("Qual a sua escolha? "))
num = int(input("Qual o número de escolha? "))
if escolha == 1:
    for c in range (1, 11):
        print(f"{num}+{c} = {num + c}")
elif escolha == 2:
    for c in range(1, 11):
        print(f"{num}-{c} = {num - c}")
elif escolha == 3:
    for c in range(1, 11):
        print(f"{num}x{c} = {num * c}")
elif escolha == 4:
    for c in range(1, 11):
        print(f"{num}/{c} = {num / c}")
"""

"""
    SOMA DE PARES
soma = 0
par = 0
for c in range(1, 7):
    n = int(input(f"Digite um número: {c}/6 "))
    if n % 2 == 0:
        par += 1
        soma += n
print(f"São {par} números pares e soma deles é {soma}")
"""

"""
    PROGRESSÃO ARITMÉTICA
pter = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
enesimo = pter + (10 - 1) * razao
for c in range(pter, enesimo + 1, razao):
    print(c, end=" --> ")
print("Acabou")
"""

"""
    NÚMEROS PRIMOS
soma = 0
numero = int(input("Digite um número: "))
for c in range(1, numero + 1):
    if numero % c == 0:
        print("\033[31m", c, "\033[m", end=" ")
        soma += 1
    else:
        print("\033[36m", c, "\033[m", end=" ")
print(f"\nO número {numero} foi dividido {soma}x")
if soma == 2:
    print("\033[31mÉ PRIMO!\033[m")
else:
    print("\033[36mNão é primo!\033[m")
"""

"""
    DETECTOR DE PALÍNDROMOS
nome = str(input("Digite uma frase: Não use acentos")).replace(" ", "").upper()
nome2 = nome[:: - 1]
print(nome, nome2)
if nome == nome2:
    print("É palíndromo!")
else:
    print("Não é palíndromo!")

frase = str(input("Digite uma frase: Não use acentos")).upper().strip()
separado = frase.split()
junto = frase.replace(" ", "")
ultimo = len(junto) - 1
inverso = ""
for let in range(ultimo, - 1, - 1):
    inverso = inverso + junto[let]
print(junto, inverso)
if inverso == junto:
    print("É palíndromo!")
else:
    print("Não é palíndromo!")
"""

"""
    Grupo da maior idade
maior = 0
menor = 0
hoje = date.today().year
for c in range(1, 4):
    idade = int(input(f"Em que ano a {c}° pessoa nasceu? "))
    if hoje - idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"São {maior} pessoas maiores de idade\n"
      f"E {menor} pessoas menores de idade")
"""

"""
maior = 99999999
menor = 1
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}° pessoa? "))
    if peso < maior:
        maior = peso
    elif peso > menor:
        menor = peso
print(f"O maior é {menor} e o menor é {maior}")

# Segunda forma

maior = 99999999
menor = 1
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}° pessoa? "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior é {maior} e o menor é {menor}")
"""

"""
    ANALISADOR COMPLETO
velho = 0
media = 0
mm20 = 0
for c in range(1, 5):
    print("==" * 20)
    nome = str(input(f"Digite o nome da {c}° pessoa: ")).upper().strip()
    idade = int(input(f"Digite a idade da {c}° pessoa: "))
    sexo = str(input(f"Digite o sexo da {c}° pessoa: [M/F] ")).upper().strip()
    media += idade / 4
    if sexo == "F" and idade < 20:
        mm20 += 1
    elif sexo == "M":
        if c == 1:
            velho = idade
        if idade > velho:
            velho = nome
print("==" * 20)
print(f"A média de idade do grupo é de {media} anos\n"
      f"O homem mais velho se chama {velho}\n"
      f"E no total há {mm20} mulheres menores de 20 anos")
"""

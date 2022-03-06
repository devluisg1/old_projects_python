# from random import randint
# from time import sleep
# from math import factorial
"""
    VALIDAÇÃO DE DADOS
sexo = str(input("Qual o seu sexo [M/F]: ")).upper()
if sexo == "M":
    print("Dados salvos com sucesso!")
elif sexo == "F":
    print("Dados salvos com sucesso!")
else:
    while sexo != "M" or "F":
        sexo = input("Dados inválidos! Responda com [F/M]: ").upper()
        if sexo == "F":
            print("Dados salvos com sucesso")
            break
        elif sexo == "M":
            print("Dados salvos com sucesso!")
            break

sexo = str(input("Informe seu sexo [F/M]: ")).upper().strip()
while sexo != "F" or "M":
    sexo = str(input("Dados inválidos, por favor informe seu sexo [F/M]: ")).upper()
    if sexo == 'F':
        print(f"Sexo {sexo} registrado com sucesso!")
        break
    elif sexo == 'M':
        print(f"Sexo {sexo} registrado com sucesso!")
        break

sexo = str(input("Informe seu sexo [F/M]: ")).upper().strip()
while sexo not in "MF":
    sexo = str(input("Dados inválidos, por favor informe seu sexo [F/M]: ")).upper().strip()
print(f"Sexo {sexo} registrado com sucesso!")
"""

"""
    JOGO DA ADVINHAÇÃO V 2.0
computador = randint(0, 11)
tentativas = 0
jogador = int(input("Vamos brincar de advinhação! Eu pensei em um número de 0 a 10, que número é esse? "))
while jogador != computador:
    if jogador < computador:
        tentativas += 1
        jogador = int(input("O número que eu escolhi é um número maior, tente denovo: "))
        if jogador == computador:
            print("AEEE, FINALMENTE")
    elif jogador > computador:
        tentativas += 1
        jogador = int(input("O número que eu escolhi é um número menor, tente denovo: "))
        if jogador == computador:
            print("AEEE, FINALMENTE")
print(f"Acertou depois de {tentativas + 1} tentativas")
"""

"""
    MENU DE OPÇÕES
print("==" * 15)
n = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
escolha = 0
while escolha != 5:
    print("==" * 15)
    print("SUAS OPÇÕES:\n"
          "[1] - SOMAR\n"
          "[2] - MULTIPLICAR\n"
          "[3] - > OU <\n"
          "[4] - NOVOS NÚMEROS\n"
          "[5] - SAIR DO PROGRAGA")
    escolha = int(input(": "))
    if escolha == 1:
        print("==" * 15)
        print(f"{n}+{n2}={n + n2}")
    elif escolha == 2:
        print("==" * 15)
        print(f"{n}x{n2}={n * n2}")
    elif escolha == 3:
        print("==" * 15)
        if n > n2:
            print(f"O maior é {n}")
        elif n < n2:
            print(f"O maior é {n2}")
        elif n == n2:
            print("Os valores são iguais")
            exit(escolha)
    elif escolha == 4:
        print("==" * 15)
        n = int(input("Digite os primeiro novo valor: "))
        n2 = int(input("Digite o segundo novo valor: "))
    elif escolha not in (1, 2, 3, 4, 5):
        print("==" * 15)
        print("Dados inválidos, tente denovo.")
print("==" * 15)
for c in range(1, 4):
    print("." * c)
    sleep(1)
print("Programa finalizado!")
print("==" * 15)
"""

"""
    CÁLCULO DE FATORIAL
f = 1
n = int(input("Digite o valor para calcular o fatorial: "))
for c in range(n, 0, -1):
    f *= c
    print(c, "x" if c > 1 else "=", end=" ")
print(f)

f = 1
n = int(input("Digite o valor para calcular o fatorial: "))
c = n
while c > 0:
    f *= c
    print(c, "x" if c > 1 else "=", end=" ")
    c -= 1
print(f)

n = int(input("Digite o valor para calcular o fatorial: "))
for c in range(n, 0, -1):
    print(c, "x" if c > 1 else "=", end=" ")
print(factorial(n))
"""

"""
    PA 2.0
prt = int(input("Digite o primeiro termo dessa pa: "))
razao = int(input("Digite a razão dessa PA: "))
enesimo = (prt + (10 - 1) * razao) + 1
c = prt + razao
while c < enesimo + razao:
    print(c, ">>>" if c < enesimo - 1 else ">>", end=" ")
    c += razao
print("ACABOU")

prt = int(input("Digite o primeiro termo dessa pa: "))
razao = int(input("Digite a razão dessa PA: "))
termo = 1
c = 1
while c <= 10:
    c += 1
    termo += razao
    print(termo, end=" ")
print("Acabou")
"""

"""
    SUPER PA
prt = int(input("Digite o primeiro termo dessa pa: "))
razao = int(input("Digite a razão dessa PA: "))
termo = prt
c = 1
total = 0
escolha = 10
while escolha != 0:
    total += escolha
    while c <= total:
        c += 1
        termo += razao
        print(termo, end=" >>> ")
    print("Pausa")
    escolha = int(input("Deseja adicionar quantos termos nesta PA? "))
print("Acabou")
print(f"Foram mostrados o total de {total} termos")
"""

"""
    SEQUÊNCIA DE FIBONACCI
print("Sequência de FIBONACCI")
termos = int(input("Desaja mostrar quantos termos? "))
n = 0
n2 = 1
c = 3
print(f"{n} >>> {n2}", end=" >>> ")
while c <= termos:
    n3 = n + n2
    print(f"{n3}", end=" >>> ")
    n = n2
    n2 = n3
    c += 1
print("ACABOU")
"""

"""
n = 0
soma = 0
values = 0
while n != 999:
    n = int(input("Digite um número [DIGITE 999 para parar!]: "))
    soma += n
    values += 1
print(f"Você digitou {values - 1} valores e a soma destes é {soma - 999}")
"""

'''
    MAIOR E MENOR NÚMERO 2.0
resp = " "
soma = 0
num = 0
menor = 9999999
maior = 1
while resp != "N":
    n = int(input("Digite um número: "))
    resp = str(input("Quer continuar [S/N]: ")).upper().strip()
    soma += n
    num += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f"Você digitou {num} números e média destes é {soma / num}\n"
      f"O maior valor digitado foi {maior} e o menor foi {menor}")

resp = " "
soma = 0
num = 0
menor = 0
maior = 0
while resp != "N":
    n = int(input("Digite um número: "))
    resp = str(input("Quer continuar [S/N]: ")).upper().strip()
    soma += n
    num += 1
    if num == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"Você digitou {num} números e média destes é {soma / num}\n"
      f"O maior valor digitado foi {maior} e o menor foi {menor}")
'''

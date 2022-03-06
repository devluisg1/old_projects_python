import random
"""
    ANÁLISE DE PESO
pessoas = []
escolha = " "
while escolha != "N":
    nome = str(input("Nome: ")).upper().strip()
    peso = float(input("Peso: "))
    junto = nome, peso
    pessoas.append(list(junto))
    escolha = str(input("Quer continuar? [S/N]: ")).upper()
maior = 0
menor = 99999999999999999999999999999999999999999999999999999999999999999999
print(f"Você cadastrou o total de {len(pessoas)} pessoas")
for i, v in enumerate(pessoas):
    if pessoas[i][1] > maior:
        maior = pessoas[i][1]
for i, v in enumerate(pessoas):
    if pessoas[i][1] < menor:
        menor = pessoas[i][1]
print(f"O maior peso é {maior}Kg, que é o peso de ", end=" ")
for i, v in enumerate(pessoas):
    if maior == pessoas[i][1]:
        print(pessoas[i][0], end=" ")
print(f"\nO menor peso é {menor}Kg, que é o peso de ", end=" ")
for i, v in enumerate(pessoas):
    if menor == pessoas[i][1]:
        print(pessoas[i][0], end=" ")
"""

"""
    LISTA ÚNICA DE PARES E ÍMPARES
lista = [[], []]
for c in range(1, 8):
    num = int(input(f"Digite o {c}° número inteiro: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f"Os números pares desta lista são: {sorted(lista[0])}")
print(f"Os números ímpares desta lista são {sorted(lista[1])}")
"""

"""
    MATRIZ 
matriz = [[], [], []]
for c in range(3):
    for i in range(3):
        num = int(input(f"Digite os número da matriz [{c}/{i}]: "))
        matriz[c].append(num)
for c in range(3):
    for i in range(3):
        print(f"[{matriz[c][i]:^5}]", end=" ")
    print()
"""

"""
    MAIS SOBRE MATRIZES
par = 0
matriz = [[], [], []]
segline = []
ter = 0
# maior = 0
for c in range(3):
    for i in range(3):
        num = int(input(f"Digite os número da matriz [{c}/{i}]: "))
        if num % 2 == 0:
            par += num
        if c == 0:
            matriz[0].append(num)
        elif c == 1:
            matriz[1].append(num)
            segline.append(num)
        elif c == 2:
            matriz[2].append(num)
for c in range(3):
    for i in range(3):
        print(f"[{matriz[c][i]:^5}]", end=" ")
    print()
print("==" * 22)
for c in range(3):
    ter += matriz[c][2]
# for c in range(3):
#    if c == 0:
#        maior = matriz[1][c]
#    elif matriz[1][c] > maior:
#        maior = matriz[1][c]
print(f"A soma dos número pares desta lista é {par}")
print(f"A soma dos números da terceira coluna é {ter}")
print(f"O maior valor da segunda linha é {max(segline)}")
# print(f"O maior valor da segunda linha é {maior}")
print("==" * 22)
"""

"""
    PALPITE DA MEGASENA
print("==" * 20)
print("ESCOLHA QUANTOS JOGOS QUER FAZER COM A SEQUÊNCIA DE 1 A 60")
jogos = int(input("Quantos jogos deseja fazer? "))
print("==" * 20)
for c in range(jogos):
    palpite = []
    while len(palpite) != 6:
        r = random.randint(1, 60)
        if r not in palpite:
            palpite.append(r)
    print(f"JOGO {c + 1}: {palpite}")
"""

"""
    ANÁLISE DE NOTAS 
lista = []
media = []
a = "NOME"
b = "MÉDIA"
escolha3 = " "
escolha2 = 0
while escolha3 != "N":
    nome = str(input("Nome do alunos(a): "))
    n1 = float(input("1° Nota do aluno(a): "))
    n2 = float(input("2° Nota do alunoa(a): "))
    media.append((n1 + n2) / 2)
    junto = [nome, n1, n2]
    list(junto)
    lista.append(junto)
    escolha = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if escolha == "N":
        print("==" * 22)
        print(f"{a:<22}", f"{b:>21}")
        print("==" * 22)
        for i, v in enumerate(lista):
            print(f"{[i]} {lista[i][0]:<20}", end="")
            print(f"{media[i]:>20}")
        print("==" * 22)
        while True:
            escolha2 = int(input("Deseja ver as notas de qual aluno? [Digite 999 para parar]: "))
            if escolha2 == 999:
                break
            if escolha2 not in range(0, len(lista)):
                while escolha2 not in range(0, len(lista)):
                    escolha2 = int(input("Aluno inexistente! Tente novamente: "))
            print(f"As notas de {lista[escolha2][0]} são {lista[escolha2][1]} e {lista[escolha2][2]}")
        escolha3 = str(input("Deseja adicionar aluno(s)? [S/N]: ")).upper()
        if escolha3 == "N":
            break
"""

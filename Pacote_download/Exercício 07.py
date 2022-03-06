# from random import randint
"""
    INTERROMPENDO COM BREAK
s = c = 0
while True:
    n = int(input("Digite um número [0 PARA PARAR]:"))
    if n == 0:
        break
    s += n
    c += 1
print(f"Você digitou {c} números e soma destes foi {s}")
"""

"""
    TABUADA 3.0
while True:
    n = int(input("Deseja ver a tabuada de qual número? [DIGITE 0 PARA FINALIZAR] "))
    print("==" * 10)
    print("Suas opções:\n"
          "[1] - ADIÇAÕ\n"
          "[2] - SUBTRAÇÃO\n"
          "[3] - MULTIPLICAÇÃO\n"
          "[4] - DIVISÃO")
    print("==" * 10)
    escolha = int(input("Qual a sua escolha? "))
    if n == 0:
        break
    if escolha == 1:
        for c in range(1, 11):
            print(f"{n} + {c} = {n + c}")
    elif escolha == 2:
        for c in range(1, 11):
            print(f"{n} - {c} = {n - c}")
    elif escolha == 3:
        for c in range(1, 11):
            print(f"{n} x {c} = {n * c}")
    elif escolha == 4:
        for c in range(1, 11):
            print(f"{n} / {c} = {round(n / c, 2)}")
"""

"""
    JOGO DO PAR OU ÍMPAR
vitoria = 0
escolha1 = " "
while escolha1 != "N":
    while True:
        computador = randint(1, 9)
        print("~=" * 22)
        jogador = int(input("Digite um valor: "))
        escolha = str(input("[P/I]: ")).upper().strip()
        pi = (computador + jogador)
        if escolha == "P":
            if pi % 2 == 0:
                print("~=" * 22)
                print(f"Jogador venceu!\n"
                      f"Jogador escolheu {jogador}\n"
                      f"Computador escolheu {computador}\n"
                      f"A soma destes é {jogador + computador} sendo este um número par")
                vitoria += 1
            if pi % 2 != 0:
                print("~=" * 22)
                print(f"Jogador perdeu!\n"
                      f"Jogador escolheu {jogador}\n"
                      f"Computador escolheu {computador}\n"
                      f"A soma destes é {jogador + computador} não sendo este um número par\n"
                      f"Você ganhou {vitoria} vez(es)")
                print("~=" * 22)
                escolha1 = str(input("Deseja jogar denovo? [S/N] ")).upper().strip()
                if escolha1 == "N":
                    break
        elif escolha == "I":
            if pi % 2 != 0:
                print("~=" * 22)
                print(f"Jogador venceu!\n"
                      f"Jogador escolheu {jogador}\n"
                      f"Computador escolheu {computador}\n"
                      f"A soma destes é {jogador + computador} sendo este um número ímpar")
                vitoria += 1
            if pi % 2 == 0:
                print("~=" * 22)
                print(f"Jogador perdeu!\n"
                      f"Jogador escolheu {jogador}\n"
                      f"Computador escolheu {computador}\n"
                      f"A soma destes é {jogador + computador} não sendo este um número ímpar\n"                 
                      f"Você ganhou {vitoria} vez(es)")
                print("~=" * 22)
                escolha1 = str(input("Deseja jogar denovo? [S/N] ")).upper().strip()
                if escolha1 == "N":
                    break

vitoria = 0
while True:
    computador = randint(1, 9)
    print("~=" * 22)
    jogador = int(input("Digite um valor: "))
    escolha = str(input("[P/I]: ")).upper().strip()
    pi = (computador + jogador)
    if escolha == "P":
        if pi % 2 == 0:
            print("~=" * 22)
            print(f"Jogador venceu!\n"
                  f"Jogador escolheu {jogador}\n"
                  f"Computador escolheu {computador}\n"
                  f"A soma destes é {jogador + computador} sendo este um número par")
            vitoria += 1
        if pi % 2 != 0:
            print("~=" * 22)
            print(f"Jogador perdeu!\n"
                  f"Jogador escolheu {jogador}\n"
                  f"Computador escolheu {computador}\n"
                  f"A soma destes é {jogador + computador} não sendo este um número par\n"
                  f"Você ganhou {vitoria} vez(es)")
            print("~=" * 22)
            break
    elif escolha == "I":
        if pi % 2 != 0:
            print("~=" * 22)
            print(f"Jogador venceu!\n"
                  f"Jogador escolheu {jogador}\n"
                  f"Computador escolheu {computador}\n"
                  f"A soma destes é {jogador + computador} sendo este um número ímpar")
            vitoria += 1
        if pi % 2 == 0:
            print("~=" * 22)
            print(f"Jogador perdeu!\n"
                  f"Jogador escolheu {jogador}\n"
                  f"Computador escolheu {computador}\n"
                  f"A soma destes é {jogador + computador} não sendo este um número ímpar\n"                 
                  f"Você ganhou {vitoria} vez(es)")
            print("~=" * 22)
            break


"""

"""
    ANÁLISE DE DADOS DO GRUPO
maiori = homens = mm20 = 0
while True:
    idade = int(input("IDADE: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("SEXO [M/F]: ")).upper().strip()
    if idade >= 18:
        maiori += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mm20 += 1
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("DESEJA CONTINUAR? [S/N]: ")).upper().strip()
    if escolha == "N":
        break
print(f"Foram cadastradas {maiori} pessoas maior(es) de 18 anos\n"
      f"Foram cadastrados {homens} homens\n"
      f"Foram cadastrada(s) {mm20} mulheres com menos de 20 anos")
"""

"""
    ESTATÍSTICA EM PRODUTO
s = caro = 0
menor = 99999999999999999999
barato = menor
while True:
    produto = input("Qual o nome do produto? ")
    price = int(input("Qual o preço do produto? R$"))
    s += price
    if price > 1000:
        caro += 1
    if price < menor:
        menor = price
        barato = produto
    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Deseja continuar? [S/N]:")).upper().strip()
    if escolha == "N":
        break
print(f"O tatol da compra foi R${s}\n"
      f"O total de produtos acima de R$1000 foi de {caro}\n"
      f"O produto mais barato foi: {barato} custando R${menor}")
      
s = caro = 0
menor = 0
barato = " "
c = 0
while True:
    produto = input("Qual o nome do produto? ")
    price = int(input("Qual o preço do produto? R$"))
    s += price
    c += 1
    if c == 1 or price < menor:
        menor = price
        barato = produto
    if price > 1000:
        caro += 1
    if price < menor:
        menor = price
        barato = produto

    escolha = " "
    while escolha not in "SN":
        escolha = str(input("Deseja continuar? [S/N]:")).upper().strip()
    if escolha == "N":
        break
print(f"O tatol da compra foi R${s}\n"
      f"O total de produtos acima de R$1000 foi de {caro}\n"
      f"O produto mais barato foi: {barato} custando R${menor}")

"""

'''
    SIMULADOR DE CAIXA ELETRÔNICO
print("~~" * 15)
print("BANK MERRILL LYNCH")
print("~~" * 15)
valor = int(input("Qual o valor que deseja sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print("~~" * 15)
print("Volte sempre BANK MERRIL LYNCH")
'''
print("~~" * 15)
print("BANK MERRILL LYNCH")
print("~~" * 15)
valor = int(input("Qual o valor que deseja sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print("~~" * 15)
print("Volte sempre BANK MERRIL LYNCH")
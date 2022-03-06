# from datetime import date
# from time import sleep
# import random
"""
    APROVANDO EMPRÉSTIMO
empr = float(input("Qual o valor do empréstimo que você está pedindo? R$"))
salario = float(input("Qual o seu salário? R$"))
escolha = str(input("Deseja pagar em meses ou anos? (Digite M para meses e A para anos)")).upper().strip()
if escolha == "M":
    tempo = float(input("Deseja pagar em quantos meses? "))
    prest = empr / tempo
    if prest > salario / 100 * 30:
        print(f"A prestação mensal do empréstimo solicitado é de {round(prest, 2)} "
              f"\nque correponde mais de 30% do seu salário, portanto o empréstimo foi NEGADO!")
    else:
        print("O empréstimo foi ACEITO!")
elif escolha == "A":
    tempo = float(input("Deseja pagar em quantos anos? "))
    prest = empr / (tempo * 12)
    if prest > salario / 100 * 30:
        print(f"A prestação mensal do empréstimo solicitado é de {round(prest, 2)} "
              f"\nque correponde mais de 30% do seu salário, portanto o empréstimo foi NEGADO!")
    else:
        print(f"A prestação mensal do empréstimo solicitado é de {round(prest, 2)} "
              f"\nque correponde mais de 30% do seu salário, portanto o empréstimo foi NEGADO!")
"""

"""
    CONVERSOR DE BASES NUMÉRICAS
num = int(input("Digite um número: "))
print("==" * 10)
print((f"DESEJA CONVERTER {num} para:\n"
       f"BINÁRIO - DIGITE 0\n"
       f"OCTAL - DIGITE 1\n"
       f"HEXADÉCIMAL - DIGITE 2\n"))
print("==" * 10)
escolha = int(input(": "))
if escolha == 0:
    print(bin(num)[2:])
elif escolha == 1:
    print(oct(num)[2:])
elif escolha == 2:
    print(hex(num)[2:])
"""

"""
    COMPARADOR DE NÚMEROS
num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num > num2:
    print("O primeiro valor é maior!")
elif num2 > num:
    print("O segundo valor é maior!")
elif num == num2:
    print("Os dois valores são iguais!")
"""

"""
    ALISTAMENTO MILITAR
ano = int(input("Em que ano você nasceu? "))
sexo = str(input("Qual o seu sexo? ")).upper().strip()
atual = date.today().year
idade = atual - ano
if sexo == "FEMININO":
    print("O seu alistamento não é obrigatório!")
elif sexo == "MASCULINO":
    if idade < 18:
        print(f"Você tem {idade} anos, ainda falta(m) {18 - idade} ano(s)\n"
              f"seu alistamento será em {ano + 18}")
    elif idade == 18:
        print("Faça seu alistamento imediatamente!")
    elif idade > 18:
        print(f"Você tem {idade} anos, você deveria ter se alistado a {idade - 18} anos\n"
              f"O ano do seu alistamento foi {atual - (idade - 18)}")
"""

"""
    MÉDIA ESCOLAR
nome = str(input("Qual o nome do aluno? "))
pn = float(input("Digite a primeira nota: "))
pn2 = float(input("Digite a segunda nota: "))
soma = pn + pn2
media = soma / 2
if media >= 7:
    print(f"O alundo teve média {media}\n"
          f"Portanto o aluno {nome} foi APROVADO!")
elif media < 7:
    if media < 5:
        print(f"O aluno {nome} teve média {media} portanto foi REPROVADO!")
    elif 5 < media <= 6.9:
        print(f"O aluno {nome} teve média {media} portanto está de RECUPERAÇÃO!")
"""

"""
    Classificando Atletas
nome = str(input("Qual o nome do atleta? "))
ano = int(input("Em que ano o atleta nasceu? "))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print(f"O atleta {nome} é da categoria MIRIM, pois tem {idade}")
elif 9 < idade <= 14:
    print(f"O atleta {nome} é da categoria INFANTIL, pois tem {idade}")
elif 14 < idade <= 19:
    print(f"O atleta {nome} é da categoria JUNIOR, pois tem {idade}")
elif 19 < idade <= 25:
    print(f"O atleta {nome} é da categoria SÊNIOR, pois tem {idade}")
elif idade > 25:
    print(f"O atleta {nome} é da categoria MASTER, pois tem {idade}")
"""

"""
    ANALISADOR DE TRIÂNGULOS
s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))
if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print("Pode fomar um triângulo!\n"
              "Sendo este um triângulo EQUILÁTERO")
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print("Pode fomar um triângulo!\n"
              "Sendo este um triângulo ESCALENO")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Pode fomar um triângulo!\n"
              "Sendo este um triângulo ISÓSCELES")
else:
    print("Não pode formar um triângulo!")
"""

"""
    IMC
peso = float(input("Qual o seu peso? Kg"))
altura = float(input("Qual a sua altura? m"))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"Seu IMC é de {round(imc, 1)}. Você está abaixo do peso ideal!")
elif 18.5 < imc < 25:
    print(f"Seu IMC é de {round(imc, 1)}. Você está no peso ideal!")
elif 25 < imc < 30:
    print(f"Seu IMC é de {round(imc, 1)}. Você está com sobrepeso")
elif 30 < imc < 40:
    print(f"Seu IMC é de {round(imc, 1)}. Você está com obesidade!")
elif imc > 40:
    print(f"Seu IMC é de {round(imc, 1)}. Você está com obesidade mórbida, cuidado!")
"""

"""
    SIMULADOR DE LOJAS
print("==" * 10, "LOJAS GUILHERME", "==" * 10)
pr = float(input("QUAL FOI O VALOR DA COMPRA? R$"))
print(f"[0] - À VISTA DINHEIRO/CHEQUE\n"      
      f"[1] - À VISTA CARTÃO\n"
      f"[2] - 2x NO CARTÃO\n"
      f"[3] - 3x OU MAIS NO CARTÃO")
escolha = int(input("QUAL A FORMA DE PAGAMENTO ESCOLHIDA? "))
if escolha == 0:
    print(f"O VALOR REAJUSTADO DA SUA COMPRA É DE R${round(pr / 100 * 90, 2)}\n"
          f"VOCÊ RECEBEU 10% DE DESCONTO DEVIDO A SUA ESCOLHA DE PAGAMENTO")
elif escolha == 1:
    print(f"O VALOR REAJUSTADO DA SUA COMPRA É DE R${round(pr / 100 * 95,2)}\n"
          f"VOCÊ RECEBEU 5% DE DESCONTO DEVIDO A SUA ESCOLHA DE PAGAMENTO")
elif escolha == 2:
    print(f"O PREÇO DA SUA COMPRA CONTINUARÁ SENDO DE R${pr} POIS NÃO HOUVE NENHUM REAJUSTE.")
elif escolha == 3:
    parcela = int(input("DESEJA PAGAR EM QUANTAS PARCELAS? "))
    juro = pr / 100 * 120
    parcelamento = juro / parcela
    print(f"O PREÇO COM 20% DE AUMENTO DA SUA COMPRA É DE {round(juro, 2)}\n"
          f"PARCELADO EM {parcela}x DE R${round(parcelamento, 2)}")
"""

"""
    PEDRA, PAPEL OU TESOURA
print("==" * 10)
print("SUAS ESCOLHAS:")
print("[0] - PEDRA\n"
      "[1] - PAPEL\n"
      "[2] - TESOURA")
print(("==" * 10))
jogador = int(input("Qual a sua jogada? "))
itens = ("PEDRA", "PAPEL", "TESOURA")
comp = random.randint(0, 2)
computador = intens[comp]
print("\033[33mPEDRA\033[m")
sleep(1)
print("\033[36mPAPEL\033[m")
sleep(1)
print("\033[32mTESOURA\033[m")
sleep(1)
print("\033[31m...\033[m")
sleep(2)
if jogador == 0:
    if computador == "PEDRA":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"EMPATE")
        print(("==" * 10))
    elif computador == "PAPEL":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"VITÓRIA DO COMPUTADOR")
        print(("==" * 10))
    elif computador == "TESOURA":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"VITÓRIA DO JOGADOR")
        print(("==" * 10))
elif jogador == 1:
    if computador == "PEDRA":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"VITÓRIA DO JOGADOR")
        print(("==" * 10))
    elif computador == "PAPEL":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"EMPATE")
        print(("==" * 10))
    elif computador == "TESOURA":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"VITÓRIA DO COMPUTADOR")
        print(("==" * 10))
elif jogador == 2:
    if computador == "PEDRA":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"VITÓRIA DO COMPUTADOR")
        print(("==" * 10))
    elif computador == "PAPEL":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"VITÓRIA DO JOGADOR")
        print(("==" * 10))
    elif computador == "TESOURA":
        print(("==" * 10))
        print(f"COMPUTADOR ESCOLHEU {computador}\n"
              f"JOGADOR ESCOLHEU {intens[jogador]}\n"
              f"EMPATE")
        print(("==" * 10))
else:
    print("OPÇÃO INEXISTENTE!")
"""

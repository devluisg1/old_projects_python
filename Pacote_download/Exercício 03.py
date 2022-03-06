# from datetime import date
"""
    JOGO DA ADIVINHAÇÃO
import random
from time import sleep
computador = random.randint(0, 5)
jogador = int(input("Em qual número pensei? "))
print("Processando...")
sleep(2)
if jogador == computador:
    print(f"Parabéns você acertou, eu escolhi o número {computador}")
else:
    print(f"Você errou, eu escolhi o número {computador} e não {jogador}")
"""

"""
    RADAR ELETRÔNICO
velocidade = float(input("Qual a velocidade do carro? "))
if velocidade <= 80:
    print("Tudo certo, dirija com cuidado!")
else:
    print(f"Você ultrapssou a velocidade permitida de 80km em {velocidade - 80}km por isso será multado em"
          f" R${((velocidade - 80) * 7)}")
"""

"""
    PAR OU ÍMPAR
num = float(input("Digite um número qualquer: "))
if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
"""

"""
    PREÇO DE VIAGEM
viagem = float(input("Qual a distância da viagem? "))
p = viagem * 0.50 if viagem <= 200 else viagem * 0.45
if viagem <= 200:
    print(f"Você irá pagar R${viagem * 0.50 } por essa viagem")

else:
    print(f"Você irá pagar R${viagem * 0.45 } por essa viagem")
# p = viagem * 0.50 if viagem <= 200 else viagem * 0.45
# print(p)
"""

"""
    ANO BISSEXTO
ano = int(input("Qual o ano quer analisar? "))
atual = date.today().year
if ano == 0:
    ano = atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("É bissexto!")
else:
    print("Não é bissexto!")
"""

"""
    MAIOR E MENOR NÚMERO
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
maior = a
menor = b
if b > a:
    maior = b
if c > a:
    maior = c
if a < b:
    menor = a
if c < b:
    menor = c
print(f"O maior número é {maior} e o menor número é {menor}")
"""

"""
    AUMENTO DE SALÁRIO
sal = float(input("Qual o seu salário? "))
if sal <= 1250:
    print(f"Seu salário recebeu o aumento de 15% e passou a ser R${(115 / 100) * sal}")
else:
    print(f"Seu salário sofreu um aumento de 10% e passou a ser R${(110 / 100) * sal}")
"""

"""
    Analisador de triângulos
s1 = float(input("Primeiro segmento: "))
s2 = float(input("Segundo segmento: "))
s3 = float(input("Terceiro segmento: "))
if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")
"""

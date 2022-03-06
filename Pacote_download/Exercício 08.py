# from random import randint
"""
    NÚMERO POR EXTENSO
    escolha = " "
while escolha != "S":
    tupla = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ",
             "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
    num = int(input("Digite um número entre 0 e 20: "))
    ran = range(0, 21)
    while num not in ran:
        num = int(input("Valor não suportado!, por favoro digite um número entre 0 e 20: "))
    print(f"{num} em extenso é {tupla[num]}")
    escolha = input("Deseja parar? [S/N]: ").upper()
print("Fim!")
"""

"""
    CAMPEONATO BRASILEIRO
brasileirao = ("FLAMENGO", "SANTOS", "PALMEIRAS", "GRÊMIO", "ATHLETICO-PR", "SÃO PAULO", "INTERNACIONAL", "CORINTHIANS",
               "FORTALEZ", "GOIÁS", "BAHIA", "VASCO", "ATLÉTICO-MG", "FLUMINENSE", "BOTAFOGO", "CEARÁ SC", "CRUZEIRO",
               "CSA", "CHAPECOENSE", "AVAÍ")
print("~~"*40)
print("Os times classificados para a fase de grupos da libertadores são: ")
print(brasileirao[0: 6])
print("~~"*40)
print("Os times rebaixados para a segunda divisão são:")
print(brasileirao[16:])
print("~~"*75)
print("A tabela em ordem alfabética fica:")
print(sorted(brasileirao))
print("~~"*75)
print(f"A CHAPECOENSE ESTÁ NA {brasileirao.index('CHAPECOENSE', 0) + 1}°")
print("~~" * 40)
"""

"""
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
tupla = (n1, n2, n3, n4, n5)
print(tupla)
print(f"A soma dos valores é {sum(tupla)}")
print(f"O menor valor é {min(tupla)}")
print(f"E maior valor é {max(tupla)}")

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(tupla)
print(f"A soma dos valores é {sum(tupla)}")
print(f"O menor valor é {min(tupla)}")
print(f"E maior valor é {max(tupla)}")
"""

"""
    ANÁLISE DE TUPLA
n1 = int(input("DigIte o primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Mais um valor: "))
n4 = int(input("Último valor: "))
pares = 0
tupla = (n1, n2, n3, n4)
print(f"O número nove apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O número 3 apareceu pela primeira vez na {tupla.index(3) + 1}° posição")
else:
    print("O valor 3 não foi digitado")
if n1 % 2 == 0:
    pares += 1
if n2 % 2 == 0:
    pares += 1
if n3 % 2 == 0:
    pares += 1
if n4 % 2 == 0:
    pares += 1
print(f"O total de número pares foi de {pares}")
"""

"""
    LISTAGEM
tupla = (
    ("SAMSUNG ODYSSEY", 3800),
    ("SAMSUNG EXPERT X50", 3000),
    ("LENOVO IDEAPAD 320s", 3200),
    ("INTEL CORE I7 7700hq", 2000),
    ("RAZER BLADE PRO", 22000),
    ("RTX 2080ti", 3000),
    ("EASY PC EXTREME", 4000.50)
)
bra = "TABELA DE PREÇOES"
print("xx" * 20)
print(f"{bra:^40}")
print("xx" * 20)
print(".." * 30)
for c in tupla:
    nome = c[0]
    price = float(c[1])
    print(f"{nome:-<50}", end="")
    print(f"R${price:>8}")
print(".." * 30)
"""

"""
    ANALISADOR DE VOGAL
print(".." * 30)
tupla = ("luis", "guilherme", "alves de carvalho", "programador", "amante", "estudante")
for c in tupla:
    print(f"\nNa palavra {c.upper()} temos  ", end="*")
    for let in c:
        if let in "aeiou":
            print(let, end="*")
    print("\n")
print(".." * 30)
"""

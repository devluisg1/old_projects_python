"""
        Analisador de nome
nome = str(input("Qual o seu nome? ")).strip()
print(f"Seu nome em letras maiúsculas é {nome.upper()}")
print(f"Seu nome em letras minúsculas é {nome.lower()}")
print(f"Seu nome em forma capitalizada é {nome.title()}")
space = nome.count(" ")
print(f"Seu nome tem {len(nome) - space} letras")
pn1 = nome.split()
print(f"O seu primeiro nome tem {len(pn1[0])} letras")
"""

"""
    Separando digitos em um número
        #Forma com string
numero = str(input("Digite um número: "))
print(f"Unidade(s): {numero[3]}")
print(f"Dezena(s): {numero[2]}")
print(f"Centena(s): {numero[1]}")
print(f"Milhar(s): {numero[0]}")
        #Forma matemática
num = int(input("Digite um número: "))
print(f"Este número tem:\n{num // 1 % 10} unidades")
print(f"{num // 10 % 10} dezenas")
print(f"{num // 100 % 10} centenas")
print(f"{num // 1000 % 10} milhares")
"""

"""
    Analisador do primeiro nome da cidade
cidade = str(input("Em que cidade você nasceu? ")).strip().upper()
cidade2 = cidade.split()
print(cidade2[0] == "SANTO")
"""

"""
    Verificador de silva
nome = str(input("Qual o seu nome? ")).upper().strip()
silva = "SILVA" in nome
print(f"Seu nome tem SILVA? {silva}")
"""

"""
        Analisador de "A"
frase = str(input("Digite um frase: ")).upper().strip().replace("Ã", "A").replace("Á", "A")
print(f"A letra 'A' aparece {frase.count('A')} vezes")
print(f"A letra 'A' aparece pela primeira vez na posição {frase.find('A') + 1}")
print(f"E a letra 'A' aparece pela última vez na posição {frase.rfind('A') + 1}")
"""

"""
    Primeiro e Último nome
nome = str(input("Qual o seu nome? ")).upper().strip()
print("Prazer em te conhecer")
pn = nome.split()
print(f"Seu primeiro nome é {pn[0]}")
un = len(pn) - 1
print(f"Seu último nome é {pn[un]}")
"""

"""
Em python todo dado dentro de áspas simples ou duplas é uma string
Entre áspas simples ou duplas triplas
O \n serve para pular para outra linha no python
"""
n = "Luis"
print(dir(n))
print(type(n))
nome = "Luis Guilherme"
print(nome.replace("i", "y"))
print(nome.upper())
print(nome.lower())
print(nome.split())
print(nome.count("e"))
print(nome[0: 6])
print(nome[0:])
print(nome.split()[0])
print(nome[::-1])
print(dir(nome))
print(nome.casefold())
print(nome.partition("i"))
print(nome.isdigit())
print(nome.expandtabs())
print(nome.endswith("e"))
print(len(nome))
nome2 = (input("Digite uma palavra: "))
nome3 = nome2[::-1]
print(nome2, nome3)
if nome2 == nome3:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

"""
tx = "luis"
tx = list(tx)
tx = chr(ord(tx[1]) + 2)
print(tx)

str = "ABBBCD"
index = 1
str = str[:index] + chr(ord(str[index]) + 3) + str[index + 1:]
print(str)

string = input(":")

decode = []

for letter in string:

    decoded = int(ord(letter))

    code = chr(decoded + 3)

    decode.append(code)

print(decode)
"""

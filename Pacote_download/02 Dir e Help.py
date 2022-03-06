"""
Uilitários Python para auxílio na programação
dir - Apresenta todos atributos e funções/métodos para determinado tipo de dados ou variável.

help - Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponíveis para
determinado tipo de dado ou variável.

help("geek".find)

print("geek".count("e"))
"""
num = 4
print("geek".__sizeof__())
print(help("geek".__sizeof__()))

print(num.__sizeof__().__doc__)

test = list("Luis")

print(test)
print(*test)
print(*test, sep="")

nome = "Luis"

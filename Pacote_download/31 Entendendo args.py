    """
Entendendo o *args

# O *args é um parâmetro, como outro qualquer. Isso significa, que você poderá chamar de qualquer
coisa, desde que começe com asterístico.

# Exemplo
*xis

# Mas por convenção da comunidade, utilizamos *args para defini-lo

# Mas oque é o *args?

# O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla (lembre-se que tuplas são imutáveis).

# Simplificando, o parâmetro *args transforma os argumentos passados em tuplas

# Exemplo


def sum_all(a=0, b=0, c=0):
    return a + b + c


print(sum_all(4, 2, 6))
print(sum_all(5, 9))  # TypeError
print(sum_all(8, 9, 7, 8))  # TypeError

# Entendendo o *args


def sum_all(*args):
    print(args)


sum_all(6, 8, 7, 9, 7, 5, 7)
sum_all()
sum_all(9)

def sum_all(*args):
    tot = 0
    for c in args:
        tot += c
    return tot


print(sum_all(7, 9))
print(sum_all(7, 9, 7, 2, 0))

def sum_all(*args):
    return sum(args)


print(sum_all(7, 9, 7, 8))

lista = []


def email(name, sobre, args):
    global lista
    junto = name, sobre
    lista.append(list(junto))
    if args == 123:
        return lista
    return "Senha incorreta"


print(email("Luis Guilherme", "Alves de Carvalho", 123))


def verification(*args):
    if "Luis" in args and "Guilherme" in args:
        return "Oi Luis Guilherme"
    return "Sei nem quem é você"


print(verification("L", 2, "Luis"))
print(verification("Luis", "Guilherme"))
print(verification())

# É bom lembrar que args não fazem algumas funções usando lista, aí será necessário desempacotar
# O desempacotamento altomático acontece quando você coloca um asterístico na frente do argumento
# Usando o * o Python entende que se está paçando uma coleção como argumento e irá ter que desempacotar
# Exemplo

num = list(range(5))


def sum_all(*args):
    return sum(args)


print(sum_all(2, 8, 6))
print(sum_all())
# print(sum_all(num))  # Repare que aqui irá gerar um TypeError
print(sum_all(*num))

def soma(a, b, c):
    return a + b + c


print(soma(1, 2, 3))
lista = [1, 2, 3]
print(soma(*lista))

# Pode desempacotar lista, tuplas e conjuntos
"""



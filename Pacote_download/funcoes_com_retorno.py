import random


def launch_coin():
    if random.randint(0, 2) == 1:
        return "cara"
    else:
        return "coroa"


def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return round(a / b, 2)


def mat(num, num2, fun=soma):
    """Função que usa mais outras 4 funções para realizar operações matemáticas, a é
    o primeiro valor, b é o segundo, no último argumento informe a nome da função
    da respectiva operação que deseja fazer. ESCOLHAS: (soma, sub, mul, div)"""
    return fun(num, num2)

# from mat import (
#    sub,
#    div,
#    mul,
#    soma,
#    mat
# )
'''
Documentando funções com Doocstrings

# É importante documentar o seu código para que você venha a entender no futuro e outras pessoas
# que por ventura o usem também entendam.

def pot(a=2, b=2):
    """
     Função simples que retorna a potência que você escolher do número que você escolher
    :param a: Retorna por padrão 2 caso você não passe nenhum argumento
    :param b: Retorna por padrão 2 caso você não passe nenhum argumento
    :return: Retorna a elevado á b
    """
    return a ** b


print(pot(2, 6))
print(help(pot()))
print(pot.__doc__)

def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mat(num, num2, fun=soma):
    """Função que usa mais outras 4 funções para realizar operações matemáticas, a é
    o primeiro valor, b é o segundo, no último argumento informe a nome da função
    da respectiva operação que deseja fazer. ESCOLHAS: (soma, sub, mul, div)"""
    return fun(num, num2)


print(mat(2, 6, div))
print(mat(2, 2, mul))
print(mat.__doc__)

# Podemos ver a documentação de uma função usando a propriedade .__doc__ ou usando a função help()

def pot(a=2, b=2):
    """
     Função simples que retorna a potência que você escolher do número que você escolher
    :param a: Retorna por padrão 2 caso você não passe nenhum argumento
    :param b: Retorna por padrão 2 caso você não passe nenhum argumento
    :return: Retorna a elevado á b
    """
    return a ** b


print(pot.__doc__)
print(mat.__doc__)
'''




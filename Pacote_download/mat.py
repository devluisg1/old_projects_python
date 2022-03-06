
def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return round(a / b, 2)


def mat(num, num2, fun=soma):
    """
    Função que usa mais outras 4 funções para realizar operações matemáticas, a é
    o primeiro valor, b é o segundo, no último argumento informe a nome da função
    da respectiva operação que deseja fazer.
    :param num: Informe o argumento do primeiro valor que irá fazer parte da operação
    :param num2: Informe o argumento do segundo valor que irá fazer parte da operação
    :param fun: Informe o argumento que representa a função respectiva da operação que deseja fazer.
     ESCOLHAS: (soma, sub, mul, div)
    :return: Retorna a operação escolhida para fazer com a e b
    """
    return fun(num, num2)



matriz = [[], [], []]
for c in range(3):
    for i in range(3):
        num = int(input(f"Digite os número da matriz [{c}/{i}]: "))
        matriz[c].append(num)
print("O determinante da matriz 3 x 3:")
for c in range(3):
    for i in range(3):
        print(f"[{matriz[c][i]:^5}]", end=" ")
    print()

d = (matriz[0][0] * matriz[1][1] * matriz[2][2] +
     matriz[1][0] * matriz[2][1] * matriz[0][2] +
     matriz[2][0] * matriz[0][1] * matriz[1][2] +
     (matriz[0][2] * -1) * (matriz[1][1] * -1) * (matriz[2][0] * -1) +
     (matriz[1][2] * -1) * (matriz[2][1] * -1) * (matriz[0][0] * -1) +
     (matriz[2][2] * -1) * (matriz[0][1] * -1) * (matriz[1][0] * -1)
     )

print(f"É igual à: {d}")




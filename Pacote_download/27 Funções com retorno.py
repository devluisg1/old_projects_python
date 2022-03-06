"""
Funções com retorno

Exemplo de função com retor e sem retorno
numeros = [1, 2, 3]
print(numeros)
ret = numeros.pop()
print(ret)
retpr = print(numeros)
print(retpr)

# Exemplo de função sem retorno:
def quadrado_de_7():
    print(7 * 7)


quadrado_de_7()
ret = quadrado_de_7()
print(ret)

obs: Em python quando tentar ver o retorno de uma função que não retorna nenhum valor,
o resultado é do tipo None

Refatorando a função para que ela retorne o valor:

def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(ret)

# Em python quando você deseja criar uma função com retorno, basta usar a palavra dedicada return

# Não há necessidade de criar uma variável, como foi feito acima, para podermos mostrar o retorno de função
Podemos passar a execução da função para outra função, como o print.


def quadrado_de_7():
    return 7 * 7


print('retorno')
print(quadrado_de_7())
print(quadrado_de_7() + 1)

# Refatorando a 1° Funçaõ


def diz_oi():
    return 'oi'


# Usar função com retorno é melhor para utilizar o dado que essa função está gerando
alguem = str(input("Digite um nome: "))
print(diz_oi(),  alguem + '!')

# 1 - O return finaliza a função
# 1° Exemplo:


def diz_oi():
    return "Oi"
    print("Tô aqui")


print("Diz oi")

# 2 - Podemos em uma função, ter mais de um return, porém somente um será executado de forma principal

vari = True


def var():
    if vari:
        return 'A'
    else:
        return 'B'


nome = "Luis Guilherme Alves de Carvalho"


def carvalho():
    if "Carvalho" in nome:
        return "Aí porra"
    else:
        return "Aqui não"


print(carvalho())

# 3 - Podemos em uma função retornar qualquer tipo de dados e até mesmo múltiplos valores
def other():
    return 2, 3, 4, 8


num1, num2, num3, num4 = other()  # Aqui é um desempacotamento
print(num1, num2, num3, num4)
print(other())

coin = random.randint(0, 2)


def launch_coin():
    if coin == 1:
        return "cara"
    else:
        return "coroa"


print(launch_coin())


from funcoes_com_retorno import launch_coin
print(launch_coin())

# É comum fazer codificações desnecessárias ao fazer funções, como no exemplo a seguir
while True:
    num = int(input(": "))

# Jeito desnecessário
    def i_p():
        if num % 2 == 0:
            return "Par"
        else:
            return "Ímpar"


# Melhor Jeito
def i_p():
        if num % 2 == 0:
            return "Par"
        return "Ímpar"


    print(f"{num} é {i_p()}")
"""

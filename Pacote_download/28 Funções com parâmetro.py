"""
Funções com Parâmetro (de entrada)

# Funções que recebem dados para serem processado dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> Processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
# Não possuem entrada;
# Não possuem saída;
# Possuem entrada mas não saída
# Possuem saída mas não possuem entrada
# Possuem entrada e saída


# Função
def quadrado_de_7():
    return 7 * 7


print(quadrado_de_7())


# Função refatorada
def quadrado(num):
    return num * num


print(quadrado(10))


def cantar_parabens(nome):
    print('Parabéns pra tu', nome)


cantar_parabens("Luis Guilherme")


# Funções podem ter inúmeros parâmetros, todos eles serão separados pro ","
# Função refatorada com uma melhora
def potencia(num, pot):
    return num ** pot


while True:
    base = int(input("Base: "))
    expoente = int(input("Expoente: "))
    print(potencia(base, expoente))
    escolha = str(input("Quer continuar? [S/N]: ")).upper()
    if escolha == "N":
        break


def repetition_word(a, b, msg):
    return (a + b) * msg


print(repetition_word(4, 2, "Guilherme "))


# Quando você está fazendo uma função oque se coloca dentro dos parênteses se chama parâmetro,
quando você está executando uma função oque se coloca dentro dos parênteses se cham argumento.

# TypeError em argumentos errados em funções
def potencia(num, pot):
    return num ** pot


print(potencia(4, 2, 7))
# Irá gerar um TypeError pois a função espera que você passe dois agumentos e você passou 3


def repetition_word(a, b, msg):
    return (a + b) * msg


print(repetition_word(5, 9))
# Irá gegar um TypeError pois a função espera que você passe 3 argumentos e você só passou 2


# Sempre que for fazer uma função nomeie parâmetros de forma que haja um bom entendimento
de outra pessoa que venha ler seu código ou usar a sua função

# A ordem dos parâmetros importa
# Sempre use argumentos na ordem que os parâmetros foram nomeados

# A exceção é quando se usa argumentos nomiados (Keywords Arguments)
# Quando estes são utilizados, a ordem de argumentos em relação a parâmetros não importa
# Exemplo:


def potencia(bas, exp):
    return bas ** exp


print(potencia(bas=4, exp=9))
print(potencia(exp=8, bas=4))
print(potencia(exp=9, bas=4))
print(potencia(bas=4, exp=8))


def sum_par(num):
    total = 0
    for c in range(num + 1):
        if c % 2 == 0:
            total += c
    return total


print(sum_par(7))


def sum_impar(num):
    total = 0
    for c in range(num + 1):
        if c % 2 != 0:
            total += c
    return total


print(sum_impar(7))

# Nunca esqueça que o return finaliza a função

lista = []


def keep(nome, peso):
    lista.append(nome)
    return peso


print("Luis", 65)

def dobra(lst):
    for c in range(len(lst)):
        lst[c] *= 2


lista = [4, 8, 9, 7]
dobra(lista)
print(lista)
"""

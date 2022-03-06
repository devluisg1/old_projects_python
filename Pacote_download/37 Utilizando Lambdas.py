"""
Utilizando Lambdas

- Expressões Lambdas ou expressões lambdas, são funções sem nome, ou seja, funções anônimas .

# Funções em Python


def qualquer_coisa(x):
    return x * 5 / 2 + 5


print(qualquer_coisa(8))

# Expressõa Lambda

expressao = lambda x: x * 5 / 2 + 5

# Podemos ter expressões Lambdas com múltiplas entradas

complete_name = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(complete_name("luis GUIherme", "Alves de carvalho"))


# Em funções Python podemos ter nenhuma ou várias entradas. Em Lambdas também

amar = lambda: "Como não amar Python"
uma = lambda x: x + 4 * 2
duas = lambda x, y: x * y * 2
tres = lambda x, y, z: round((x + y + z) * (x / y / z), 2)
print(amar)
print(uma(1))
print(duas(3, 8))
print(tres(4, 7, 9))

# Caso passemos mais parâmetros do que o esperado, um Type-Error Será gerado.

autores = ["Adam Smith", "J. M. Kennys", "Nicolau Maquiavel"]
autores.sort(key=lambda sombrenome: sombrenome.split(" ")[- 1].upper())
print(autores)

autores = ["Adam Smith", "J. M. Kennys", "Nicolau Maquiavel"]
for c in autores:
    print(c.split(" ")[- 1])

# Função Quadrática
# f(x) = ax² + bx + c

def saquare_function_generator(a, b, c):
    '''Recebe 3 parâmetros (a, b, c) e retorna uma função quadrática
       e seu resultado'''
    return lambda x: a * x ** 2 + b * x + c


print(saquare_function_generator(7, 8, 9)(5))

# Lambdas são usadas principalmente na filtragem e ordenamento de dados, porém não se
# restringem a isso quando se entende elas.
"""




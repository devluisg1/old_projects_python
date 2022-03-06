"""
Módulo Collections - Named Tuple

https://docs.python.org/pt-br/3/library/collections.html#collections.namedtuple

Recaptulando tupla

tupla = (1, 2, 3)
print(tupla[1])

# Named Tuple -- São tuplas diferenciadas, onde especificamos um nome para a mesama e também parâmetros

# Para usar estas Named Tuple precisa-se fazer o seu import

# Existem três formas de declarar elementos em Named Tuple


# 1° Forma - declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raça nome')
# 2° Forma - declaraçaõ Named Tuple
cachorro2 = namedtuple('cachorro2', 'idade, raça, nome')
# 3° Forma - declaração Named Tuple
cachorro3 = namedtuple('cachorro3', ['idade', 'raça', 'nome'])
ray = cachorro3(idade=2, raça='Dog Alemão', nome='Bruce Wane') # Aconselho a forma 3
print(ray)

# Existe 2 forma de acessar elemento em uma Named Tupla, usando o índice ou o nome do elemento

# 1° Forma
print(ray[0])
print(ray[1])
print(ray[2])

# 2° Forma
print(ray.idade)
print(ray.raça)
print(ray.nome)

# As funções e métodos que funcionam em uma tupla funcionam em uma Named Tuple
"""

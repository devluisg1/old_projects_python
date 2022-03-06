"""
Módulo Collections - Counter (Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Collection como: High Performance Container Datatype

Counter: Recebe um iterável como parâmeto e cria um objeto do tipo Collection Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro, e como valor
valor e quantidade de ocorrências desse elemento

-- Utiliziando o Counter
# Em primeiro lugar temos que importar o counter
from collections import Counter

from collections import Counter

ex 1:

lista = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 45, 45, 66, 43]
counter = Counter(lista)
print(counter)
print(type(counter))

ex 2:

nome = "Luis Guilherme"
print(Counter(nome))

ex 3:

texto = '''
Reconhecimentos
Muitas pessoas trabalharam árdua e longamente neste livro. William Weissbaum,
da Sony, nos proveu de soluções precisas para problemas narrativos, bem como
de conselhos astutos durante todo o processo. O conhecimento de games e a
sagacidade de Marianne Krawczyk foram muito apreciados. Tricia Pasternak foi
a melhor editora de todos os tempos. Raven Van Helsing nos ajudou de maneira
que nem imaginávamos, com o YouTube. Por último, obrigado ao meu agente,
Howard Morhaim, e ao meu intrépido coautor, Matthew Stover, por me dar a
chance de ajudar em um projeto tão grandioso.
Robert E. Vardeman
'''
counter = Counter(texto)
print(counter)
print("==" * 15)
palavras = texto.split()
counter = Counter(palavras)
print(counter)
print(counter.most_common(5))

# O Counter pode ser usado em qualquer iterável, em strings, em lista, tuplas, dicionários e conjuntos
ranges e etc.

# O Counter pega um valor de um interável, e o transforma em chave e a ocorrência desse elemento vira valor

# Pode-se encontrar as chaves com mais ocorrência em um Counter usando o comando most_common()
"""

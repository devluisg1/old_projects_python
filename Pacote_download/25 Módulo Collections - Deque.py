"""
Módulo Collections - Deque

https://docs.python.org/pt-br/3/library/collections.html#collections.deque

# Podemos dizer que o deque  é uma lista de alta performance.

# Para ser utilizade precisamos fazer seu import


from collections import deque

# Criando deques
deq = deque("Luis")
print(deq)

# A grande diferença de um deque para uma lista normal, é que com o deque você pode manipular
a ponta esquerda e a direita da lista

# Todas as funções e métodos que funcionam listas, funcionam em deques

# Adicionando elementos no deque
deq.append("$")
print(deq)
deq.appendleft('%')  # Adiciona no começo da lista
print(deq)
# Removendo elementos no deque
print(deq.pop())
print(deq)
print(deq.popleft())  # Remove no começo da lista
print(deq)
"""

"""
Listas Aninhadas

- Algumas lingauagens de programações (C/jAVA) possuem uma estrutura de dados chamados de arrays:

    # Unidimensionais (Arrays/vetores);
    # Multidimensionais (Matrizes);
Em Pyton nós teemos às listas

things = [1, 8, 'n', True]

# Exemplos

matriz = [[], [], []]
for c in range(3):
    for i in range(3):
        matriz[c].append(i)
print(matriz)

listas = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

for lista in listas:
    for num in lista:
        print(num)

[[print(valor) for valor in lista] for lista in listas]
"""

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

velha = [["X" if numero % 2 == 0 else "O" for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

print([["*" for i in range(1, 4)] for j in range(1, 4)])

"""
É necessário conhecer o loop for para trabalhar com ranges
É necessário conhecer melhor os ranges para trabalhar melhor com loops for

ranges criamm sequências de forma ordenada
"""

for c in range(11):
    print(c)

for c in range(5, 56, 5):
    print(c)

for c in range(10, 0, - 1):
    print(c)

for c in range(11):
    print("*==--==--==*" * c)

print(sum(range(11)))

lista = list(range(10))
print(lista)

lista = tuple(range(10))
print(lista)

"""
Conjuntos

Conjunto em qualquer linguagem de programação faz referência a teoria dos conjuntos
da matemática

- No python, os conjuntos são chamados de sets

# Sets (conjuntos) não possuem valores duplicados
# Sets (conjuntos) não possuem valores ordenados
# Elementos não são acessados via índice, ou seja, conjunto não são indexados:

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com
chaves, valores e items duplicados

Os conjuntos (sets) são representados por {}

Diferença entre conjuntos e dicionários

# Os dicionários tem chave/valor
# Os conjuntos tema apenas valor

Definindo um conjunto

# 1° Forma
s = {1, 2, 6, 8, 4}
print(s)
print(type(s))
a = set({1, 2, 6, 8, 4, 1, 2, 6, 8, 4})
print(s)
print(type(s))


# 2° Forma
s = {1, 2, 6, 8, 4, 1, 2, 6, 8, 4}
print(s)
print(type(s))
- Ao criar um conjunto, caso adicionar um valor já existente, o programa não irá gerar um erro
porém não adicionará o valor novamente e o ignorará.

# Pode-se usar sets(conjuntos) em strings
nome = "Luis Guilherme"
nome = set(nome)
print(nome)

- Quando o valor for mostrado na tela, ele será mostrado de modo randômico

# É possível fazer conjuntos com listas e tuplas, o pragrama irá mostrar o programa em forma de conjuntos
e sem valores repetidos casa haja algum

lista = [1, 4, 5, 8, 4, 7, 5, 1, 4]
tupla = (1, 2, 3, 4, 4, 5, 5, 1)
print(set(lista))
print(set(tupla))

# É possível verificar se há valores em conjuntos usando if e in
ex:
if 3 in conjunto:
    print("Tem 3")
else:
    print("Não tem 3")

# Listas e tuplas aceitam valores duplicados, dicionário não aceitam chaves duplicadas
e conjuntos não aceitam valores duplicados

lista = [1, 4, 5, 8, 4, 7, 5, 1, 4]
tupla = (1, 4, 5, 8, 4, 7, 5, 1, 4)
print(lista)
print(tupla)
dicionario = {}.fromkeys(lista, "dict")
print(dicionario)
conjunto = {1, 4, 5, 8, 4, 7, 5, 1, 4}
print(conjunto)

# É possível usar qualquer tipo de dados em sets(conjuntos) assim como em todas
as outras coleções

# É possível iterar sobre conjuntos em python usando for
conjunto = {4, 3, 'a', 9, 4, 5, 'v', True, 'a'}
for c in conjunto:
    print(c)
for c, i in enumerate(conjunto):
    print(c, i)

Imagine que fizamos um formulário de cadastro de visitantes em uma feira ou um museu
e os visitantes informam manualmente a cidade de onde vieram
Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adiciojar novos elementos
E ter repetição

cidade = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidade)
print(len(cidade))

Agora precisamos saber quantas pessoas de cidades dististas vieram para o museu/feira 
Neste caso, recomenda-se usar sets(conjuntos)

# É possivel adicionar valor em um conjunto usando o add(), deixando assim claro que conjuntos são mutáveis

s = {1, 2, 3}
print(s)
s.add(4)

# Caso tentar adicionar um valor já existente o programa não irá gerar um erro, mas irá ignorar o valor

print(s)
s.add(4)

# 1° Forma
Use .remove() para remover um valor de um conjunto, caso tente remover um valor inexistente, ele irá gerar key error
E para remover, como o conjunto não é indexado, indique o valor e não o índice, pois índice não existe em conjuntos
E também não retorna nenhum valor

s = {1, 2, 3}
print(s)
s.remove(2)
print(s)

# 2° Forma
Use .discard() para remover items de um conjunto, a maior difirença para o remove() é que o discard
não gera erro quando se tenta remover um valor inexistente

s = {1, 2, 3}
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
s.discard(1)
print(s)
s.discard(1)
print(s)

# Pode-se copiar um conjunto usando Deep copy e Shallow copy
s = {1, 2, 3}
novo = s.copy()
novo.add(4)
print(s)
print(novo)

s = {1, 2, 3}
novo = s
s.remove(2)
print(s)
print(novo)
s.add(2)
print(s)
print(novo)

# Pode-se remover todos os valores de um conjunto usando o clear
s = {1, 2, 3}
s.clear()
print(s)

# 1° Forma
Para juntar conjuntos usa-se o union(), union é um recurso matemático, a união de dois conjuntos

est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
uni = est_java.union(est_python)
print(uni)
est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
uni = est_python.union(est_java)
print(uni)

# 2° Forma
Pode-se também juntar conjuntos usando o caractere pipe: |

est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
uni = est_java | est_python
print(uni)

# 1° Forma
Pode-se ver a intersecção de conjuntos usando o intersection()

est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
intersec = est_python.intersection(est_java)
print(intersec)

# 2° Forma
Pode-se ver também a intersecção usando o caractere de e comercial: &

est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
intersec = est_python.intersection(est_java)
print(intersec)

est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
intersec = est_python & est_java
print(intersec)

# Pode-se ver a diferença de dois conjuntos usando o difference

est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
est_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}
diference = est_python.difference(est_java)
print(diference)


s = {1, 2, 3, 4, 5, 6, 7}
print(sum(s))
print(min(s))
print(max(s))
print(len(s))
est_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
print(est_python.issuperset('PEdro'))
"""

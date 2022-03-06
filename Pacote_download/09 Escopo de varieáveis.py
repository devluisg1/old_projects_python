"""
Casos de escopo
 1 - Variáveis globais;
    - Escopo rechonhecido em todo o programa

    nome = "Luis"
    print(numero)

 2 - Variáveis locais;
    - Escopo reconhecido apenas no bloco que foi declarada

    num = 42
    if num >= 15:
     novo = num + 20
    print(novo)

Python tem tipagem de variável dinâmica, ou seja, não é necessário declarar que tipo de dado será a variável
No Python é possível fazer reatribuição de variável

numero = 42
print(numero)
print(type(numero))

numero = "Luis"
print(numero)
print(type(numero))

def r():
    x = 8
    print(n)
    print(x)


n = 2

r()
print(x) # Dá erro
"""

"""
Funções com parâmetro padrão (Defaut Parameter)
# Funções onde a entrada de parâmetros seja opcional;
# Por exemplo a função print()

# Exemplo de função com argumento obrigatório
def sqr(num):
    return num ** 2


print(sqr(2))
print(sqr())
# A falta de argumento neste caso gera um TypeError

# Mais um exemplo de função onde a passagem de parâmetro seja opcional
# Usar o = e o parâmetro padrão, torna esse parâmetro opcional
# Pode-se usar o parâmetro padrão em qualquer parâmetro da função com a condição que os parâmetro padrões estejam
# SEMPRE depois dos parâmetros que não são padrão
# Se o usuário não adcionar nenhum argumento que foi colocado no padrão, ele executará o parâmetro padrão
# Caso o usuário adicione outro argumento a função, o parâmetro padrão é descartada na execução

def expo(numero, pote=2):
    return numero ** pote


print(expo(4, 2))
print(expo(5))
print(expo(6, 8))
print(expo(2))
print(expo(6, 2))


def expo(numero=2, pote=2):
    return numero ** pote


print(expo())
print(expo(3))
print(expo(4, 5))


def soma(a=0, b=0):
    return a + b


print(soma())
print(soma(2))
print(soma(8, 9))


def show_informatio(nome="Luis", dev=False):
    if nome == "Luis" and dev is True:
        return "Bem-Vindo programador Luis"
    elif nome == "Luis":
        return "Eu pensei que você era programador"
    return f"Olá {nome}"


print(show_informatio("Luis"))
print(show_informatio("Carlos"))
print(show_informatio("Luis"))


# Benefícios de usar parâmetros padrão
# Nos permite ser mais flexiveis nas funções;
# Evitar erros por falta de argumentos
# Evita erros com parâmetros incorretos;
# Nos permite trabalhar com exemplos mais legíveis de código

# Podemos utilizar qualquer tipo de dados como parâmetros padrões, até outras funções


def soma(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mat(num, num2, fun=soma):
    return fun(num, num2)


print(mat(2, 4, soma))
print(mat(2, 4, sub))
print(mat(2, 4, div))
print(mat(2, 4, mul))

# É necessário tomar cuidado com o escopo de variávei
# Caso utilize duas varáveis de mesmo nome, uma global e uma local respectivamente.
# No Python, a variável local se sobrepõe a global
# ex:

nome = "Luis"  # Variável global


def oi():
    nome = "Luis"  # Variável local
    return f"Oi {nome}"


print(oi())

# Atenção com variáveis locais e globais, UnboundLocalError é o erro de quando a variável local está sendo usada
# Para processamento sem ser inicioalizada.

# Porém pode-se resolver isso usando a palavra reservada global, que índica que você deseja usar a varável global
nome = "Luis"  # Variável global


def oi():
    global nome

    nome = "Luis"  # Variável local
    return f"Oi {nome}"


# Podemos ter funções dentro de funções, e também tem uma forma especial de escopo de variável
# Prática não comum


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador
    return dentro()


print(fora())
"""

"""
Entendendo **kwargs

# Poderia ser:
**xis

# Mas por convenção da comunidade ficou como:
**kwargs

# Este é só mais um parâmetro, mas diferentemente de *args que coloca os valores em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esse parâmetros em um dicionário


def favorit_calors(**kwargs):
    print(type(kwargs))
    return kwargs


print(favorit_calors(luis="Verde", guilherme="Azul"))


# Exemplo


def favorit_calors(**kwargs):
    for k, v in kwargs.items():
        print(f"A cor favorita de {k.title()} é {v}")


favorit_calors(luis="Verde", guilherme="Azul", alves="Amarelo")


# É sempre bom lembrar que os parâmetros *args e **kwargs não são obrigatórios


# 2° Exemplo


def comprimeto_especial(**kwargs):
    if "luis" in kwargs and kwargs["luis"] == "Guilherme":
        return f"Fala, Luis Guilherme meu chapa"
    elif "luis" in kwargs:
        return f"Olá {kwargs['luis']}"
    return "Não sei quem vc é"


print(comprimeto_especial())
print(comprimeto_especial(luis="Guilherme"))
print(comprimeto_especial(luis="Python"))
print(comprimeto_especial(carlos="Magno"))

# Nas nossas funções podemos ter:

# Parâmetros obrigatórios;
# *agrs;
# Parâmetros defaul (não obrigatórios);
# **kwars
# Todos tem que estar nesta ordem aqui representada

def my_function(idade, nome, *args, solteiro=False, **kwargs):
    print(f"O {nome} tem {idade} anos")
    print(args)
    if solteiro is False:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)


my_function(17, "Luis")
print()
my_function(17, "Carlos", 9, 7, 2, solteiro=True, cs="Go", dev="Python")
print()
my_function(17, "Luis", 9, 7, 2, solteiro=False)

# Entendendo porque é importante manter a ordem dos parâmetros da declaração


# Função com a ordem correta de parâmetros
def show_all(a, b, *args, c="Luis", **kwargs):
    return [a, b, args, c, kwargs]


print(show_all(1, 2, 3, c="Guilherme", sobrenome="Alves", sobrenome2="Carvalho"))


# Função com a ordem incorreta de parâmetros
def show_all(a, b, c="Luis", *args, **kwargs):
    return [a, b, args, c, kwargs]


print(show_all(1, 2, 3, sobrenome="Alves", sobrenome2="Carvalho"))


def mostrar_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': "Luis", 'sobrenome': "Carvalho"}
print(mostrar_nome(**nomes))



def soma(a, b, c):
    return a + b + c


print(soma(1, 2, 3))
lista = [1, 2, 3]
tupla = (1, 2, 3)
dicionario = {"a": 1, "b": 2, "c": 3}
conjunto = {1, 2, 3}
print(soma(*lista))
print(soma(*tupla))
print(soma(*conjunto))
print(soma(**dicionario))

# Os nomes da chaves em um dicionário devem ser os mesmos dos parâmetros da função

dicionario = {"e": 1, "b": 2, "c": 3}


def soma(a, b, c):
    return a + b + c


print(soma(**dicionario))  # Irá gerar erro


dicionario = {"a": 1, "b": 2, "c": 3, "luis": "Guilherme"}


def soma(a, b, c, **kwargs):
    return a + b + c


print(soma(**dicionario, nome="Luis"))

"""

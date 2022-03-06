"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python

A ideia de PEp8 é que possamos escrever códigos de forma Pythonica.

[1] - Utilize Camel Case para nomes de classes:

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilizae nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 3

[3] -  Ultilize 4 espaços para identação: (Use o Tab apenas se o mesmo for configurado para 4 espaços)

if "a" in "banana":
    print("Tem")

[4] -  Linhas em branco
-Separar funções e definições de classe com duas linhas em duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports

-Imports devem ser sempre feitos em linhas separadas;

#Maneiras corretas de fazer imports;

import math
import os

from math import sqrt, acos, tanf

#Caso haja muitos imports de um mesmo pacote, recomenda-se fazer:

from math import (
    sqrt,
    cos,
    pow,
    radians,
    log
)

# imports devem ser colocados no topo do arquivo, logo depois de qualer comentário ou docstrings e antes de
constantes ou variáveis globais.

[6] - Não faça espaços desnecessário em expressões e instruções:

funcao(algo[1]), {outro: 2})

dict["chave"] = lista[indice]

[7] - Termine sempre uma instruçõo com uma nova linha
"""





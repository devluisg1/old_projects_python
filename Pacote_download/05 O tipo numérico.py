"""
* SÍMBOLO DE MULTIPLICAÇÃO
+ SÍMBOLO DE ADIÇÃO
- SÍMBOLO DE SUBTRAÇÃO
/ SÍMBOLO DE DIVISÃO
// SÍMBOLO DE DIVISÃO INTEIRA
% SÍMBOLO DE RESTO DE DIVISÃO
** SÍMBOLO DE POTENCIA
** (1/2) FORMA DE RADICIAÇÃO QUADRÁTICA
** (1/3) FORMA DE RADICIAÇÃO CÚBICA
"""
import math
import random

num = 42
num += 1
print(num)
print(type(num))
num = 5
print(dir(num))
print(num.__pow__(0))
num = 3
num /= 3
print(num.__abs__())
num = 3
num2 = 1
num5 = num + num2
print(num5.bit_length())
print(num.__sizeof__())
print(math.log(num))
print(random.randint(0, 15))

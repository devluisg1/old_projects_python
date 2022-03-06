# from math import sqrt
""""
         Dissecando vairiável
algo = input("Digite algo: ")
print("O tipo primitivo dessa variável é", type(algo))
print("É um número?", algo.isnumeric())
print("É apenas espaços?", algo.isspace())
print("É alphanumeric?", algo.isalnum())
print("É apenas letras?", algo.isalpha())
print("Está maiúscula? ", algo.isupper())
print("Está minúscula?", algo.islower())
print("Está capitalizada?", algo.istitle())
"""

"""
        Antecessor e sucessor
n = int(input("Digite um número por favor: "))
print(f"Analisando {n}, o sucessor dele é {n + 1} e o antecessor {n - 1}")
"""

"""
        Analisador
n = int(input("Digite um número:"))
print(f"Analisando {n}, pode-se afirmar que seu dobro é {n * 2} \nSeu triplo é {n * 3} "
      f"sua raiz quadrada é {sqrt(n)} e sua raiz cúbica é {n ** (1/3)}")
"""

"""
        Média de aritmética
n1 = float(input("Digite aqui sua primeira nota: "))
n2 = float(input("Digite aqui a segunda nota: "))
print(f"A soma de suas notas foi {n1 + n2} e sua média foi {(n1 + n2) / 2}")

"""

"""
        Conversor de medidas
m = float(input("Digite aqui uma medida em metros para efetuarmos uma conversão: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f"Convertendo {m}m para km obtemos {km}km, para mm obtemos {hm}hm, \nPara Dam obtemos {dam}"
      f"dam, para dm obtermos {dm}dm,"
      f"para cm obtemos {cm}cm e para mm obtemos {mm}mm")
"""

"""
        Tabuada
n = float(input("Digite um número para você a tabuada de adição, subtração, multiplicação, divisão: "))
for c in range(1, 11):
    print(f"\033[31m{n} + {c} = {n + c :}\033[m"
          f"\033[33m  {n} - {c} = {n - c}\033[m"
          f"\033[35m  {n} * {c} = {n * c}\033[m"
          f"\033[36m  {n} / {c} = {n / c}\033[m")
"""

"""
        Conversor de moedas
n = float(input("Quantos reis você deseja converter: "))
print(f"Convertendo R${n} em dólares, você tem U$D{n * 4.47}")
"""

"""
        Pintando parede
largura = float(input("Qual a largura da sua parede? "))
altura = float(input("Qual a altura da sua parede? "))
print(f"Sua parede tem a dimensão de {largura}X{altura} com área de {altura * largura}m².\n"
      f"Sendo assim sua parede necessitará de {(altura * largura) / 2}L de tinta")
"""

"""
    Calculando desconto
produto = float(input("Qual o valor do produto? R$"))
print(f"O produto que custava R${produto}, com a promoção de 5% vai custar R$ {95 / 100 * produto}")
"""

"""
    Calculando aumento
salario = float(input("Qual é o salário do funcionário? R$"))
print(f"O funcionário que recebia R${salario}, com o aumento de 15% vai passar a receber "
      f"R${115 / 100 * salario :}")
"""

"""
    Conversor de temperatura
escolha = int(input("Se deseja converter Célsius para Fahrenheit digite 0\n"
                    "Se deseja converter Fahrenheit para Célsius digite 1 "))
if escolha == 0:
    c = float(input("Digite aqui uma temperatura em graus Célsius para ser convertida a Fahreheit:"))
    print(f"A conversão de {c}°C é {(c * 9 / 5) + 32}°F: ")
elif escolha == 1:
    f = float(input("Digite aqui uma temperatura em graus Fahreheit para ser convertida a Célsius :"))
    print(f"A conversão de {f}°F é {(f - 32) * 5 / 9}°C ")
"""

"""
    Aluguel de carro
dia = float(input("Por quantos dias usou este carro? "))
km = float(input("Quantos Km percorreu com o carro? "))
print(f"De acordo com os dados fornecidos você deverá pagar R${(dia * 60) + (km * 0.15)} por o uso do carro alugado!")
"""

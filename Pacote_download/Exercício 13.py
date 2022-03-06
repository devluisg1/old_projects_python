# import random
# from time import sleep
# import math
"""
    FUNÇÃO PARA VOTANTES E NÃO VOTANTES
def voto(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade >= 18 or idade >= 65:
        print(f"A pessoa com {idade} anos tem o voto obrigatório")
    elif 16 <= idade < 18:
        print(f"A pessoa com {idade} anos tem o voto opcional")
    else:
        print(f"Com {idade} anos ainda não vora")


print("=" * 80)
print(f"{'Vamos analisar a sua situação de votante':^80}")
print("=" * 80)

ida = int(input("Em que ano você nasceu? "))
voto(ida)
"""

'''
    FUNÇÃO FATORIAL
    
def fatorial(n, show=True):
    """
    Uma função que retorna o fatorial de um número mostrando
    ou não o cálculo
    :param n: Número que deseja fazer o fatorial
    :param show: Escolha de mostrar ou não o cálculo, não escreva nada para mostrar
    -------e escreva False para não mostrar
    :return: O resultado do fatorial de n
    """
    r = 1
    for c in range(n, 0, -1):
        r *= c
        if show:
            print(c, "x" if c > 1 else "=", end=" ")
    return r


print(fatorial(5, False))
print(help(fatorial))
print(fatorial(10))
'''

"""
    FICHA DE JOGADOR
def jogador(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gols")


no = input("Nome do jogador: ")
gol = input("Gols: ")
# if len(no) != 0 and gol.isnumeric() and len(gol) != 0:
#    jogador(nome=no, gols=gol)
# elif len(no) == 0 and gol.isnumeric() and len(gol) != 0:
#    jogador(gols=gol)
# elif len(no) != 0 and len(gol) == 0 or gol.isalpha():
#    jogador(nome=no)
# else:
#    jogador()
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if len(no) == 0:
    jogador(gols=gol)
else:
    jogador(no, gol)
"""

"""
    INPUT ESPECIAL
def leiaint(msg):
    ok = 0
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = 1
        else:
            print("\033[31mValor inválido, tente novamente!\033[m")
        if ok == 1:
            return valor


nome = leiaint("Digite um número: ")
print(nome)
"""

"""
def notas(*args, se=False):
    '''
    --- Uma função que retorna: O total de notas adicionadas, a maior nota,
    a menor nota, a média e a situação se for solicitado.
    :param args: Notas dos alunos/turma (Adicione quantas desejar)
    :param se: Situação da turma/aluno (Opicional)
    :return: Um dicionário com as informações solicitadas
    '''
    maior = max(args)
    menor = min(args)
    total = len(args)
    media = round(sum(args) / total, 2)
    dicio = {"Total": total, "Maior": maior, "Menor": menor, "Média": media}
    if se is True:
        if media <= 6:
            dicio.update({"Situação": "Ruim"})
        elif media >= 7:
            dicio.update({"Situação": "Boa"})
        else:
            dicio.update({"Situação": "Razoável"})
    return dicio


print(notas(7, 5, 9, 2, se=True))
help(notas)
"""

'''
cores = ("\033[m",  # 0 - SEM COR
         "\033[0;30;41m",  # 1 - VERMELHO
         "\033[0;30;42m",  # 2 - VERDE
         "\033[0;30;43m",  # 3 - AMARELO
         "\033[0;30;44m",  # 4 - AZUL
         "\033[0;30;45m",  # 5 - ROXO
         "\033[7;30m")     # 6 - BRANCO


def ajuda(com):
    titulo(f"ACESSANDO MANUAL PYTHON DO COMANDO \'{escolha}\'", r)
    print(cores[6], end="")
    help(com)
    print(cores[0], end="")


def titulo(msg, cor=0):
    lines = len(msg) + 4
    print(cores[cor], end="")
    print("=" * lines)
    print(f"  {msg}")
    print("=" * lines)
    print(cores[0], end="")


while True:
    r = random.randint(0, 6)
    titulo("SISTEMA DE AJUDA PY HELP", 2)
    escolha = input("Função/Biblioteca: ")
    if escolha.upper() == "FIM":
        titulo("ATÉ LOGO!", 1)
        break
    sleep(0.5)
    ajuda(escolha)
    sleep(0.5)
'''

sec = 7200
if sec >= 60:
    minu = sec // 60
    sec = sec % 60
    if minu >= 60:
        hora = minu // 60


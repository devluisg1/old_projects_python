# from time import sleep
# from random import randint

"""
    FUNÇÃO DE ÁREA
def area(largura, comprimento):
    '''
    Uma função simples que cálcula a área de figura retângular
    :param largura: Recebe a largura
    :param comprimento: Recebe o comprimento
    :return: Retorna a largura x  altura
    '''
    return f"A área do seu terreno de {largura}X{comprimento} é de {largura * comprimento}"


lar = float(input("Largura: "))
com = float(input("Comprimento: "))
print(area(lar, com))
"""

"""
    PRINT ESPECIAL
def escreva(texto="None"):
    '''
    Uma função de escrevar coisas na tela, como o print
        com a diferença desta ter um ajuste de linhas encima
        e embaixo do texto de acordo com o tamanho deste e sentralizar
        o argumento passado.
        Obs: Se quiser mostrar um tipo numérico que não seja str
        converta-o antes usando a função str()
        :param texto: Escreva oque deseja mostrar na tela
        :return: O argumento texo com linhas encima e ambaixo
    
    '''
    
    print("=" * (len(texto) + 4))
    # print(f"{texto:^{(len(texto) + 4)}}")
    print(f"  {texto}")
    print("=" * (len(texto) + 4))


escreva("Luis Guilherme")
"""

"""
    FUNÇÃO CONT
def linha(a):
    print("==" * a)


def contador(begin, end, step):
    if step < 0:
        step = step * -1
    if step == 0:
        step = 1
    if begin > end:
        step = step * - 1
        end = end - 3
    for c in range(begin, end + 1, step):
        print(f"{c}", end=" -> ")
        sleep(0.5)
    print("Fim")


#    if step < 0:
#        step = step * -1
#    if begin > end:
#        c = begin
#        while c >= end:
#            print(f"{c}", end=" -> ")
#            sleep(0.5)
#            c -= step
#        print("Fim")
#    c = begin
#    while c <= end:
#        print(f"{c}", end=" -> ")
#        sleep(0.5)
#        c += step
#    print("Fim")
linha(30)
print("Contagem de 1 até 10 de 1 em 1")
contador(1, 10, 1)
linha(30)
print("Contagem de 10 até 0 de 2 em 2")
contador(20, 2, 2)
linha(30)
print("Agora personalize a contagem...")
linha(30)
inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
linha(30)
"""

"""
    FUNÇÃO MAIOR 
def lista_random(ll, fvl, svl):
    lista = []
    while len(lista) != ll:
        r = randint(fvl, svl)
        if r not in lista:
            lista.append(r)
    return lista


def maior(*args):
    #   m = 0
    for c in args:
        print(f"{c}", end=" ")
        # 2° Forma
        #        if c > m:
        #            m = c
        # 3° Fornma
        #        if c == 0:
        #            m = c
        #        else:
        #            if c > m:
        #                m = c
        sleep(0.5)
    print(f"\nExistem {len(args)} valor(es)")
    print(f"O maior valor foi {max(args)}")
#   print(f"O maior valor foi {m}")


maior(*lista_random(6, 1, 100))
maior(8, 9, 7, 9, 5, 7,  6, 7)
"""

"""
    FUNÇÃO SOMA PARES DA LISTA
def lista_random(ll, fvl, svl):
    lista = []
    while len(lista) != ll:
        r = randint(fvl, svl)
        if r not in lista:
            lista.append(r)
    return lista


def sum_par(*args):
    par = 0
    for c in args:
        if c % 2 == 0:
            par += c
        print(f"{c}", end=" ")
        sleep(0.5)
    print(f"\nLista: {list(args)}")
    print(f"A soma dos valores pares dessa lista é {par}")


lista = lista_random(10, 1, 100)
sum_par(*lista)
"""

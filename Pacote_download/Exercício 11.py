# from random import randint
# from time import sleep
# from operator import itemgetter
# from datetime import date
"""
    DICIONÁRIO EM PYTHON
dici = {}
nome = str(input("Nome: ")).upper().strip()
n1 = float(input("1° Nota: "))
n2 = float(input("2° Nota: "))
media = (n1 + n2) / 2
dici.update({"nome": nome})
dici["media"] = media
if media >= 7:
    dici.update({"situation": "APROVADO"})
elif 5 > media < 7:
    dici["situation"] = "RECUPERAÇÃO"
elif media < 5:
    dici.update({"situation": "REPROVADO"})
print("==" * 25)
for k, v in dici.items():
    print(f"{'--':>4} {k}: {v}")
print("==" * 25)
# print(f"{'--':>4} Nome: {dici['nome']}")
# print(f"{'--':>4} Média: {dici['media']}")
# print(f"{'--':>4} SITUÇÃO: {dici.get('situation')}")
"""

"""
    JOGO DE DADOS
jogo = {}
print("==" * 15)
for c in range(1, 5):
    jogo.update({f"jogador{c}": randint(1, 6)})
    print(f"jogador{c} tirou: {jogo.get(f'jogador{c}')}")
    sleep(1)
print("==" * 15)
print(f"{'RANKING':^30}")
print("==" * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for c, i in enumerate(ranking):
    print(f"{c + 1} POSIÇÃO: {i[0]} com {i[1]}")
    sleep(1)
print("==" * 15)
"""

"""
    CARTEIRA DE TRABALHO
dados = {}
nome = str(input("Nome: ")).upper().strip()
dados.update({"nome": nome})
sexo = str(input("Sexo [M/F]: ")).upper()
idade = int(input("ano de nascimeto: "))
dados["idade"] = date.today().year - idade
carteira = int(input("N° da carteira de trabalho: (caso não tenha digite 0)"))
dados.update({"carteira": carteira})
if carteira != 0:
    contr = int(input("Ano de contratação: "))
    dados.update({"contratação": contr})
    salario = float(input("Salário: "))
    dados.update({"Salário": salario})
    if sexo == "M":
        aposent = (date.today().year - idade) + 35
        ano = contr + 35
        dados.update({"Idade de Aposentadoria": aposent})
        dados.update({"Ano de Aposentadoria: ": ano})
    elif sexo == "F":
        aposent = (date.today().year - idade) + 30
        ano = contr + 30
        dados.update({"Idade de Aposentadoria": aposent})
        dados.update({"Ano de Aposentadoria": ano})
for k, v in dados.items():
    print(f"--{'':>2} {k}: {v}")
"""

"""
    CADASTRO DE JOGADOR DE FUTEBOL
jogador = {}
gols = []
nome = str(input("Nome do jogador: ")).capitalize().strip()
jogador.update({"nome": nome})
partidas = int(input(f"Quantos partidos {nome} jogou? "))
jogador.update({'partidas': partidas})
for c in range(1, partidas + 1):
    n = int(input(f"Quanto gols {nome} fez na {c}° partida? "))
    gols.append(n)
jogador.update({"gols": gols})
jogador.update({"total": sum(gols)})
print("==" * 20)
print(jogador)
print("==" * 20)
for k, v in jogador.items():
    print(f"{k}: {v}")
print("==" * 20)
print(f"O jogador {jogador.get('nome')} jogou {jogador['partidas']} partida(s)")
for c in range(1, partidas + 1):
    print(f"{' ':>4} Na {c}° partida, fez {gols[c - 1]} gol(s)")
print(f"Com um total de {jogador.get('total')} gol(s)")
print("==" * 20)
"""

"""
    UNINDO DICIONÁRIO E LISTA
lista = []
media = qntd = 0
maior = femi = a = 0
while True:
    nome = str(input("Nome: "))
    qntd += 1
    sexo = str(input("Sexo: [M/F] ")).upper().strip()
    if sexo not in "FM":
        while sexo not in "FM":
            sexo = str(input("ERRO! Responda apenas com 'F' ou 'M': ")).upper().strip()
    if sexo == "F":
        femi += 1
    idade = int(input("Idade: "))
    dic = {
        f"nome": nome,
        f"sexo": sexo,
        f"idade": idade
    }
    lista.append(dic)
    media = media + idade
    escolha = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if escolha not in "SN":
        while escolha not in "SN":
            escolha = str(input("ERRO! Responda apenas com 'S' ou 'N': "))
    if escolha == "N":
        break
print("==" * 25)
media = media / qntd
print(f"A) Temos o total de {qntd} pessoas cadastradas")
print(f"B) A média de idade é de {round(media, 2)} anos")
if femi > 0:
    print("C) As mulheres cadastradas foram: ", end=" ")
    for c in range(len(lista)):
        if lista[c]['sexo'] == "F":
            print(f"[{lista[c]['nome']}]", end=" ")
else:
    print("C) Inexistente!", end=" ")
for c in range(len(lista)):
    if lista[c]['idade'] > media:
        maior += 1
if maior > 0:
    print(f"\nD) A lista das pessoas com idade acima da média: ")
    for c in range(len(lista)):
        if lista[c]['idade'] > media:
            print(f"   Nome = {lista[c]['nome']}; "
                  f"Sexo = {lista[c]['sexo']}; "
                  f"Idade = {lista[c]['idade']}")
else:
    print("D) Inexistente!")
print("ENCERRADO")
"""

"""
lista = []
gols = []
prtds = []
escolha2 = 0
escolha3 = 0
while escolha3 != "N":
    nome = str(input("Nome do jogador? ")).upper().strip()
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    prtds.append(partidas)
    for c in range(1, partidas + 1):
        n = int(input(f"Quantos gols {nome} fez na {c}° partida: "))
        gols.append(n)
    jogador = {
        'nome': nome,
        'gols': gols.copy(),
        'total': sum(gols)
    }
    lista.append(jogador)
    gols.clear()
    escolha = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if escolha not in "SN":
        while escolha not in "SN":
            escolha = str(input("Erro! Responda com [S/N]: ")).upper()
    if escolha == "N":
        print("==" * 35)
        print(f"{'N° NOME':<23}", end="")
        print(f"{'GOLS':^24}", end="")
        print(f"{' TOTAL':>23}")
        print("==" * 35)
        for i, c in enumerate(lista):
            print(f"{i}  {c['nome']:<19}{str(c['gols']):^28}{c['total']:>20}")
        print("==" * 35)
        while True:
            escolha2 = int(input("Deseja mostrar os dados de qual jogador? [digite 999 parar parar]: "))
            if escolha2 == 999:
                break
            if escolha2 > len(lista) - 1:
                while escolha2 not in range(len(lista)):
                    escolha2 = int(input("NÚMERO DE JOGADOR INEXISTENTE! TENTE DE NOVO: "))
                    if escolha2 == 999:
                        break
            for c in range(len(lista[escolha2]['gols'])):
                print(f"=== No {c + 1}° jogo"
                      f" {lista[escolha2]['nome']} "
                      f"fez {lista[escolha2]['gols'][c]} gols")
    escolha3 = str(input("Deseja adicionar mais jogadores? [S/N]: ")).upper()
    if escolha3 == "N":
        break
"""

"""
While expressão booleano:
    // Execução do loop

O bloco do while será repetido enquanto a expressão for verdadeiro.
Expressão boolenana é aquela que assumi valor de verdadeiro ou falso.

É importante que se cuide do critério de parada de um loop para que não se entre em um loop infinito

resposta = " "
while resposta != "SIM":
    resposta = (str(input("Acabou porra? ")))

num = 0
while num < 10:
    num += 1
    print(num)

nu = 1
while nu < 10:
    print(nu)
    nu += 1

sexo = str(input("Qual o seu sexo? [M/F] ")).upper().strip()
if sexo == "M":
    print("Registrado com sucesso")
elif sexo == "F":
    print("Registrado com sucesso")
else:
    while sexo != "M" or "F":
        sexo = str(input("Dados inválidos, por favor digite seu sexo, informe com [M/F] ")).upper().strip()
        if sexo == "F":
            print("Registrado com sucesso")
            break
        elif sexo == "M":
            print("Registrado com sucesso")
            break

pergunta = input("Deseja parar [S/N]? ").upper()
while pergunta == "S" or "N":
    while pergunta == "N":
        pergunta = str(input("Deseja continuar [S/N]? ")).upper()
    if pergunta == "S":
        print("Programa finalizado!")
        break
    elif pergunta != "S" or "N":
        pergunta = input("Dados errados! Responda com [S/N]: ").upper()

passw = input("Nova senha: ")
passw0 = input("Confirmação da senha: ")
if passw0 != passw:
    while passw0 != passw:
        passw0 = input("Primeira senha não condiz com a segunda, tente denovo: ")
        if passw0 == passw:
            print()
cpf = int(input("CPF: "))
tent = input("Digite sua senha: ")
if tent == passw:
    print("Senha correta!")
else:
    while tent != passw:
        tent = input("Senha icorreta, tente denovo: ")
        if tent == passw:
            print("Senha correta")
            break
"""

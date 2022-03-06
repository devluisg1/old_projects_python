# idade = int(input("Quantos anos voccê tem? "))
# nome = int(input("Qual número? "))
# if idade and nome == 65:
#   print("Aí sim")
ativo = True
logado = False
if ativo and logado:
    print("Bem vindo usuário!")
elif not ativo:
    print("Faça o login em sua conta!")
elif not logado:
    print("FAÇA LOGIN EM SUA CONTA")
print(ativo is True)
nome = input("Qual é seu nome? ").upper()
print("E" in nome)

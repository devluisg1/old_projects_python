"""
Usa-se para sair de loops de forma projetada
"""
"""
for c in range(1, 12):
    if c == 7:
        break
    else:
        print(c)
print("Saí do loop")

while True:
    c = str(input("Digite q para sair: "))
    if c == "q":
        break
"""
c = 0
while c != 9000:
    c += 1
    print(c)

s = 0
c = 0
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    else:
        s += n
        c += 1
print(s, c)

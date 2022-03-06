"""
Dicionário
Em algumas linguagens de programação, os dicionário python são chamados de mapas

Dicionários são coleções do tipo: chave/valor

[0, 1, 2]   (0, 1, 2)
[1, 2, 3]   (1, 2, 3)

Dicionário são representados por {}

# Chave e valor são separados por dois pontos
# Tanto chave quanto valor podem ser de qualquer tipo de dados
# Podemos misturar os tipos de dados
# Pode-se acessar elementos em um dicionário informando a chave entre colchetes
# Caso acesse com uma chave que não existe, obviamente dará erro
# Pode-se acessar um elemento pela forma .get, sendo essa a mais recomendada
# Com o modo .get quando se pede uma chave que não existe o programa não dá erro
# Podemos utilizar None quando queremos inicializa-la  com nada
# Pode-se definir um valor padrão caso não se se encontre a chave informada
# Podemos verificar se determinada chave encontra-se no dicionário, lembrando que não se procura valores apenas chaves
# Tuplas são indicadas para serem chaves de dicionários, pois são imutáveis
# Pode-se adicionar valores em dicionário de forma: dicionario["chave"] = valor/ ou dicionário.update({"chave": valor})
# Também há como mudar os valores de um dicionário, basta informar a chave e depois informar a troca de valor
# Pode-se também atualizar os valores de um dicionário do mesmo jeito que se adiciona um valor
# Em um dicionário não se admite chaves repetidas
# Quando se tenta adicionar uma chave já existente ela atualiza o valor da já existente
# Pode-se remover um valor de um dicionário com a função pop, o valor é retornado logo em seguida
# Pode-se remover também com a método del, só que nesse caso o valor não é retornado
# Tanto com del e pop quando tenta remover um íntem já removido irá gerar um keyerror
# Pode-se limpar um dicionário com a função .clear
# Há como fazer a cópia de um dicionário para o outro com deep copy e shallow copy
# Use o fromkeys caso precise de mais de uma chave com o mesmo valor

# - 1° Forma
paises = {"br": "Brasil", "eua": "Estados Unidos da América", "bel": "Bélgica"}
print(paises)
print(type(paises))

# - 2° Forma
paises = dict(br="Brasil", eua="Estadors Unidos", bel="Bélgica")
print(paises)
print(type(paises))

# 1° Forma
paises = {"br": "Brasil", "eua": "Estados Unidos da América", "bel": "Bélgica"}
print(paises["eua"])
print(paises["bel"])

# 2° Forma
print(paises.get("eua"))
print(paises.get("br"))
print(paises.get("bel"))
print(paises.get("ru"))
print(type(None))

paises = {"br": "Brasil", "eua": "Estados Unidos da América", "bel": "Bélgica"}
paises = paises.get("br")
if paises:
    print("Encontrei o pais " + paises)
else:
    print("Não encontrei")

paises = {"br": "Brasil", "eua": "Estados Unidos da América", "bel": "Bélgica"}
paises = paises.get("br", "Não econtrado")
print(paises)

paises = {"br": "Brasil", "eua": "Estados Unidos da América", "bel": "Bélgica"}
print("br" in paises)
print("Estados Unidos da América" in paises)
print("bel" in paises)

if "ru" in paises:
    print(paises.get("ru"))
else:
    print("Não têm ru")
    print("Mas temos...")
    print(paises.get("br"))
    print(paises.get("eua"))
    print(paises.get("bel"))

localidades = {
    (331, 64960000): "Casa de Guilherme",
    (3345, 64960000): "Escola de Guilherme",
    (33187, 64960000): "Quintal de Guilherme",
}
print(localidades)
print(type(localidades))

receita = {"jan": 100, "fev": 200, "mar": 300}
print(receita)

# 1° Forma
receita["abr"] = 400
print(receita)

# 2° Forma
receita.update({"mai": 500})
print(receita)
novo = {"jun": 600}
receita.update(novo)
print(receita)

# 1° Forma
receita = {"jan": 100, "fev": 200, "mar": 300}
print(receita)
receita["fev"] = 780
print(receita)

# 2° Forma
receita = {"jan": 100, "fev": 200, "mar": 300}
print(receita)
receita.update({"fev": 9871})
print(receita)

# 1° Forma
receita = {"jan": 100, "fev": 200, "mar": 300}
print(receita)
ret = receita.pop("mar")
print(ret)
print(receita)

# 2° Forma
print(receita)
del receita["jan"]
print(receita)

# 3° Forma
receita.clear()
print(receita)

Imágine uma loja
Com listas e tuplas será necessário saber os índices, tornando a informação mais rústica
observe como fica com dicionário:

carrinho = []
produto1 = {"nome": "Carro", "qntd": 1, "preço": 45.000}
produto2 = {"nome": "Casa", "qntd": 1, "preço": 350.00}
print(produto1)
print(produto2)
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

carrinho = []
produto1 = {}
produto2 = {}
nome = input("Qual o nome do primeiro produto? ")
produto1["nome"] = nome
quantidade = input("Qual a quantidade do primeiro produto? ")
produto1["qntd"] = quantidade
price = float(input("Qual o preço primeiro produto? "))
produto1.update({"preço": price})
nome = input("Qual o nome do segundo produto? ")
produto2["nome"] = nome
quantidade = input("Qual a quantidade do segundo produtos? ")
produto2["qntd"] = quantidade
price = float(input("Qual o preço do segundo produto? "))
produto2.update({"preço": price})
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

É fácil observar que é mais fácil de acessar, adicionar ou apagar elementos com dicionários

receita = {"jan": 100, "fev": 200, "mar": 300}
receita.clear()
print(receita)

# 1° Forma Deep copy
receita = {"jan": 100, "fev": 200, "mar": 300}
novo = receita.copy()
print(novo)
novo["jan"] = 50
print(receita)
print(novo)

# 2° Forma Shallow copy
receita = {"jan": 100, "fev": 200, "mar": 300}
novo = receita
print(novo)
novo["fev"] = 654
print(novo)
print(receita)

outro = {}.fromkeys("a", "b")
print(type(outro))
print(outro)

usuario = {}.fromkeys(["Luis", "Guilherme", "Alves", "de"], "Carvalho")
print(usuario)
print(type(usuario))

veja = {}.fromkeys("Luis", "Guilherme")
print(veja)
nom = {}.fromkeys("aptdpa", "Vlau")
print(nom)

nop = {}.fromkeys(range(1, 5), "PAU")
print(nop)

O método fromkeys recebe dois parametros, um iterável e um valor
Ele irar gerar para cada valor iterável uma chave e atribuir  a esta chave o valor informado

computadores = []
odyssey = {"nome": "odyssey 2", "preço": 5499.00, "lançamento": 2019}
legion = {"nome": "legion y530", "preço": 6000.00, "lançamento": 2018}
computadores.append(odyssey)
computadores.append(legion)
print(computadores)
print(computadores[1]["preço"])


pessoas = {}
pessoas.update({"nome": "Luis Guilherme"})
pessoas["idade"] = 17
pessoas.update({"sexo": "masculino"})
print(pessoas)
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k, v in pessoas.items():
    print(f"O {k} é {v}")
del pessoas["sexo"]

paises = []
estado = {}
while True:
    estado["uf"] = str(input("Nome do estado: ")).capitalize()
    estado["sigla"] = str(input("Sigla do estado: ")).upper()
    paises.append(estado.copy())
    escolha = input("Continuar? [S/N]: ").upper()
    if escolha == "N":
        break
print(paises)
for c in paises:
    for e in c.values():
           print(e)

# Desempacotando valores de um dicionário
dici = {"a": 1, "b": 2}
num, num1 = dici.values()
print(num, num1)
# Para desempacotar as chaves basta trocar o .values por .keys, para pegar o ítem basta não colocar nada
"""

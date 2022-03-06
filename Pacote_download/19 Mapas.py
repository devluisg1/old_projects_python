"""
Mapas
Conhecidos em python como dicionários
# Há como iterar sobre mapas/dicionário com repetições while e for
# É recomendado que se acesse as chaves quando com a função .keys, principalmente quando for caso de iteração
# Há como acessar os valores de um dicionário usando a função .values
# Para desempacotar os valores de um dicionário use repetição e a função .items
# O método popitem serve para apagar o último elemento de um dicionário

receita = {"jan": 100, "fev": 200, "mar": 300}
for c in receita:
    print(c)
print("=" * 20)
for c in receita:
    print(receita[c])
print("=" * 20)
for c in receita:
    print(f"A chave {c} tem o valor {receita[c]}")
print("=" * 20)
print(receita.keys())
print("=" * 20)

for c in receita.keys():
    print(c, receita[c])

receita = {"jan": 100, "fev": 200, "mar": 300}
print(receita.values())

receita = {"jan": 100, "fev": 200, "mar": 300}
print(receita.items())
for c, v in receita.items():
    print(c, v)

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))

print(receita.popitem())
print(receita)
print(receita.pop("fev") )
print(receita)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)
"""
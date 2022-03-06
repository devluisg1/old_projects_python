"""
Módulo Collections - Defoult Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

Recaptulando dicionário

dic = {'curso': 'Pogramção em python'}
print(dic['curso'])
print(dic)
print(dic['outro'])# Isso irá gerar um key error, pois não existe este ítem no dicionário

Default Dict = Ao criar um dicion´raio utilizando-o, nós informamos um valor default.
Podeser ser utilizado um lambda para isso. Este valor sempre será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave não existente, essa chave será criada e o valor default
será atribuído.

obs: lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores

from collections import defaultdict
dici = defaultdict(lambda: 0)
dici.update({'curso': 'Pogramção em python'})
print(dici)
print(dici['outro'])# Isso não gera o key error
print(dici)

# Todas as funções e métodos que funcionam em um dicionário normal funcionam num Default Dict
"""

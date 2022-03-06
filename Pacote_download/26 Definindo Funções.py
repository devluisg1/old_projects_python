"""
Definindo Funções

# Funções são pequenas partes de código que realizam tarefas específicas
# Uma função pode ou não receber entrada de dados e retornar uma saída de dados
# Funções são muit úteis para executar procedimentos similares por repetidas vezes:
# É recomendado que se faça funções simples
# Toda função que já vem integrada na linguagem de programação, é chamada de Built-ins
# Existem funções globais, sendo essas que funcionam em qualquer tipo de dados
# Porém existem funções que são restritas a apenas um tipo de dados ou a alguns.
# Exemplo: A função append só funcionam em lista, por outro lado o print funciona em todos os tipos de dados.
Obs: Se você escrever uma função que realiza várias tarefas dentro dela:
é bom fazer uma verficaçãp para que  a função seja simplificada.
# Existem funções que recebem algum tipo de dado de entrada e outraas que não necessitam desses dados
# Funções sem o ponto no começo a exemplo do print não dependem de outros objetos, já as com ponto
exemplo de count, dependem de outros objetos
# O DRY ou Dont Repeat Yoursel (Não Repita Você mesmo) que consiste em você evitar repetir códigos
já emplementados antes
# Em python, defini-se funções geralmente:
usando def  nome_da_função(parametros_de_entrada):
    bloco_da_função

nome_da_função - Sempre,  com letras minúsculas, e se for nome composto, sempre deve ser separado
por anderline. (Snake Case)

parametros_de_entrada - São opcionais, onde tendo mais de um, cada um separado por vírgula, podendo opcionais
novamente dizendo

bloco_da_função - Também chamados de coropo da função ou implementação, é onde o processamento da função
acontece. Neste bloco, pode ter ou não um retorno.

OBS: Veja que para definir uma função, utilizamos a palavra revervada 'def' iformando o Pytho que
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontosc:
Que é utilizado em python para definir blocos
Iremos aprender a fazer funções, mas elas já são utilizadas desde o começo do uso de uma linguagem
de programação

Exemplo de funções:
print()
len()
max()
min()
count()
e muitas outrasso

# Exemplo de utilização de funções
cores = ['verde', 'azul', 'branco', 'amarelo']
print(cores)
cores.append('vermelho')
print(cores)



# Definindo a 1° função
def diz_oi():
    print("oi")


# Obs: Veja que dentro das nossas funções, podemos utilizar outras funções
# Obs: Veja que nossa função só exetuca uma tarefa, ou seja, ela só diz oi
# Obs: Veja que esta função não tem parâmetro de entrada, ou seja o parênteses está vazio
# Obs: Veja que esta função não retorna nada
# Obs: Para que uma funçã seja utilizada, ela precisa ser chamada
# Obs: Lembre-se sempre de usar os dois espaços depois de definir uma função
# Obs: Nunca esqueça de abrir e fechar um parênteses para utilizar uma função
# Obs: Não existe espaço entre a função e o parênteses

# Utilizando função:
# Chamada de execução
diz_oi()


def cantar_parabens():
    print('Parabéns pra tu')


for c in range(5):
    cantar_parabens()

# Em Python, podemos inclusive criar uma variável do tipo de uma função e
executar esta função através da varável

def cantar_parabens():
    print('Parabéns pra tu')


canta = cantar_parabens


canta()


Não há necessidade de usar esse modo
"""

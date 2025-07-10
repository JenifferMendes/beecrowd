"""
Leia um número inteiro que representa um código de DDD para discagem 
interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando 
a tabela abaixo:
Se a entrada for qualquer outro DDD que não esteja presente na tabela acima,
o programa deverá informar:
DDD nao cadastrado
Entrada
A entrada consiste de um único valor inteiro.
Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. 
Imprima DDD nao cadastrado caso não existir DDD correspondente ao 
número digitado.
"""


ddd = [
    [61, "Brasilia"],
    [71, "Salvador"],
    [11, "Sao Paulo"],
    [21, "Rio de Janeiro"],
    [32, "Juiz de Fora"],
    [19, "Campinas"],
    [27, "Vitoria"],
    [31, "Belo Horizonte"]
]

codigo = int(input())

if not any(codigo == item[0] for item in ddd):
    print("DDD nao cadastrado")
    
for c, d in enumerate(ddd):
    if codigo == ddd[c][0]:
         print(f"{ddd[c][1]}")


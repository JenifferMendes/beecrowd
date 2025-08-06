"""
Leia um conjunto não determinado de pares de valores M e N 
(parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a
soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. 
A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a 
soma deles, conforme exemplo abaixo.
"""


while True:
    b, a = map(int, input().split())
    if a <= 0 or b <= 0:
        break

    inicio = min(a, b)
    fim = max(a, b)
    soma = 0

    for c in range(inicio, fim + 1):
        soma += c
        print(f"{c} ", end="")
    print(f"Sum={soma}")

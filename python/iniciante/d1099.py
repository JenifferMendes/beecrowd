"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a 
soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de 
teste que vem a seguir. Cada caso de teste consiste em uma linha contendo 
dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
"""

num = int(input())

for c in range(0, num):
    a, b = map(int, input().split())
    impares = 0
    if a == b:
        print(impares)
    elif a < b:
        for d in range(a + 1, b):
            if d % 2 == 1:
                impares += d
        print(impares)
    else:
        for d in range (b + 1, a):
            if d % 2 == 1:
                impares += d
        print(impares)

"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos 
a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
"""

num = int(input())

impares = num

if num % 2 == 1:
    print(num)
    for c in range(0, 5):
        impares += 2
        print(impares)
else:
    impares = num + 1
    print(impares)
    for c in range(0, 5):
        impares += 2
        print(impares)

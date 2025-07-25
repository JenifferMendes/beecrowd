"""
Escreva um programa que leia dois valores X e Y. A seguir, 
mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e 
(X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em 
branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em
branco após o último valor da linha.
"""

x, y = map(int, input().split())

for i in range(1, y + 1):
    print(i, end="\n" if i % x == 0 else " ")
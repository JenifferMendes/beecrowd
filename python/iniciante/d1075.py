"""
Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que 
divididos por N dão resto igual a 2.

Entrada
A entrada contém um valor inteiro N (N < 10000).

Saída
Imprima todos valores que quando divididos por N dão resto = 2, um por linha.
"""

n = int(input())

for c in range(0, 10000):
    if c % n == 2:
        print(c)
"""
Faça um programa que leia um valor T e preencha um vetor N[1000] com a 
sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. 
Imprima o vetor N.

Entrada
A entrada contém um valor inteiro T (2 ≤ T ≤ 50).

Saída
Para cada posição do vetor, escreva "N[i] = x", onde i é a posição do vetor e
x é o valor armazenado naquela posição.
"""


T = int(input())

for i in range(1000):
    print(f"N[{i}] = {i % T}")

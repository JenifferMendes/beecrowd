"""
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores 
nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e 
x é o valor armazenado naquela posição.
"""


numeros = []

for c in range(0, 10):
    num = int(input())
    numeros.append(num)

for p, v in enumerate(numeros):
    if v <=0:
        numeros[p] = 1

for a,b in enumerate(numeros):
    print(f"X[{a}] = {b}")
"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números
impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores 
ímpares que estão 
entre os valores fornecidos na entrada que deverá caber em um inteiro.
"""

a = int(input())
b = int(input())
soma = 0

if a < b:
    for c in range(a + 1, b):
        if c % 2 == 1:
            soma += c
elif a > b:
    for c in range(b + 1, a):
        if c % 2 == 1:
            soma += c
print(soma)
"""
Ler um número inteiro N e calcular todos os seus divisores.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Escreva todos os divisores positivos de N, um valor por linha.
"""

num = int(input())

for c in range(1, num + 1 ):
    if num % c == 0:
        print(c)

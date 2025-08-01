"""
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i 
para cada i com os valores (0 <= i <= N-1). 
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

Entrada
A entrada contém somente valores inteiros, podendo ser positivos ou negativos.
Todos os valores estão na mesma linha.

Saída
A saída contém apenas um valor inteiro.
"""

valores = list(map(int, input().split()))

A = valores[0]
N = None

for valor in valores[1:]:
    if valor > 0:
        N = valor
        break

soma = sum(A + i for i in range(N))

print(soma)

"""
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão 
apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. 
Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

Entrada
O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

Saída
Imprima a saída conforme o exemplo fornecido.

1 1 1
1 2 2
2 4 8
2 5 9
3 9 27
3 10 28
4 16 64
4 17 65
5 25 125
5 26 126
"""

n = int(input())
a =1
for c in range(0, n):
    print(f"{a ** 1} {a ** 2} {a ** 3}")
    print(f"{a ** 1} {a ** 2 + 1} {a ** 3 + 1 }")
    a +=1
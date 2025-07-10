"""
Escreva um programa que leia um valor inteiro N (1 < N < 1000). 
Este N é a quantidade de linhas de saída que serão apresentadas na execução 
do programa.
Entrada
O arquivo de entrada contém um número inteiro positivo N.
Saída
Imprima a saída conforme o exemplo fornecido.
"""


n = int(input())
a = 1

for c in range(0, n):
    print(f"{a ** 1} {a ** 2} {a ** 3 }")
    a += 1
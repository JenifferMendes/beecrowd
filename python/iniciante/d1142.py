"""
Escreva um programa que leia um valor inteiro N.
Este N é a quantidade de linhas de saída que serão apresentadas na execução 
do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
"""


n = int(input())
a = 0

for c in range(0, n):
    print(f"{a+1} {a+2} {a+3} PUM")
    a += 4

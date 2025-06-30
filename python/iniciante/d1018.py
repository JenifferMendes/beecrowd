"""
Leia um valor inteiro. A seguir, calcule o menor número de notas 
possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de 
cada tipo necessárias, conforme o exemplo fornecido. 
"""

saldo = int(input())
print(saldo)

if saldo / 100:
    cem = saldo // 100
    saldo = saldo % 100
    print(f"{cem} nota(s) de R$ 100,00")
if saldo / 50:
    cinquenta = saldo // 50
    saldo = saldo % 50
    print(f"{cinquenta} nota(s) de R$ 50,00")
if saldo / 20:
    vinte = saldo // 20
    saldo = saldo % 20
    print(f"{vinte} nota(s) de R$ 20,00")
if saldo / 10:
    dez = saldo // 10
    saldo = saldo % 10
    print(f"{dez} nota(s) de R$ 10,00")
if saldo / 5:
    cinco = saldo // 5
    saldo = saldo % 5
    print(f"{cinco} nota(s) de R$ 5,00")
if saldo / 2:
    dois = saldo // 2
    saldo = saldo % 2
    print(f"{dois} nota(s) de R$ 2,00")
print(f"{saldo} nota(s) de R$ 1,00")

"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor 
representa um valor monetário. A seguir, calcule o menor número de notas 
e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis 
são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor 
inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""

saldo = float(input())
cem = cinquenta = vinte = dez = cinco = dois = 0
um = cents = quart = ten = five = one = 0

print("NOTAS:")
if saldo / 100 :
    cem = int(saldo // 100)
    saldo = saldo % 100
print(f"{cem} nota(s) de R$ 100.00")
if saldo / 50:
    cinquenta = int(saldo // 50)
    saldo = saldo % 50
print(f"{cinquenta} nota(s) de R$ 50.00")
if saldo / 20 :
    vinte = int(saldo // 20)
    saldo = saldo % 20
print(f"{vinte} nota(s) de R$ 20.00")
if saldo / 10:
    dez = int(saldo // 10)
    saldo = saldo % 10
print(f"{dez} nota(s) de R$ 10.00")
if saldo / 5:
    cinco = int(saldo // 5)
    saldo = saldo % 5
print(f"{cinco} nota(s) de R$ 5.00")
if saldo / 2:
    dois = int(saldo // 2)
    saldo = saldo % 2
print(f"{dois} nota(s) de R$ 2.00")
print("MOEDAS:")
if saldo / 1:
    um = int(saldo // 1)
    saldo = saldo % 1
print(f"{um} moeda(s) de R$ 1.00")
if saldo / 0.50 :
    cents = int(saldo // 0.5)
    saldo = saldo % 0.5
print(f"{cents} moeda(s) de R$ 0.50")
if saldo / 0.25 :
    quart = int(saldo // 0.25)
    saldo = saldo % 0.25
print(f"{quart} moeda(s) de R$ 0.25")
if saldo / 0.1 :
    ten = int(saldo // 0.1)
    saldo = saldo % 0.1
print(f"{ten} moeda(s) de R$ 0.10")
if saldo / 0.05 :
    five = int(saldo // 0.05)
    saldo = saldo % 0.05
print(f"{five} moeda(s) de R$ 0.05")
if saldo / 0.01 :
    one = saldo * 100
    print(one)
print(f"{one:.0f} moeda(s) de R$ 0.01")

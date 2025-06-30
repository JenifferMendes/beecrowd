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

saldo = int(input().replace(".", ""))

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade = saldo // nota
    saldo = saldo % nota
    print(f"{quantidade:.0f} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    quantidade = saldo // moeda
    saldo = saldo % moeda
    print(f"{quantidade:.0f} moeda(s) de R$ {moeda / 100:.2f}")

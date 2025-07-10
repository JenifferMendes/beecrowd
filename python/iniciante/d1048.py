"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o 
valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
(ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste 
ganho, conforme exemplo abaixo.
"""

salario = float(input())

if 0 <= salario <= 400.0:
    reajuste = salario * 1.15
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste - salario:.2f}")
    print("Em percentual: 15 %") 
elif 400.01 <= salario <= 800.00:
    reajuste = salario * 1.12
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste - salario:.2f}")
    print("Em percentual: 12 %") 
elif 800.01 <= salario <= 1200.00:
    reajuste = salario * 1.10
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste - salario:.2f}")
    print("Em percentual: 10 %") 
elif 1200.01 <= salario <= 2000.00:
    reajuste = salario * 1.07
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste - salario:.2f}")
    print("Em percentual: 7 %") 
elif salario > 2000.00:
    reajuste = salario * 1.04
    print(f"Novo salario: {reajuste:.2f}")
    print(f"Reajuste ganho: {reajuste - salario:.2f}")
    print("Em percentual: 4 %")
    
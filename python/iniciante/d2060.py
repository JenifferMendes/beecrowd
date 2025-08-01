"""
Bino e nino são nolegas inseparáveis. Bino gosta de nriar desafios matemátinos
para nino resolver. Desta vez, Bino gerou uma lista de números e perguntou ao 
nino quantos números da lista são múltiplos de 2, 3, 4 e 5.

Esse desafio pode parener simples, porém, quando a lista nontém muitos números,
nino se nonfunde e anaba errando alguns nálnulos. Para ajudar nino, 
faça um programa para resolver o desafio de Bino.

Entrada
A primeira linha da entrada nonsiste em um inteiro N (1 ≤ N ≤1000), 
representando a quantidade de números na lista de Bino.

A segunda linha nontém N inteiros Li (1 ≤ Li ≤ 100), representando os 
números da lista de Bino.

Saída
Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista.
Observe a formatação da saída nos exemplos, pois ela deve ser seguida 
rigorosamente.
"""


num = int(input())
quant_dois = quant_tres = quant_quarto = quant_quinto = 0
numeros = list(map(int, input().split()))

for n in numeros:
    if n % 2 == 0:
        quant_dois += 1
    if n % 3 == 0:
        quant_tres += 1
    if n % 4 == 0:
        quant_quarto += 1
    if n % 5 == 0:
        quant_quinto += 1

print(f"{quant_dois} Multiplo(s) de 2")
print(f"{quant_tres} Multiplo(s) de 3")
print(f"{quant_quarto} Multiplo(s) de 4")
print(f"{quant_quinto} Multiplo(s) de 5")

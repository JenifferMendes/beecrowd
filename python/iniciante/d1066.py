"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
quantos valores digitados foram ímpares, quantos valores digitados foram 
positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não 
esquecendo o final de linha após cada uma.
"""
pares = impares = positivos = negativos = 0

for c in range(0,5):
    num = int(input())
    if num > 0:
        positivos += 1
        if num % 2 == 0:
            pares += 1
        else: 
            impares += 1
    if num < 0:
        negativos += 1
        if num % 2 == 0:
            pares += 1
        else: 
            impares += 1
    if num == 0:
        pares += 1
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")

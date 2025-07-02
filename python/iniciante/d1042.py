"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, 
mostre os valores em ordem crescente, uma linha em branco e em seguida, 
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""


a, b, c = map(int, input().split())

valores = [a, b, c]
crescente = valores[:]
crescente.sort()

for c in crescente:
    print(c)

print()

for valor in valores:
    print(valor)

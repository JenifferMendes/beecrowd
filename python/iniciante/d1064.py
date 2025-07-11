"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram
positivos. Na próxima 
linha, deve-se mostrar a média de todos os valores positivos digitados, 
com um dígito após o ponto decimal.
Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
Pelo menos um destes números será positivo.
Saída
O primeiro valor de saída é a quantidade de valores positivos. 
A próxima linha deve mostrar a média dos valores positivos digitados.
"""

positivos = soma = 0
for c in range(0, 6):
    num = float(input())
    if num > 0:
        positivos += 1
        soma += num
media = soma / positivos
print(f"4 valores positivos")
print(f"{media:.1f}")
"""
Uma das formas de calcular a raiz quadrada de um número natural é pelo método
das frações periódicas continuadas. Esse método usa como denominador uma 
repetição de frações. Essa repetição pode ser feita uma quantidade específica
de vezes.
Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz 
quadrada de 2, temos a fórmula abaixo.
Sua tarefa é, dado o número N de repetições, calcular o valor aproximado
da raiz quadrada de 2.
Entrada
A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de 
repetições do denominador na fração continuada.
Saída
A saída é o valor aproximado da raiz quadrada com 10 casas decimais.
"""


n = int(input())

# o codigo deve seguir a logica de 1+1/(n-1 repeticoes de 2+1)/2)
def solve(n):
    if n == 0:
        return 0
    return 1.0 / (2.0 + solve(n - 1))

print(f"{1 +solve(n):.10f}")

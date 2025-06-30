"""
Leia um valor inteiro, que é o tempo de duração em segundos de um 
determinado evento em uma fábrica, e informe-o expresso no formato 
horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido 
para horas:minutos:segundos, conforme exemplo fornecido.
"""

segundo = int(input())
hora = minuto = 0

if segundo > 60:
    minuto = segundo // 60
    segundo = segundo % 60
if minuto > 60:
    hora = minuto // 60
    minuto = minuto % 60
print(f"{hora}:{minuto}:{segundo}")

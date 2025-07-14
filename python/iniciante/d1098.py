"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.
	
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""

i = 0.0
j = 1.0

while i <= 2.0:
    for c in range(0,3):
        print(f"I={i:.1f} J={j:.1f}")
        j += 1 
    i += 0.2
    j += 0.2
print("fim")
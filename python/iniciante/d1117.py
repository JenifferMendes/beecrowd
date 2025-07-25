"""
Faça um programa que leia as notas referentes às duas avaliações de um aluno.
Calcule e imprima a média semestral.
Faça com que o algoritmo só aceite notas válidas 
(uma nota válida deve pertencer ao intervalo [0,10]).
Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. 
O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem
"media = " seguido do valor do cálculo. O valor deve ser apresentado com 
duas casas após o ponto decimal.

"""

while True:
    a = float(input())
    if 10.0 >= a >= 0:
        break
    else:
        print("nota invalida")
    
while True:
    b = float(input())
    if 10.0 >= b >= 0:
        break
    else:
        print("nota invalida")

media = (a + b) / 2
print(f"media = {media:.2f}")
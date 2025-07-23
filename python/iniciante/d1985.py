"""
O MacPRONALTS está com uma super promoção, exclusivo para os competidores da 
primeira Seletiva do MaratonaTEC. Só que teve um problema, 
todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma
fila muito grande. O pior é que a moça do caixa estava sem calculadora ou um
programa para ajudá-la a calcular com maior agilidade, eis que surge você para 
fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS.
Segue o cardápio do dia contendo o número do produto e seu respectivo valor.

1001 | R$ 1.50

1002 | R$ 2.50

1003 | R$ 3.50

1004 | R$ 4.50

1005 | R$ 5.50

Entrada
A primeira entrada informada é a quantidade de produtos comprados (1 <= p <= 5).
Para cada produto segue a quantidade (1 <= q <= 500) que o consumidor comprou.

Obs.: não poderão ser informados números de produtos repetidos.

Saída
Você deve imprimir o valor da compra com duas casas decimais.
"""

produtos = [
    1001, 1.50 ,
    1002, 2.50 ,
    1003, 3.50 ,
    1004, 4.50 ,
    1005, 5.50 ,
]


num = int(input())
total = 0
for c in range(0, num):
    codigo, quantidade = map(int, input().split())
    for d in produtos:
        if codigo == d:
            valor = produtos.index(d)
            preco = produtos[valor + 1] * quantidade
            total += preco
print(f"{total:.2f}")

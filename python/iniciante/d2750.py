"""
O seu professor de programação gostaria que você fizesse um programa com as 
seguintes características:

Criar 16 variáveis inteiras;
Atribuir a elas valores de 0 a 15 a cada um das variáveis anteriores;
Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do 
trigésimo nono traço da primeira linha, embaixo do 4o traço deve começar a 
escrever “decimal”, embaixo do 16o traço deve começar a escrever “octal”, 
embaixo do 26o traço deve começar a escrever “Hexadecimal” e o restante
preencher com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço, décimo terceiro, vigésimo terceiro e do 
trigésimo nono traço da primeira linha, embaixo do 8o traço deve imprimir o 
valor da primeira variável em valor decimal, embaixo do 18o traço deve 
imprimir o valor da primeira variável em valor octal, embaixo do 31o traço 
deve imprimir o valor da primeira variável em valor hexadecimal e o 
restante preencher com espaço em branco;
Repita o procedimento 6 para as outras 15 variáveis;
Repita o procedimento 3.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|  decimal  |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
--------------------------------------- (39 traços)
---------------------------------------
| decimal   |  octal  |  Hexadecimal  |
---------------------------------------
|      0    |    0    |       0       |
|      1    |    1    |       1       |
|      2    |    2    |       2       |
|      3    |    3    |       3       |
|      4    |    4    |       4       |
|      5    |    5    |       5       |
|      6    |    6    |       6       |
|      7    |    7    |       7       |
|      8    |   10    |       8       |
|      9    |   11    |       9       |
|     10    |   12    |       A       |
|     11    |   13    |       B       |
|     12    |   14    |       C       |
|     13    |   15    |       D       |
|     14    |   16    |       E       |
|     15    |   17    |       F       |
---------------------------------------
"""


numeros = list(range(16))
dash = '-' * 39
print(dash)
print("|  decimal  |  octal  |  Hexadecimal  |")
print(dash)

for n in numeros:
    print(f"|{n:>7}{' ' * 4}| {oct(n)[2:]:^7} | {hex(n)[2:].upper():^13} |")

print(dash)


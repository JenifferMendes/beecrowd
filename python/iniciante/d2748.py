"""
O seu professor de programação gostaria de fazer uma tela com as seguintes 
características:

Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira 
linha, embaixo do 10 traço deve começar a escrever a palavra "Roberto" e o 
restante preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira 
linha, preencher no meio com espaço em branco;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira 
linha, embaixo do 10 traço deve começar a escrever o número "5786" e o 
restante preencher no meio com espaço em branco;
Repita o procedimento 3;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira 
linha, embaixo do 10 traço deve começar a escrever a palavra "UNIFEI" e o 
restante preencher no meio com espaço em branco;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|        Roberto                      |
|                                     |
|        5786                         |
|                                     |
|        UNIFEI                       |
--------------------------------------- (39 traços)

Entrada
Não há.

Saída
A saída será impresso conforme a figura acima.
"""


n = 39
dash = '-' * n
dash_dois = f"{'|':<{n/2}}{'|':>{n/2 + 1}}"
print(dash)
print(f"{'|':<{8}} {'Roberto':<{13}}{'|':>{17}}")
print(dash_dois)
print(f"{'|':<{8}} {'5786':<{13}}{'|':>{17}}")
print(dash_dois)
print(f"{'|':<{8}} {'UNIFEI':<{13}}{'|':>{17}}")
print(dash)
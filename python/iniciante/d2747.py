"""

O seu professor de programação gostaria de fazer uma tela com as seguintes 
características:

Ter 39 traços (-) na primeira linha;
Ter uma | embaixo do primeiro traço e do trigésimo nono traço da primeira 
linha, preencher no meio com espaço em branco;
Repita o procedimento 2 mais quatro vezes;
Repita o procedimento 1.
No final deve ficar igual a imagem a seguir:

--------------------------------------- (39 traços)
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |
--------------------------------------- (39 traços)
Entrada
Não há.

Saída
A saída será impressa conforme a figura acima.
"""

n = 39
dash = '-' * n
print(dash)
for c in range(0, 5):
    print(f"{'|':<{n/2}}{'|':>{n/2 + 1}}")
print(dash)

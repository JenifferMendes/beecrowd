"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal 
possível segundo o esquema abaixo, da esquerda para a direita.  
Em seguida conclua qual dos animais seguintes foi escolhido, através das 
três palavras fornecidas.

Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para 
identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
"""


opcao = input()
opcao_dois = input()
opcao_tres = input()


if opcao == 'vertebrado':
    if opcao_dois == 'ave':
        if opcao_tres == 'carnivoro':
            print('aguia')
        elif opcao_tres == 'onivoro':
            print('pomba')
    elif opcao_dois == 'mamifero':
        if opcao_tres == 'onivoro':
            print('homem')
        elif opcao_tres == 'herbivoro':
            print('vaca')
if opcao == 'invertebrado':
    if opcao_dois == 'inseto':
        if opcao_tres == 'hematofago':
            print('pulga')
        elif opcao_tres == 'herbivoro':
            print('lagarta')
    elif opcao_dois == 'anelideo':
        if opcao_tres == 'hematofago':
            print('sanguessuga')
        elif opcao_tres == 'onivoro':
            print('minhoca')

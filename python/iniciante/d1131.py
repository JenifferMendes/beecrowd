"""
A Federação Gaúcha de Futebol contratou você para escrever um programa para 
fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para 
ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. 
Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma 
resposta. Se a resposta for 1, o algoritmo deve ser executado novamente 
solicitando o número de gols marcados pelos times em uma nova partida, 
caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS 
(ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols
marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro 
(1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal
(1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas 
as estatísticas conforme a descrição apresentada acima. Obs: a palavra
"Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.
"""

grenais = gre = interv = empate = 0

while True:
    inter, gremio = map(int, input(). split())
    grenais += 1
    if inter > gremio:
        interv += 1
    elif inter < gremio:
        gre += 1
    else:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    num = int(input())
    if num == 2:
        break
    
print(f"{grenais} grenais")
print(f"Inter:{interv}")
print(f"Gremio:{gre}")
print(f"Empates:{empate}")

if interv > gre:
    print(f"Inter venceu mais")
elif interv < gre:
    print(f"Gremio venceu mais")
elif interv == gre:
    print(f"Nao houve vencedor")
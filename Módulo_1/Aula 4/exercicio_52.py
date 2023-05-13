"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""

from random import randint

players = dict()
counter = 0

print("Valores sorteados: \n")

for i in range(4):
    jodada = randint(1, 6)
    players[f"Jogador {i + 1}"] = jodada

    print(f"O jogador {i + 1} tirou {jodada} pontos no dado.")

print("\n Ranking dos jogadores:")

players_list = sorted(list(zip(players.values(), players.keys())),reverse=True)

for i, player in enumerate(players_list):
    print(f"{i+1}º lugar:{players_list[i][1]} com {players_list[i][0]} pontos")
    counter +=1

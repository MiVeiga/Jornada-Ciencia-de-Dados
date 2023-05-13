"""
Suponha que você tenha uma lista com o nome e a 
altura de todas as pessoas que estão em uma fila, 
e deseja ordenar a fila da pessoa mais alta para a pessoa mais baixa

fila = (("Ana", 1.75), ("Pedro", 1.68), ("João", 1.82), ("Maria", 1.70), ("Carlos", 1.90))

"""

fila = [("João", 1.8), ("Maria", 1.6), ("Pedro", 1.75), ("Ana", 1.68), ("Carlos", 1.9)]

fila_ordenada = sorted(fila, key=lambda x: x[1], reverse=True)

print("Fila ordenada da pessoa mais alta para a mais baixa:")
for nome, altura in fila_ordenada:
    print(f"{nome} - {altura}")
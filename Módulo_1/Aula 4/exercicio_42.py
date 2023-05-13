"""
Suponha que você tenha uma lista com o nome de todas as pessoas que entraram em um evento.
Essa lista foi sendo alimentada de acordo com a ordem se chegada.
Imprima o nome da primeira pessoa e o nome da última pessoa que chegou.

nomes = ("Ana", "Pedro", "João", "Maria", "Carlos")
"""
nomes = ("Pedro","Ana",  "João","Carlos","Maria")

primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro nome:{primeiro_nome}")
print(f"Último nome:{ultimo_nome}")
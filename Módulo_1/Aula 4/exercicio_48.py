"""
Suponha que você tenha uma lista de músicas, 
mas quer remover todas as ocorrências da música "Bohemian Rhapsody"
musicas = ["Stairway to Heaven", "Bohemian Rhapsody", "Sweet Child O' Mine", "Bohemian Rhapsody", "Hotel California", "Bohemian Rhapsody"]
"""

musicas = ["Stairway to Heaven", "Bohemian Rhapsody", "Sweet Child O' Mine", "Bohemian Rhapsody", "Hotel California", "Bohemian Rhapsody"]
while "Bohemian Rhapsody" in musicas:
    musicas.remove("Bohemian Rhapsody")
print(musicas)

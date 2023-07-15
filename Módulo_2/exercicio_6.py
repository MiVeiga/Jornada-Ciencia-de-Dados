# Desenvolva um programa que conte quantas vezes a palavra
#  "comentário" foi mencionada em uma seção de comentários
# de uma publicação no LinkedIn, utilizando um loop for.
# comments = ["Ótimo comentário!", "Concordo com o comentário anterior.",
#   "Esse comentário é muito relevante.", "comentário interessante!"]


comments = ["Ótimo comentário!", "Concordo com o comentário anterior.",
            "Esse comentário é muito relevante.", "comentário interessante!"]


# Amanda
comentario = ["Ótimo comentário!", "Concordo com o comentário anterior.",
              "Esse comentário é muito relevante.", "comentário interessante!"]

contador = 0

for comentario in comentario:
    if "comentário" in comentario:
        contador += 1

print("foi mencionada", contador, "vezes.")

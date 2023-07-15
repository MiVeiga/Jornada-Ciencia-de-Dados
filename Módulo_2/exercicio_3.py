# Escreva um programa que conte quantos caracteres "a" existem em todas as
# postagens de um usuário do Twitter, utilizando um loop while.

# tweets = ["Estou adorando a nova função do Twitter!",
# "Só aqui no Twitter para encontrar as melhores notícias!",
# "Acompanhando os tweets sobre o lançamento do novo filme.",
# "Essa temporada de futebol está sensacional! #VaiTime"]

#Pedro
tweets = ["Estou adorando a nova função do Twitter!",
"Só aqui no Twitter para encontrar as melhores notícias!",
"Acompanhando os tweets sobre o lançamento do novo filme.",
"Essa temporada de futebol está sensacional! #VaiTime"]

tweet = 0
count_a = 0
while tweet < len(tweets):
    count_a += tweets[tweet].lower().count('a')
    tweet +=1

print(count_a)
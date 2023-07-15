#Crie uma função chamada `contar_likes` que receba 
# uma lista de posts de uma rede social 
# e retorne a quantidade total de likes desses posts.
#posts = [
#     {'id': 1, 'likes': 10},
#     {'id': 2, 'likes': 5},
#     {'id': 3, 'likes': 15}
# ]

posts = [
    {'id': 1, 'likes': 2},
    {'id': 2, 'likes': 5},
    {'id': 3, 'likes': 15}
]

def contar_likes(banana):
    total_likes = 0 

    for post in banana:
        total_likes +=post["likes"]
    return total_likes


print(contar_likes(posts))



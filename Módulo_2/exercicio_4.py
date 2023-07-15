#Faça um programa que exiba os usuários que possuam 
# mais de 100 seguidores no Instagram, utilizando um loop for.
#followers = {"user1": 150, "user2": 300, "user3": 50, "user4": 120, "user5": 80}

followers = {"user1": 150, "user2": 300, "user3": 50, "user4": 120, "user5": 80}

for user, number in followers.items():
    if number > 100:
        print(user)







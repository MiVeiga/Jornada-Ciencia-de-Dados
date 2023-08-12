# Desenvolva um programa em Python que exiba os primeiros
# 10 números primos encontrados em uma lista de amigos do Facebook.
# friends_list = [2, 3, 5, 6, 8, 10, 11, 13, 15, 17, 19, 21]

# def is_prime(num):
#     if num <=1:
#         False
#     for i in range(2, num):
#         if num % i == 0:
#             False
#     return True

# def is_prime(num): 
#     if num <= 1: False 
#     for i in range(2, num): 
#         if num % i == 0: 
#             if (num % num == 0):
#                  False 
#     return True

# def is_prime(num): 
#     status = False 
#     if num <= 1: 
#         status = False 
#     for i in range(2,num):
#         if num % i == 0: 
#             status = False 
#             break 
#         else: 
#             status = True 
#     return status

def is_prime(num):
    if num < 2: 
        return False
    for i in range(2,int(num ** 0.5)+1 ):
        if num % i == 0:
            return False
    return True

friends_list = [2, 3, 5, 6, 8, 10, 11, 13, 15, 17, 19, 21]

count = 0

for friend in friends_list:
    if is_prime(friend):
        print(friend)
        count += 1
    if count == 10:
        break

"""
Crie um programa que pergunte ao usuário se ele é vegetariano e se ele é alérgico a glúten. 
Se o usuário for vegetariano e alérgico a glúten, 
imprima "Você pode comer no restaurante X", caso contrário, 
imprima "Você não pode comer no restaurante X".
"""

vegetariano = input("Você é vegetariano? (sim/não) \n")
gluten = input("Você é alérgico a glúten? (sim/ não) \n")

if vegetariano == "sim" and gluten =="sim":
    print("Você pode comer no restaurante x")
else:
    print("Você não pode comer no restaurante x")
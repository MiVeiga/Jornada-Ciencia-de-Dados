"""""
Crie um programa que pergunte ao usuário se ele é fumante e 
se tem pressão alta. Se o usuário for fumante e tiver pressão alta, 
imprima "Você precisa parar de fumar urgentemente", 
caso contrário, imprima "Parabéns por não fumar ou por manter sua pressão arterial controlada".
"""

fumante = input("Você é fumante? (s/n) \n")
pressao = input("Você tem pressão alta? (s/n) \n")

if fumante == "s" and pressao == "s":
    print("Você precisa parar de fumar urgentemente")
else:
    print("Parabéns por não fumar ou por manter sua pressão arterial controlada")
"""""
Crie um programa que verifique se uma pessoa tem idade suficiente e altura suficiente para andar 
em um brinquedo de parque de diversões. 
Para andar no brinquedo, é preciso ter mais de 12 anos e medir mais de 1,50m.
"""

idade = int(input("Digite a idade da pessoa: "))
altura = float(input("Digite a altura da pessoa em metros: "))
if idade > 12 and altura > 1.50:
    print("Esta pessoa pode andar no brinquedo.")
else:
    print("Esta pessoa não pode andar no brinquedo.")

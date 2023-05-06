"""
Crie um programa que verifique se uma pessoa pode doar sangue. 
Para doar sangue, é preciso ter entre 18 e 69 anos e pesar mais de 50kg.
"""

idade = int(input("Digite a idade da pessoa: "))

peso = float(input("Digite o peso da pessoa em kg: "))

if idade >= 18 and idade <= 69 and peso > 50:
    print("Esta pessoa pode doar sangue.")
else:
    print("Esta pessoa não pode doar sangue.")
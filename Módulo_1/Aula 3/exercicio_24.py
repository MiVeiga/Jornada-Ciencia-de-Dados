"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia  um conjunto indeterminado de temperaturas em Kelvin,
e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.Para parar ele deverá informar uma temperatura negativa
"""

from math import inf

maior = -inf
menor = inf
soma = 0
contador = 0

while True:
    temperatura = float(input("Digite a temperatura desejada em Kelvin.Para parar só digitar uma temperatura negativa "))
    if temperatura < 0:
        break
    
    contador += 1
    soma += temperatura
    if temperatura < menor :
        menor = temperatura
    if temperatura > maior: 
        maior = temperatura

print(f"A menor temperatura é {menor}K")
print(f"A mior temperatura é {maior}K")
print(f"A média das temperaturas é {soma/contador:.2f}K")








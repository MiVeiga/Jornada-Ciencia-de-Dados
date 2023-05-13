"""
Uma empresa precisa verificar se um funcionário está apto 
para receber um aumento de salário. 
Para isso, ela estabeleceu que o funcionário deve ter no mínimo 3 anos 
de experiência e um desempenho avaliado como "Bom" ou "Excelente". 
Escreva um programa em Python que receba a quantidade de anos de experiência 
e o desempenho do funcionário e verifique se ele está apto para receber o aumento.
"""

anos_experiencia = int(input("Digite a quantidade de anos de experiência do funcionário: "))
desempenho = input("Digite o desempenho avaliado do funcionário (Satisfátorio ou Bom ou Excelente): ")
if anos_experiencia >= 3 and (desempenho == "Bom" or desempenho == "Excelente"):
  print("O funcionário está apto para receber o aumento de salário.")
else:
  print("O funcionário não está apto para receber o aumento de salário.")
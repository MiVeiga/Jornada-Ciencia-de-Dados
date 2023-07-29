#Crie um módulo chamado "geometria" que contenha funções 
# para calcular a área e o perímetro de um retângulo. 
# Em seguida, crie um programa principal que importe esse módulo 
# e peça ao usuário para digitar a largura e a altura do retângulo. 
# O programa deve imprimir a área e o perímetro.

from modulos import geometria

b = float(input("Digite a base do retângulo: "))
h = float(input("Digite a altura do retângulo: "))

print("Área do retângulo:",geometria.area(b, h))
print("Perimetro do retângulo:",geometria.perimetro(b,h))
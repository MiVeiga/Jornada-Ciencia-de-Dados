#Imagine que em Codeville temos diferentes 
# formas gênios, como retângulos e círculos. 
# Vamos criar um exemplo de polimorfismo com 
# um método calcular_area compartilhado:

import math

class Formas_Geometricas:
    def calcular_area(self):
        pass

class Retangulo(Formas_Geometricas):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura


class Circulo(Formas_Geometricas):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

retangulo = Retangulo(5, 8)
circulo = Circulo(3)

formas = [retangulo, circulo]

for forma in formas:
    print(f"A area da forma é: {forma.calcular_area():.2f}")
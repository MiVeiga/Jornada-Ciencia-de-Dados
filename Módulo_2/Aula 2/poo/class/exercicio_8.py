#Crie uma classe chamada Circulo que tenha o atributo raio. 
#Em seguida, crie um método chamado area 
#que retorne a área do círculo (área = π * raio^2).

#ANDRE

# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio
    
#     def area(self):
#         area = 3.14 * (self.raio*self.raio)
#         print(f"Area:{area}")

# circulo1 = Circulo(5)
# circulo1.area()


#PEDRO
# class Circulo:

#     def __init__(self,raio):
#         self.raio = raio
    
#     def area(self):
#         pi = 3.1415926535898
#         return pi * (self.raio) ** 2


# circ1 = Circulo(6)
# print(f"Área: {circ1.area():.2f}")



#Jaime
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area (self):
        area = math.pi * (self.raio ** 2)
        print(f"A Área do Círculo, de raio {self.raio} é {area:.2f}.")

circulo1 = Circulo(10)
circulo1.area()
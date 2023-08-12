#Crie uma classe chamada Ponto que tenha os atributos x e y. 
# Em seguida, crie um método chamado mostrar_coordenadas que 
# imprima as coordenadas do ponto.

#Andre
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def mostrar_coordenadas(self):
        print(f"Coordenadas X:{self.x}\nCoordenadas Y:{self.y}")

local01 = Ponto(13, 10)
local01.mostrar_coordenadas()




#Em Codeville, temos diferentes tipos de veículos 
# que podem se mover de formas distintas. No entanto, 
# todos eles possuem um método "mover" 
# com comportamentos específicos.

#pass é uma instrução em Python que serve 
# como marcador de espaço reservado para onde 
# você pode colocar código no futuro


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print(f"O carro da marca {self.marca} {self.modelo} está se movendo nas estradas")


class Bicicleta(Veiculo):
    def mover(self):
        print(f"A bicicleta da marca {self.marca} {self.modelo} está se movendo na ciclovia")
    
class Patinete(Veiculo):
    def mover(self):
        print(f"O patinete  da marca {self.marca} {self.modelo} está me movendo pelas calçadas")


carro = Carro("Chevrolet", "Meriva")
bicicleta = Bicicleta("caloi", "velocidade")
patinete = Patinete("buldogue","xr800")

veiculos = [carro,bicicleta, patinete]

for veiculo in veiculos:
    veiculo.mover()
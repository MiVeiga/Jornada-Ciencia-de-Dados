#Imagine que em Codeville temos uma obediência 
# de animais, onde existem animais terrestres e 
# animais aquáticos. Vamos criar essa autoridade 
# usando herança:


class Animal:
    def __init__(self, nome, habitat):
        self.nome = nome
        self.habitat = habitat


class AnimalTerreste(Animal):
    def mover(self):
        print(f"O animal {self.nome} está se movendo na rua")


class AnimalAquatico(Animal):
    def nadar(self):
        print(f"O animal {self.nome} está nadando no Rio BlaBla")


cachorro = AnimalTerreste("Dog Maneiro", "Casa da Joana")
baleia = AnimalAquatico("Baleia Amiga", "Rio")

cachorro.mover()
baleia.nadar()


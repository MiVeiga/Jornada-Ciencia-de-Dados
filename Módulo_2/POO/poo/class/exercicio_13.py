#Crie uma classe chamada Animal que tenha 
# o atributo nome. Em seguida, crie um método 
# chamado emitir_som que imprima "O {nome} emitiu um som".


#Pedro
# class Animal:
#     def __init__(self,nome):
#         self.nome = nome

#     def emitirSom(self):
#         print(f"O {self.nome} emitiu um som!")

# cachorro = Animal('Scooby')
# cachorro.emitirSom()

# papagaio = Animal("Cibãm")
# papagaio.emitirSom()


#Vanessa

# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

#     def emitirSom(self):
#         print(f"O {self.nome} emitiu um som!")

# baleia = Animal("iiinnnñññññããããã")
# baleia.emitirSom()

# burro = Animal("inhõõõ")
# burro.emitirSom()

# galinha = Animal("cócócó")
# galinha.emitirSom()



class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def emitirSom(self):
        print(f"O {self.nome} emitiu um som: {self.som}!")

baleia = Animal("baleia","iiinnnñññññããããã")
baleia.emitirSom()

burro = Animal("burro","inhõõõ")
burro.emitirSom()

galinha = Animal("galinha", "cócócó")
galinha.emitirSom()
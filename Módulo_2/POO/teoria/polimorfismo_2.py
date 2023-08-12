#Suponha que em Codeville temos diferentes 
# instrumentos musicais, como violões e pianos.
# Vamos criar um exemplo de polimorfismo com 
# um método tocar compartilhado:

class InstrumentosMusicais:
    def tocar(self):
        pass

class Violao(InstrumentosMusicais):
    def tocar(self):
        print("Tocando acordes no violão")

class Piano(InstrumentosMusicais):
    def tocar(self):
        print("Tocando notas no piano")


violao = Violao()
piano = Piano()

instrumentos = [violao, piano]

for instrumento in instrumentos:
    instrumento.tocar()
#Crie uma classe chamada BonecaBarbie que tenha 
# os atributos nome, cor_cabelo e acessorios. 
# Em seguida, crie um método chamado mostrar_informacoes 
# que imprima as informações da boneca
#  (nome, cor do cabelo e acessórios).


class BonecaBarbie:
    def __init__(self, nome, cor_cabelo, acessorios):
        self.nome = nome
        self.cor_cabelo = cor_cabelo
        self.acessorios = acessorios
    
    def mostrar_informacoes(self):
        print(f"Boneca: {self.nome}, Cor de Cabelo: {self.cor_cabelo}, Acessório: {self.acessorios}")



barbie1 = BonecaBarbie("Barbie Fashion", "loiro", "colar")
barbie1.mostrar_informacoes()

barbie2 = BonecaBarbie("Barbie Maluca", "castranho", "pulseira")
barbie2.mostrar_informacoes()




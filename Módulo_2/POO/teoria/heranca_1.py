#Imagine que em Codeville, temos uma
# hierarquia de prédios. Existem prédios básicos, 
# como "PrédioResidencial" e "PrédioComercial". 
# Cada um deles herda algumas características da classe 
# "Prédio" e adiciona suas próprias particularidades.


class Predio:
    def __init__(self, endereco, andares):
        self.endereco = endereco
        self.andares  = andares
    
class PredioResidencial(Predio):
    def __init__(self, endereco, andares, numero_apartamentos):
        super().__init__(endereco, andares) #Chamando o construtor da classe pai
        self.numero_apartamentos = numero_apartamentos

class PredioComercial(Predio):
    def __init__(self, endereco, andares, numero_salas):
        super().__init__(endereco, andares)
        self.numero_salas = numero_salas


predio_residencial = PredioResidencial("Rua Bla, 123", 8, 40)
predio_comercial = PredioComercial("Rua A ,456", 4, 10 )

print("Informações do Prédio Residencial:")
print("Endereço:",predio_residencial.endereco)
print("Nº de andares:",predio_residencial.andares)
print("Nº de apartamentos:",predio_residencial.numero_apartamentos)

print("Informações do Prédio Comercial:")
print("Endereço:",predio_comercial.endereco)
print("Nº de andares:",predio_comercial.andares)
print("Nº de apartamentos:",predio_comercial.numero_salas)

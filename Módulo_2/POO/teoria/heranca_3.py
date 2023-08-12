#Suponha que em Codeville tenhamos diferentes 
# tipos de funcionários em uma empresa. 
# Vamos criar uma autoridade de 
# funcionários usando herança:

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
class Gerente(Funcionario):
    def administrar(self):
        print(f"O gerente {self.nome} está administrando a equipe, pois ele é {self.cargo}")

class Desenvolvedor(Funcionario):
    def programar(self):
        print(f"O desenvolvedor {self.nome} está programando novas funcionalidades pois ele é {self.cargo}")

gerente = Gerente("Pedro", "Gerente de Projetos")
dev = Desenvolvedor("Carlos", "Desenvolvedor Python")

gerente.administrar()
dev.programar()
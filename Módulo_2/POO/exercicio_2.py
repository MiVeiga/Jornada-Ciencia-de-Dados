# Na empresa Codeville Corp., os dados
# dos funcionários devem ser protegidos.
# Crie uma classe Funcionario com os atributos
# nome, cargo e salario. Mantenha o salário
# privado e adicione um método aumentar_salario para
# alterá-lo.

# Alisson
# class Funcionario:
#     def __init__(self, nome, salario, cargo):
#         self.nome = nome
#         self.__salario = salario
#         self.cargo = cargo

#     def getSalario(self):
#         return self.__salario

#     def getCargo(self):
#         return self.cargo

#     def aumentarSalario(self):
#         tipo = str(
#             input("Para aumento por porcentagem digite (p), para valor de aumento (v): "))
#         if tipo == "p":
#             aumento = float(
#                 input("Qual porcentagem voce deseja receber de aumento: "))
#             self.__salario *= ((aumento / 100) + 1)   
#         else:
#             aumento = float(
#                 input("Digite o valor que deseja receber de aumento: "))
#             self.__salario += aumento

#         print(f"Seu novo salário é {self.__salario}")


# funcionario = Funcionario("Alisson", 10000, "Dev full-stack")
# # print(funcionario.getSalario())
# # print(funcionario.getCargo())
# funcionario.aumentarSalario()


#Angelo
# class Funcionario:
#     def __init__(self,nome,cargo,salario):
#         self.nome = nome
#         self.cargo = cargo
#         self.__salario = int(salario)

#     def aumentar_salario(self,novo_salario):
#         print(f"Seu salario é de: R${self.__salario}  ")
#         self.__salario = novo_salario
#         print(f"Seu novo salario é de: R${novo_salario}")

# conta_bancaria = Funcionario("Roberto","Construtor","1200")

# conta_bancaria.aumentar_salario(1300)
#Imagine que em Codeville temos 
# uma classe para armazenar informações 
# de funcionários. Vamos aplicar o 
# encapsulamento usando os níveis de acesso.


class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.public_nome = nome
        self._protected_cpf = cpf
        self.__private_salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.public_nome}")
        print(f"CPF: {self._protected_cpf}")
        print(f"Salário: {self.__private_salario}")


funcionario = Funcionario("Alice", "98273812779", 5000)
funcionario.mostrar_informacoes()
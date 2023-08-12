#No Banco Codeville, você está criando 
# um sistema de contas bancárias. 
# Crie uma classe ContaBancaria com os 
# atributos titular, saldo e senha. 
# Garanta que a senha seja privada e 
# só possa ser alterada através de um 
# método alterar_senha

class ContaBancaria:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def ver_senha(self):
        print(f"Sua senha é: {self.__senha}") 
    
    def alterar_senha(self, senha_antiga, senha_nova):
        if senha_antiga == self.__senha:
            self.__senha = senha_nova
        else:
            print("Senha antiga incorreta")
    

conta = ContaBancaria("Milena", 100, "1234")
conta.ver_senha()
conta.alterar_senha("1234", "456")
conta.ver_senha()


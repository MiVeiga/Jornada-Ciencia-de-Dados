#Suponha que em Codeville temos uma 
# classe para representar contas bancárias 
# com informações recebidas. Vamos aplicar 
# o encapsulamento usando os níveis de acesso.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.public_titular = titular
        self._protected_saldo = saldo
        self.__private_codigo_acesso = "1234"
    
    def verificar_saldo(self):
        print(f"Saldo disponível: R$ {self._protected_saldo}")

    def __acessar_conta(self):
        print("Conta autorizada")


conta = ContaBancaria("Joao", 2000)
# print(conta._protected_saldo)
# conta.verificar_saldo()
# conta.__acessar_conta()
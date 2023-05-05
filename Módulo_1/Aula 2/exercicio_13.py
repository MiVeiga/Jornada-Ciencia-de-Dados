#Um banco quer um sistema para percorrer 
# a lista de transações de um cliente e calcular o saldo da conta.
#transacoes = [100, -50, 300, -200, 50]

#lista de transacoes
transacoes = [100, -50, 300, -200, 50]

saldo = 0

for transacao in transacoes:
    saldo += transacao

print('O saldo da conta é de R${:.2f}'.format(saldo))


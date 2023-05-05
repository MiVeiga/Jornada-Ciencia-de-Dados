# Um restaurante quer um sistema  para percorrer
# a lista de pedidos e calcular o valor total da conta.

#definindo uma lista de pedidos
itens_pedido = {'xbacon': 2, 'refri': 10, 'batata frita': 5}
print(itens_pedido)

#variavel do valor que a cliente vai pagar
total_conta = 0

#Percorreu a lista de pedido e calculou o valor total o pedido
for item, valor in itens_pedido.items():
    total_conta += valor
print("O valor total da conta é de R$ {:.2f}".format((total_conta)))




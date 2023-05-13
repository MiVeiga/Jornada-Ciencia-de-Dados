
""""
Uma loja precisa gerar um relatório de vendas de seus produtos,
listando o nome de cada produto e a quantidade vendida. 
Escreva um programa em Python que receba o nome e 
a quantidade vendida de cada produto e armazene as informações em um dicionário. 
Ao final, o programa deve imprimir o relatório de vendas
"""

relatorio_vendas = {}

while True:
    produto = input("Digite o nome do produto(ou digite sair para encerrar): \n")
    if produto == "sair":
        break

    quantidade = int(input("Digite a quantidade vendida do produto:"))
    relatorio_vendas[produto] = quantidade

print("Relatório de vendas")

for produto, quantidade in relatorio_vendas.items():
    print(f"{produto}:{quantidade} unidades vendidas.")


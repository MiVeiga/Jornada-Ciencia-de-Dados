"""
 Uma loja de roupas está fazendo uma promoção onde oferece 
 descontos de 10%  para compras acima de R$ 200,00. 
 Escreva um programa em Python que receba o valor total 
 da compra e calcule o valor final com desconto, se houver.
"""

"""
Douglas
valor_total = float(input("Digite o valor total da compra: \n"))

if valor_total > 200:
    valor_desconto = valor_total * 0.1
    valor_final = valor_total - valor_desconto
    print(f"O valor com desconto é de R$ {valor_final:.2f}")
else:
    print(f"O valor final é de R$ {valor_total:.2f}")

"""

"""
Miguel

conta = float(input("Digite o valor da conta? \n"))
print("Valor da compra: ", conta)
if conta >= 200:
    desconto = (conta * 10) /100
    valorFinal = conta - desconto
    print(f"O valor com desconto é de {valorFinal}")
else:
    print(f"Valor final é de {conta}")
"""


"""
Elcio

desconto = 10 / 100

compra = float(input("Informe o valor da sua compra, Comprando acima de 200 reais, você ganha um desconto de 10 porcentos!"))


if compra >= 200.00:
    print("Sua compra é acima de 200 reais e saíra com desconto!")
    print(f"O valor da sua compra com desconto é {compra - compra * desconto}")
else:
    print(f"Sua compra é {compra}, somente compras de 200 reais ou acima ganham o desconto!!")


"""

"""
Jaime

valor_compra = float(input("Informe o valor da compra: \n"))
valor_final = 0

if valor_compra > 200:
    valor_final = valor_compra * 0.9
    print(f"O valor da sua compra com desconto é: {valor_final:.2f}")
else:
    print(f"Valor da compra é {valor_compra:.2f}")

"""

"""
Willian/Guilherme

valor_compra = float(input('Digite o valor da compra: '))

if valor_compra >= 200:
    valor_compra -= valor_compra * 0.1

print(f'Valor total da compra: {valor_compra:.2f}')
"""

"""
Pedro
compras = [5,23,123,2]
soma_das_compras = sum(compras)
preco_com_desconto = 0

if soma_das_compras > 200:
    preco_com_desconto = soma_das_compras - (soma_das_compras * 0.10)
    print(f"A Compra no valor de R${soma_das_compras} teve 10% de desconto, está custando R${preco_com_desconto} ")
else:
    diferenca_para_desconto = 200 - soma_das_compras
    print(f"Sua compra deu R${soma_das_compras}")
    print(f"Se comprar mais R${diferenca_para_desconto} em produtos vc aproveita 10% de desconto")
"""


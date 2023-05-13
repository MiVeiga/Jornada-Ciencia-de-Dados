"""
Uma loja precisa calcular o valor final de uma compra, 
considerando que há um desconto de 10% para compras acima de R$ 100,00 
e um acréscimo de 5% para compras parceladas em 3 vezes. 
Escreva um programa em Python que receba o valor total da compra 
e a forma de pagamento (à vista ou parcelado em 3 vezes) 
e calcule o valor final com os devidos descontos ou acréscimos.

"""

"""
Miguel

parcelas = int(input("Quantas parcelas será?  Até 3 vezes possível\n"))
compra = float(input("Digite o valor da compra? \n"))

if compra >= 100:
    desconto = (compra *10) / 100
    print(f"Desconto de {desconto:.2f}")
    valorFinal = compra - desconto
    print(f"Valor final: {valorFinal:.2f}")
elif parcelas == 3:
    acrescimo = (compra * 5) / 100
    print(f"Acrescimo de {acrescimo:.2f}")
    valorFinal = compra + acrescimo
    print(f"Valor final: {valorFinal:.2f}")
else:
    print(f"Valor final: {compra:.2f}")
"""

"""
William/Guilherme
valor_total = float(input('Qual o valor total da compra? '))
forma_pagamento = input('Qual a forma de pagamento? v = à vista, p = à prazo: ')

if valor_total > 100:
    valor_total -= valor_total * 0.1
    print(f'10% de desconto aplicado.')

if forma_pagamento.lower() == 'p':
    parcelas = int(input('Será parcelado em quantas vezes? '))
    if parcelas == 3:
        valor_total += valor_total * 0.05
        print(f'5% de acréscimo aplicado.')

print(f'Valor a pagar: {valor_total:.2f}')

"""

"""
Jaime

valor_compra = float(input("Informe o valor da compra: \n"))
forma_pgto = (input("Informe a forma de pagamento: 1x ou 3x \n"))
valor_final = 0

if valor_compra > 100 and forma_pgto == "1x":
    valor_final = valor_compra * 0.9
    print(f"O valor da sua compra com desconto à vista é de R${valor_final:.2f}")
elif valor_compra > 100 and forma_pgto == "3x":
    valor_final = (valor_compra * 0.9) * 1.05
    print(f"O valor da sua compra é de R${valor_final:.2f}")
elif valor_compra <= 100 and forma_pgto == "3x":
    valor_final = valor_compra * 1.05
    print(f"O valor da sua compra é de R${valor_final:.2f}")
else:
    print(f"O valor da compra é R${valor_compra:.2f}")

"""

"""
Douglas

valor_compra = float(input("Qual o valor da compra? \n"))
pagamento = input(f"Deseja pagar a vista ou parcelado? (V) ou (P)").strip().upper()

while pagamento not in ["V", "P"]:
    pagamento = input("Forma de pagamento inválida. Informe a forma de pagamento novamente (V para a vista ou P para parcelado): ")

if valor_compra > 100.0 and pagamento == "V":
    valor_compra = valor_compra * 0.9


if pagamento == "P":
    valor_compra = valor_compra * 1.05

print(f"O valor final da compra é de : R$ {valor_compra:.2f}")

"""


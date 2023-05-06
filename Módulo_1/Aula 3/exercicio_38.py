"""
Crie um programa que verifique se uma pessoa pode 
pegar um empréstimo de acordo com suas condições financeiras. 
Considere que uma pessoa pode pegar um empréstimo 
se a parcela não ultrapassar 30% da 
renda mensal e se a renda mensal for maior que R$1500,00.
"""


valor_emprestimo = float(input("Digite o valor do empréstimo: "))
numero_parcelas = int(input("Digite o número de parcelas: "))
renda_mensal = float(input("Digite a renda mensal: "))
valor_parcela = valor_emprestimo / numero_parcelas
if valor_parcela <= renda_mensal * 0.3 and renda_mensal > 1500:
    print("Você pode pegar o empréstimo.")
else:
    print("Você não pode pegar o empréstimo.")
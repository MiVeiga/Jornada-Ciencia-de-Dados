# Você precisa criar um dicionário
# chamado "cardapio" para armazenar os
# pratos do restaurante e seus respectivos preços.
# Adicione os seguintes pratos ao cardápio:
# "Bife à Parmegiana" com preço de R$ 30.90, "Salada Caesar"
# com preço de R$ 15.50 e "Mousse de Chocolate" com preço de
# R$ 8.75. Imprima o cardápio completo com os preços.

cardapio = {
    "Bife à Parmegiana": 30.90,
    "Salada Caesar": 15.50,
    "Mousse de Chocolate": 8.75
}

for prato, preco in cardapio.items():
    print(f"{prato}: R${preco}")
#Um e-commerce quer um sistema
# para percorrer a lista de produtos em promoção 
# e exibir uma mensagem de desconto para cada um.
#produtos_promocao = ['Camiseta', 'Calça', 'Tênis']
#percentual_desconto = 20

produtos_promocao = ['Camiseta', 'Calça', 'Tênis']
percentual_desconto = 20
preco_original = 100

for produto in produtos_promocao:
    preco_promocional = preco_original-(preco_original*(percentual_desconto/100))
    print(f"{produto} está com {percentual_desconto}% de desconto. De R${preco_original:2f} por R${preco_promocional}")
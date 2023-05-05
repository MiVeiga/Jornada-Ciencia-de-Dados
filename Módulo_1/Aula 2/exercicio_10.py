#Verificar se o produto tem desconto e qual é o valor final
# produto maior igual a 100 reais tem 10%
# produto maior igual a 50 reais tem 5%


preco = float(input("Digite o preço do produto: "))
if preco >= 100:
  desconto = preco * 0.1
  preco_final = preco - desconto
  print("O produto tem 10% de desconto.")
else:
  if preco >= 50:
    desconto = preco * 0.05
    preco_final = preco - desconto
    print("O produto tem 5% de desconto.")
  else:
    desconto = 0
    preco_final = preco
    print("O produto não tem desconto.")
print("O preço final do produto é R$", preco_final)
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                #      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
# R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos 
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


#Pegar do cliente os valores/kg das frutas

morango = float(input("Digite quantos quilos de morango foram comprados \n"))
maca = float(input("Digite quantos quilos de maça foram comprados \n"))

#variavel do valor final que cliente vai pagar
valor = 0

# alimentando a variavel de valor ou seja preco que o cliente vai pagar.
if morango <= 5:
    valor += morango * 2.5
else:
    valor += morango * 2.2

if maca <= 5:
    valor += maca * 1.8
else:
    valor += maca * 1.5


#Descontos do cliente

if(morango + maca) > 8 or valor > 25:
    valor -= valor * 10 / 100


print(f"O valor final da compra é: {valor:.2f}")
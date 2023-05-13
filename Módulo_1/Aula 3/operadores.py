#Operadores Lógicos:

#AND: and
#OR: or
#NOT: not

#Operadores Aritméticos:

#Adição: +
#Subtração: -
#Multiplicação: *
#Divisão: /
#Divisão inteira: //
#Resto da divisão: %
#Exponenciação: **


#Operadores de Comparação:

#Igualdade: ==
#Desigualdade: !=
#Maior que: >
#Menor que: <
#Maior ou igual a: >=
#Menor ou igual a: <=
#A variavel recebe o resto da outra variavel: %=


# Exemplo de operadores lógicos
x = 10
y = 5

if x > 5 and y < 10:
    print("Os dois testes são verdadeiro")

if x > 5 or y < 2:
    print("Pelo menos um dos testes é verdadeiro")

if not x < y:
    print("x não é menor que y")


# Exemplo de operadores aritméticos

a = 10
b = 3


print(a + b) #SOMA
print(a - b) #SUBTRACAO
print(a * b) #MULTIPLICACAO
print(a / b) #DIVISAO
print(a // b) #DIVISAO INTEIRA
print(a % b)  #RESTO DA DIVISAO
print(a ** b) #EXPONENCIAÇÃO



# Exemplo de operadores de comparação

x = 10
y = 5

if x == y: 
    print("x é igual a y")

if x != y:
    print("x é diferente de y")

if x > y:
    print("x é maior que y")

if x < y:
    print("x é menor que y")

if x >= y:
    print("x é maior ou igual a y")

if x <= y:
    print("x é menor ou igual a y")

# if :
#     print("")
    
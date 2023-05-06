
# Percorrendo uma lista de números e imprimindo cada um
#quando se sabe antecipadamente o número de vezes que se deseja repetir uma ação

numeros = [1, 2, 3, 4, 5]

for numero in numeros: 
    print(numero)

# Repetindo até que o usuário digite um número positivo

numero = -1

while numero < 0:
    numero = int(input("Digite um número positivo: \n"))

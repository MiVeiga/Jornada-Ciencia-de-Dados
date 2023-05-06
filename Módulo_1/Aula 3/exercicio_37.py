#Crie um programa que verifique se um número é par e positivo ao mesmo tempo.


num = int(input("Digite um número: "))
if num > 0 and num % 2 == 0:
    print("O número é positivo e par.")
else:
    print("O número não é positivo e par.")
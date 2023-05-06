"""
Crie um programa que verifique se um número é 
divisível por 3 e 7 ao mesmo tempo ou se é maior que 100 e menor que 200.
"""

num = int(input("Digite um número: "))
if (num % 3 == 0 and num % 7 == 0) or (num > 100 and num < 200):
    print("O número é divisível por 3 e 7 ao mesmo tempo ou está entre 100 e 200.")
else:
    print("O número não satisfaz as condições.")
